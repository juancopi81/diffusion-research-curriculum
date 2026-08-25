# Week 9 - Linear Algebra in Diffusion Architectures

**Status:** Complete.

**References:**

- [Week 9 linear algebra note](./w09_mml_linear_algebra.md)
- [Week 9 PCA/SVD notebook](../notebooks/w09_pca_svd_solved.ipynb)
- MML §10.4, eigenvector computation and low-rank approximation
- Optional bridge: MML §10.7, latent-variable perspective on PCA

## Linear Operations Inside Larger Nonlinear Models

Once their parameters have been learned, dense layers, convolutions, and
feature projections apply linear transformations during a forward pass. A
dense layer can be written as

$$
h' = \phi(Wh+b),
$$

where $Wh$ is linear, adding $b$ makes the transformation affine, and the
activation $\phi$ makes the complete layer nonlinear. A convolution has the
same structure, except that its learned weights are shared across spatial
locations. Attention also uses learned linear projections to produce queries,
keys, values, and outputs.

These operations do not make an entire U-Net, attention block, or residual
block linear. U-Nets contain nonlinear activations and normalization layers.
Attention weights depend on the input through the softmax of scaled
query-key products. A residual block has the form $x+F(x)$ and remains
nonlinear whenever $F$ is nonlinear. The linear maps are building blocks
inside a larger nonlinear function.

## Compression and Latent Representations

PCA and a learned encoder both map data into a lower-dimensional
representation from which it can be reconstructed. In the notebook, PCA
encoded each centered 2D observation using its coordinate along one principal
direction and decoded it back onto a line through the empirical mean. This was
a lossy compression because the second coordinate was removed.

PCA is itself learned from data, but it learns one global linear subspace and
optimizes squared reconstruction error. A nonlinear encoder-decoder can map
data to and from a curved low-dimensional manifold and can use architectural
structure, such as convolutions, to model spatial patterns. A latent diffusion
model uses such a learned encoder to transform images into a lower-dimensional
latent tensor before diffusion and a decoder to return to image space. This is
specific to latent diffusion; pixel-space diffusion does not require this
compression stage. Greater expressiveness also does not guarantee that every
learned feature is semantically meaningful.

## Low-Rank Intuition

The leading direction had variance $8.1944$, compared with $0.3143$ in the
second direction, so retaining one component preserved approximately $96.3\%$
of the total variance. The resulting reconstruction MSE was $0.3143$, exactly
the variance associated with the discarded direction under the notebook's
covariance convention. Keeping both components reduced the MSE to approximately
$3.16\times10^{-31}$, which is zero up to floating-point error.

The reconstruction plot makes the truncation visible: reconstructed points lie
on the leading principal line, while the residual segments show the discarded
orthogonal variation. Dominant directions are useful for compact
reconstruction, but high variance is not the same as semantic importance. For
an image dataset, lighting or background could create large variance while a
small, low-variance feature could determine an object's identity. PCA has no
labels or downstream objective with which to distinguish them.

LoRA uses a related low-rank idea by parameterizing a weight update as
$\Delta W=BA$. This reduces the number of trainable parameters by constraining
the update to low rank; it does not guarantee that every unrestricted update
can be represented without loss.

## Main Takeaway

PCA gave a concrete example of encoding, reconstruction, and low-rank
approximation: it retained the dominant linear direction and discarded a
measurable residual. Latent diffusion similarly relies on a compact
representation, and diffusion architectures repeatedly use linear operations
such as convolutions and learned projections. The limitation is that PCA uses
a single global linear subspace chosen by variance and reconstruction error,
whereas a latent diffusion system uses nonlinear learned representations and a
denoising model whose goal is to learn the structure of a full data
distribution. The analogy explains some building blocks, not the whole model.
