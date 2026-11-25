# Week 17 — The DDPM Posterior and Objective

During training, both the clean image and the noise added to it are known. During generation, the sampler has only the current noisy image and its timestep. How can a network trained to predict noise tell the sampler where to go next? The link is the mean of the previous state given the current one. [Worked derivation and handwritten pages](../proofs/w17_ddpm_worked_derivation.md)

## Day 1 — Reading the algorithms through the notebook

Let $\beta_t$ be the variance of the noise added at step $t$, $\alpha_t=1-\beta_t$, and $\bar\alpha_t=\prod_{s=1}^t\alpha_s$, with $\bar\alpha_0=1$. A single forward step retains a factor of $\sqrt{\alpha_t}$ of the previous state. Starting from the clean image instead, all $t$ steps can be sampled in one draw, with $\epsilon\sim\mathcal N(0,I)$:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon.
$$

| DDPM algorithm | How it works in the Week 16 MNIST notebook |
| --- | --- |
| 1. Training | For each clean image, `prepare_batch` draws a uniform timestep and Gaussian noise, then constructs $x_t$ in one shot. `train_step` gives $(x_t,t)$ to the network and takes an optimizer step on the MSE between its prediction and that same noise draw. |
| 2. Sampling | `sample_loop` starts with $x_T\sim\mathcal N(0,I)$ and counts down to $1$. At each step, `single_step_reverse` uses the network prediction and schedule to compute a mean. It adds scaled fresh noise for $t>1$ and returns the mean at $t=1$. |

The network’s output has the same meaning in both algorithms. Training uses a known corruption draw as the target. Sampling uses the prediction to compute the reverse mean, then makes a separate random draw to sample around that mean. [DDPM, Algorithms 1 and 2](https://arxiv.org/pdf/2006.11239#page=4) · [Week 16 notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

## Day 2 — Deriving the clean-conditioned posterior

**If we knew the clean image, where could the previous state have been?** Fix $x_0$, $x_t$, and $t>1$. Let $y=x_{t-1}$. Bayes’ rule under the law conditioned on $x_0$ gives

$$
q(y\mid x_t,x_0)\propto q(x_t\mid y)\,q(y\mid x_0).
$$

The first factor asks how likely the observed $x_t$ is after one step from $y$. The forward Markov property makes $y$ sufficient for that step. The second factor tells us which values of $y$ are plausible after $t-1$ steps from $x_0$. Both factors are Gaussian. For one coordinate their product has log density

$$
-\frac{(x_t-\sqrt{\alpha_t}\,y)^2}{2\beta_t}
-\frac{(y-\sqrt{\bar\alpha_{t-1}}\,x_0)^2}{2(1-\bar\alpha_{t-1})}
+C(x_t,x_0).
$$

Collecting powers of $y$ gives $-Ay^2/2+By+C$, so the variance is $1/A$ and the mean is $B/A$. Simplifying with $\bar\alpha_t=\alpha_t\bar\alpha_{t-1}$ gives

$$
\tilde\beta_t=\beta_t\frac{1-\bar\alpha_{t-1}}{1-\bar\alpha_t},
\qquad
\tilde\mu_t(x_t,x_0)=
\frac{\sqrt{\bar\alpha_{t-1}}\,\beta_t}{1-\bar\alpha_t}\,x_0
+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}\,x_t.
$$

For an image, both Gaussian factors split across pixels and the schedule uses the same noise scale for each pixel. The posterior therefore has covariance $\tilde\beta_t I$. At $t=1$, the previous state is the very $x_0$ we conditioned on. Its conditional mean is $x_0$ and its variance is zero. [DDPM, Equations 6–7](https://arxiv.org/pdf/2006.11239#page=3) · [Coefficient matching and boundary check](../proofs/w17_ddpm_worked_derivation.md#read-the-gaussian-parameters-from-the-log-density)

## Day 3 — Averaging over possible clean images

**Can we average the possible clean images first, then compute the reverse mean just once?** Yes. With $x_t$ observed, each possible $x_0$ gets its weight from $q(x_0\mid x_t)$. Write the two coefficients from Day 2 as $a_t,b_t$. The tower property and the affine form of the mean give

$$
\begin{aligned}
\mathbb E[X_{t-1}\mid X_t=x_t]
&=\mathbb E[\tilde\mu_t(x_t,X_0)\mid X_t=x_t]\\
&=a_t\,\mathbb E[X_0\mid X_t=x_t]+b_t x_t.
\end{aligned}
$$

That last line is the Day 2 mean evaluated at the average plausible clean image. It determines the reverse **mean**. The reverse distribution averages over multiple clean images and can have additional variability.

### Getting the reverse mean from a noise prediction

Solve the forward noising equation for $X_0$ and take its conditional expectation at fixed $t$. The schedule and the observed $x_t$ are fixed, so only the noise needs to be averaged:

$$
\mathbb E[X_0\mid X_t=x_t]
=\frac{x_t-\sqrt{1-\bar\alpha_t}\,\mathbb E[\epsilon\mid X_t=x_t]}
{\sqrt{\bar\alpha_t}}.
$$

Under squared error the ideal noise predictor outputs precisely that conditional average, the average noise that could have produced this particular $x_t$. Substituting the trained predictor $\epsilon_\theta(x_t,t)$ for the conditional noise mean gives a clean-image estimate $\hat x_{0,\theta}$. Substituting that estimate into $a_t\hat x_{0,\theta}+b_t x_t$ gives the model mean

$$
\mu_\theta(x_t,t)=\frac{1}{\sqrt{\alpha_t}}
\left(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\epsilon_\theta(x_t,t)\right).
$$

This is `mean` in `single_step_reverse`. The sampler separately chooses the fixed variance $\tilde\beta_t$ and uses its **square root** to scale a fresh standard Gaussian draw. At $t=1$ the code sets that draw to zero and outputs the model’s final mean. [DDPM, Equation 11 and Algorithm 2](https://arxiv.org/pdf/2006.11239#page=4) · [Week 16 sampler](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

### From mean error to noise error

For a training example, the clean-conditioned mean can be written in the same form using the actual noise $\epsilon$. Subtracting the two means cancels the common $x_t$ term. Squaring the difference gives

$$
\|\mu_\theta-\tilde\mu_t\|^2
=\frac{\beta_t^2}{\alpha_t(1-\bar\alpha_t)}
\|\epsilon-\epsilon_\theta(x_t,t)\|^2.
$$

For $t>1$, Equation 8 weights this squared mean error by $1/(2\sigma_t^2)$, where $\sigma_t^2$ is the model’s fixed reverse variance at that step. Thus Equation 12 weights the squared **noise** error by

$$
w_t=\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar\alpha_t)}.
$$

If two sampled timesteps have the same squared noise error $e$, their contributions to Equation 12 are $w_t e$ and $w_s e$. The simplified objective in Equation 14 drops this explicit timestep weight. That is the Week 16 training choice: sample timesteps uniformly and use plain noise MSE, so equal errors contribute equally. [DDPM, Equations 8, 12, and 14](https://arxiv.org/pdf/2006.11239#page=3) · [Worked mean-error subtraction](../proofs/w17_ddpm_worked_derivation.md#from-mean-error-to-noise-error)
