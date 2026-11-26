# Week 17 — DDPM worked derivation and study record

These are the attempts, prompts, corrections, and handwritten pages from Days 1–3. For the mathematical argument from forward noising through the training objective, see the [Week 17 concept note](../notes/w17_ddpm_posterior_and_objective.md).

## Day 1 — Reading the algorithms through the notebook

With the notebook closed, Juan picked the gradient update in Algorithm 1. He used the prompt to recall the function name and correctly identified the two tensors in the loss as the actual corruption noise and the model’s prediction. For Algorithm 2 he remembered drawing the starting image with `torch.randn`. He initially placed that draw inside the reverse step. After the tutor pointed him to the outer loop, he found the line and explained why replacing the training batch size with his sample count gives `(n_samples, 1, 28, 28)`.

| Paper step | What Juan traced in the Week 16 notebook |
| --- | --- |
| Algorithm 1, draw a timestep and corrupt a clean image | `prepare_batch` draws a timestep per image and fresh noise. It forms $x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon$ directly and returns that same $\epsilon$ as the target. |
| Algorithm 1, update the model | `train_step` calls the model on $(x_t,t)$, computes the MSE against $\epsilon$, and takes an optimizer step. After Juan’s recap, the tutor clarified that the clean image and sampled noise are used to **construct** the network input. |
| Algorithm 2, initialize and iterate | `sample_loop` draws $x_T$ from a standard Gaussian. The clean batch supplies dimensions, dtype, and device. The loop runs from $T$ through $1$. |
| Algorithm 2, take one reverse step | `single_step_reverse` calls the model at each step. Juan identified $\beta_t$ and $\bar\alpha_t$ as schedule values in the reverse mean. For $t>1$ the code adds fresh noise scaled by the step’s standard deviation. At $t=1$ it sets $z=0$ and returns the computed mean. |

[DDPM, Algorithms 1 and 2](https://arxiv.org/pdf/2006.11239#page=4) · [Week 16 solved notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

## Day 2 — Deriving the clean-conditioned posterior

### Apply Bayes with the clean image already fixed

Juan remembered using Bayes with one observation in Week 4 and asked how to handle two conditioning values. The tutor suggested holding $x_0$ fixed first. On paper, Juan set $A=X_{t-1}$ and $B=X_t$, then used $P_c$ for the law conditional on $X_0=c$. Ordinary Bayes under $P_c$ then gives the density identity below. [Week 4 Bayes derivation](../notes/w04_conditioning_in_diffusion.md#checkpoint-21-complete-derivation) · [Handwritten Bayes setup](../notes/figures/w17_day2_01_conditional_bayes_handwritten.png)

$$
q(y\mid x_t,x_0)
=\frac{q(x_t\mid y,x_0)\,q(y\mid x_0)}{q(x_t\mid x_0)}
\propto q(x_t\mid y)\,q(y\mid x_0),
\qquad y=x_{t-1}.
$$

The denominator is constant in $y$. The forward Markov property gives $q(x_t\mid y,x_0)=q(x_t\mid y)$. Juan identified the first factor as one forward step and the second as accumulated corruption through $t-1$. His first page used $\epsilon\ne0$ to justify the nondegenerate case. The tutor clarified that the condition is on the **variance**, $1-\bar\alpha_{t-1}>0$, which holds for $t>1$ under this schedule. [Week 15 forward laws](../notes/w15_forward_process_discrete.md#the-direct-conditional-distribution)

### Read the Gaussian parameters from the log density

Write $\alpha_t=1-\beta_t$ and $\bar\alpha_t=\alpha_t\bar\alpha_{t-1}$. In one dimension the two factors have means $\sqrt{\alpha_t}\,y$ and $\sqrt{\bar\alpha_{t-1}}\,x_0$, respectively. Juan used the Week 4 approach of expanding both squares while keeping $x_0$ and $x_t$ fixed. [Handwritten Gaussian factors and expansion](../notes/figures/w17_day2_02_gaussian_factors_handwritten.png)

$$
\log q(y\mid x_t,x_0)
=-\frac{(x_t-\sqrt{\alpha_t}\,y)^2}{2\beta_t}
 -\frac{(y-\sqrt{\bar\alpha_{t-1}}\,x_0)^2}{2(1-\bar\alpha_{t-1})}
 +C(x_t,x_0).
$$

The terms involving $y$ were correct on the first expansion. The tutor flagged the constant inside the second square, $\bar\alpha_{t-1}x_0^2$. Juan corrected it and collected the terms independent of $y$ into $C(x_t,x_0)$. With prompts to name the two brackets and compare them with a Gaussian log density, he obtained the following coefficients. [Handwritten coefficient matching](../notes/figures/w17_day2_03_matching_coefficients_handwritten.png)

$$
\log q(y\mid x_t,x_0)=-\tfrac12 A y^2+B y+C(x_t,x_0),
$$

$$
A=\frac{\alpha_t}{\beta_t}+\frac{1}{1-\bar\alpha_{t-1}},
\qquad
B=\frac{\sqrt{\alpha_t}\,x_t}{\beta_t}
+\frac{\sqrt{\bar\alpha_{t-1}}\,x_0}{1-\bar\alpha_{t-1}}.
$$

Matching powers of $y$ gave $A=1/\sigma^2$ and $B=\mu/\sigma^2$. The tutor suggested keeping the denominator factored. Juan used $\alpha_t(1-\bar\alpha_{t-1})+\beta_t=1-\bar\alpha_t$ to simplify $1/A$, then multiplied $B$ by that variance to get the mean. He compared his result with Equation 7 **after** doing the algebra. [Handwritten mean and variance](../notes/figures/w17_day2_04_mean_and_variance_handwritten.png) · [DDPM, Equations 6–7](https://arxiv.org/pdf/2006.11239#page=3)

$$
\tilde\beta_t=\frac{1}{A}
=\beta_t\frac{1-\bar\alpha_{t-1}}{1-\bar\alpha_t},
$$

$$
\tilde\mu_t(x_t,x_0)=\frac{B}{A}
=\frac{\sqrt{\bar\alpha_{t-1}}\,\beta_t}{1-\bar\alpha_t}\,x_0
+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}\,x_t.
$$

### Check the last page against the derivation

- **Which alpha goes under the root?** Juan’s derived coefficient of $x_t$ on page 4 correctly uses $\sqrt{1-\beta_t}=\sqrt{\alpha_t}$. An extra bar appeared when copying it onto page 5.
- **What equals one at $t=1$?** Juan found the unit coefficient of $x_0$ and zero variance. The tutor clarified that the $x_1$ coefficient vanishes, so the **mean equals $x_0$**. The variance expression still carries $\beta_1$, multiplied by $1-\bar\alpha_0=0$. The posterior puts all its mass on the known clean image. In generation the clean image is unknown, and the notebook returns the model’s final mean.
- **Why does the scalar result extend to images?** Juan distinguished correlations among clean pixels across the dataset from the independent corruption of each pixel. With $x_0$ and $x_t$ fixed, both Gaussian factors separate across coordinates. The tutor pointed out that every pixel uses the same schedule, so all diagonal entries agree. This gives covariance $\tilde\beta_t I$ and explains the factor $\sqrt{\tilde\beta_t}$ multiplying standard Gaussian noise in the notebook.

For $t>1$, the image-level result is

$$
q(x_{t-1}\mid x_t,x_0)
=\mathcal N\!\left(x_{t-1};\tilde\mu_t(x_t,x_0),\tilde\beta_t I\right).
$$

[Handwritten paper comparison and boundary check](../notes/figures/w17_day2_05_paper_and_boundary_handwritten.png)

## Day 3 — Averaging over possible clean images

Juan proposed two routes in his opening answer. He could average all the candidate posterior means, or he could average the possible clean images first and calculate the posterior mean just once. He was unsure whether the two operations give the same result.

The tutor identified the weighting law $q(x_0\mid x_t)$ and supplied the affine form $a_t x_0+b_t x_t$ from Day 2. Juan then split the conditional expectation by linearity, pulled out the schedule coefficient $a_t$, and kept $b_t x_t$ intact because $x_t$ is already observed. [Juan’s handwritten calculation](../notes/figures/w17_day3_01_conditional_mean_handwritten.png)

$$
\mathbb E[a_tX_0+b_t x_t\mid X_t=x_t]
=a_t\,\mathbb E[X_0\mid X_t=x_t]+b_t x_t.
$$

The tower property identifies the left side as the reverse mean $\mathbb E[X_{t-1}\mid X_t=x_t]$. The right side evaluates the Day 2 mean at the posterior average clean image. This proves the equivalence Juan proposed. [Day 3 plan](../notes/w17_study_plan.md#day-3--from-the-posterior-to-predicted-noise)

Given the forward noising equation, Juan solved for $x_0$ using the actual noise $\epsilon$, then substituted the model prediction $\epsilon_\theta(x_t,t)$. Both algebraic steps were correct. His last line kept the label $x_0$. The tutor added a hat there to mark the clean-image estimate obtained with predicted noise. [Handwritten rearrangement and substitution](../notes/figures/w17_day3_02_clean_from_predicted_noise_handwritten.png) · [Week 16 prediction conversions](../notes/w16_prediction_parameterizations.md#setup-and-prediction-conversions)

$$
\hat x_{0,\theta}(x_t,t)
=\frac{x_t-\sqrt{1-\bar\alpha_t}\,\epsilon_\theta(x_t,t)}
{\sqrt{\bar\alpha_t}}.
$$

On the next page Juan used the hat for the model estimate. To find the actual posterior mean, he returned to the equation with the sampled noise and took its conditional expectation. He pulled out the schedule coefficients and the observed $x_t$, leaving the conditional mean of the noise. The tutor flagged a missing $\epsilon$ inside the second expectation on the intermediate line. Juan had already included it correctly in his final expression. [Handwritten conditional expectation](../notes/figures/w17_day3_03_conditional_noise_mean_handwritten.png)

$$
\mathbb E[X_0\mid X_t=x_t]
=\frac{x_t-\sqrt{1-\bar\alpha_t}\,\mathbb E[\epsilon\mid X_t=x_t]}
{\sqrt{\bar\alpha_t}}.
$$

Juan restored the missing $\epsilon$ and compared the two expressions side by side. He identified the ideal prediction as $\mathbb E[\epsilon\mid X_t=x_t]$, in his words “the average noise that could have produced this particular $x_t$.” Substituting that prediction makes the clean-image estimate equal the posterior mean. The tutor flagged one notation slip in the closing sentence of the page. The observation is $X_t=x_t$, with $t$ denoting the timestep. [Corrected page and comparison](../notes/figures/w17_day3_04_noise_predictor_comparison_handwritten.png)

Juan then substituted the entire clean-image estimate into the $x_0$ term of his Day 2 mean. The substitution was correct. When he copied the separate $x_t$ term, he wrote $\sqrt{\bar\alpha_t}$ where Day 2 gave $\sqrt{\alpha_t}$. With that bar corrected, the model’s reverse mean before simplification is

$$
\mu_\theta(x_t,t)=
\frac{\sqrt{\bar\alpha_{t-1}}\,\beta_t}{1-\bar\alpha_t}
\left(\frac{x_t-\sqrt{1-\bar\alpha_t}\,\epsilon_\theta(x_t,t)}{\sqrt{\bar\alpha_t}}\right)
+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}\,x_t.
$$

[Handwritten substitution](../notes/figures/w17_day3_05_reverse_mean_substitution_handwritten.png)

Juan corrected the separate $x_t$ coefficient in both lines. Using the suggested identity $\bar\alpha_t=\alpha_t\bar\alpha_{t-1}$, he factored the denominator and canceled $\sqrt{\bar\alpha_{t-1}}$, obtaining $\sqrt{\bar\alpha_{t-1}}/\sqrt{\bar\alpha_t}=1/\sqrt{\alpha_t}$. [Corrected substitution and cancellation](../notes/figures/w17_day3_06_schedule_ratio_handwritten.png)

The tutor put the two coefficients of $x_t$ over a common denominator. Juan expanded the numerator to $\beta_t+\alpha_t-\alpha_t\bar\alpha_{t-1}=1-\bar\alpha_t$. He then canceled $1-\bar\alpha_t$ against the matching denominator factor, leaving $x_t/\sqrt{\alpha_t}$ as the first term of the reverse mean. [Handwritten simplification of the coefficient](../notes/figures/w17_day3_07_reverse_mean_xt_coefficient_handwritten.png)

Given the unsimplified noise coefficient, Juan canceled one factor of $\sqrt{1-\bar\alpha_t}$ and retained the minus sign. His last line gives $-\beta_t/(\sqrt{\alpha_t}\sqrt{1-\bar\alpha_t})$. [Handwritten noise coefficient](../notes/figures/w17_day3_08_reverse_mean_noise_coefficient_handwritten.png)

The tutor combined Juan’s two coefficients by factoring out $1/\sqrt{\alpha_t}$.

$$
\mu_\theta(x_t,t)=\frac{1}{\sqrt{\alpha_t}}
\left(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\epsilon_\theta(x_t,t)\right).
$$

This is the mean computed by the Week 16 sampler. Its denominator in code is $\sqrt{1-\beta_t}=\sqrt{\alpha_t}$. [DDPM, Equation 11](https://arxiv.org/pdf/2006.11239#page=4) · [Week 16 sampler](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

### From mean error to noise error

Juan wrote the model mean minus the clean-conditioned mean. With this order, he correctly canceled the two $x_t$ terms and obtained the sign $\epsilon-\epsilon_\theta$. His second line also dropped the shared $1/\sqrt{\alpha_t}$. The tutor pointed out that this factor multiplies both noise terms and can be pulled outside the difference. Restoring it gives

$$
\mu_\theta(x_t,t)-\tilde\mu_t(x_t,x_0)
=\frac{\beta_t}{\sqrt{\alpha_t}\sqrt{1-\bar\alpha_t}}
\bigl(\epsilon-\epsilon_\theta(x_t,t)\bigr).
$$

The prompt used the opposite subtraction order. Reversing the order changes the sign and gives the same squared norm. [Juan’s first subtraction](../notes/figures/w17_day3_09_mean_difference_attempt_handwritten.png)

Juan restored $1/\sqrt{\alpha_t}$ in both noise terms and squared the common coefficient correctly. His last line says “take squared norm” and omits the superscript on the norm itself. Applying $\|cv\|^2=c^2\|v\|^2$ gives the corrected line below. [Corrected subtraction and squared coefficient](../notes/figures/w17_day3_10_squared_mean_error_handwritten.png)

$$
\|\mu_\theta(x_t,t)-\tilde\mu_t(x_t,x_0)\|^2
=\frac{\beta_t^2}{\alpha_t(1-\bar\alpha_t)}
\|\epsilon-\epsilon_\theta(x_t,t)\|^2.
$$

For $t>1$, the tutor connected this identity to the fixed reverse variance $\sigma_t^2$. Equation 8 multiplies the squared mean error by $1/(2\sigma_t^2)$, giving the timestep weight $\beta_t^2/[2\sigma_t^2\alpha_t(1-\bar\alpha_t)]$ on the squared noise error in Equation 12. [DDPM, Equations 8 and 12](https://arxiv.org/pdf/2006.11239#page=3)

**Day 3 closing comparison.** Given the weight, Juan explained that the same squared noise error contributes differently at two timesteps if their weights differ. In his Week 16 noise MSE, both errors contribute equally. For a per-example error $e$, Equation 12 uses $w_t e$ and Equation 14 uses $e$. The notebook samples timesteps uniformly and applies MSE directly to predicted and sampled noise. [DDPM, Equations 12 and 14](https://arxiv.org/pdf/2006.11239#page=4) · [Week 16 training notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

### Handoff to the next session

Juan proposed averaging the possible clean images before the tutor supplied the weighting law. With the affine form given, he showed why that shortcut works. He also explained the loss weighting once the weight was on the page. The reverse-mean algebra was guided, with the corrected coefficients preserved above. Day 4 brings those coefficients back in code when Juan traces which schedule values the reverse step needs outside the notebook. [Day 4 plan](../notes/w17_study_plan.md#day-4--move-the-working-pieces-into-nano-diffusion)

## Day 4 — Tracing the reverse step’s inputs

Reading `single_step_reverse`, Juan spotted `alpha_bar` in the first lookup and traced `t_tensor` back to the supplied `t` and `x_t`. The function builds that index locally. After a prompt to inspect the third lookup, he identified `betas` and explained that the caller currently supplies neither schedule table. [Week 16 notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

Juan proposed keeping the four existing parameters and passing both schedule tables explicitly:

```python
def single_step_reverse(
    x_t: torch.Tensor,
    t: int,
    model: nn.Module,
    generator: torch.Generator,
    alpha_bar: torch.Tensor,
    betas: torch.Tensor,
) -> torch.Tensor:
    ...
```

The existing lookups can use those parameter names directly. When the function is extracted, its caller will need to pass the two tables.

In `prepare_batch`, Juan identified both schedule dependencies on his first pass. The function uses `T` to set the range of sampled timesteps and `alpha_bar` to look up the coefficient for each image. Asked to use the table as the sampling bound, he reasoned that its shape is `(T + 1,)` and wrote:

```python
t = torch.randint(1, alpha_bar.shape[0], (len(clean),), generator=generator)
```

The exclusive upper bound preserves the original draw from timesteps 1 through `T`. Passing `alpha_bar` therefore supplies both the coefficients and the information needed to draw `t`.

Reading the Gaussian initialization in `sample_loop`, Juan identified the dtype, device, and shape of `clean_batch`. He correctly noted that `n_samples` replaces the batch dimension. The image values themselves come from the random draw.

Juan proposed passing the per-image shape, dtype, and device explicitly, along with the two schedule tables. He identified `alpha_bar.shape[0] - 1` as the starting timestep. After the tutor supplied the descending range, Juan wrote the update below with all six arguments in signature order. The assembled sketch retains the notebook’s no-gradient decorator and final return.

```python
@torch.no_grad()
def sample_loop(
    model: nn.Module,
    generator: torch.Generator,
    n_samples: int,
    image_shape: tuple[int, int, int],
    dtype: torch.dtype,
    device: torch.device,
    alpha_bar: torch.Tensor,
    betas: torch.Tensor,
) -> torch.Tensor:
    x_t = torch.randn((n_samples, *image_shape), dtype=dtype, device=device, generator=generator)
    for t in range(alpha_bar.shape[0] - 1, 0, -1):
        x_t = single_step_reverse(x_t, t, model, generator, alpha_bar, betas)
    return x_t
```

Juan extracted the schedule, coefficient lookup, and forward batch into `diffusion.py`. His guarded smoke check passed in a fresh CPU process. During review, the tutor checked the three-step schedule and lookup against hand-calculated values. On nonzero images, the extracted function returned exactly the same timesteps, noise, and noisy images as the Week 16 notebook for $T=1,3,1000$ with seeds 16 and 42. Following review, Juan added assertions for the cumulative schedule, the two gathered values, and their broadcast shape, then ran the smoke check successfully.

Juan then extracted `single_step_reverse` with `alpha_bar`, `betas`, and `generator` as the final three parameters. The tutor ran the [Week 16 scalar example](../notes/w16_hf_ddpm_training.md#tracing-one-reverse-step) against this implementation. At $t=2$, it returned $0.894427$ with $z=0$ and $0.694427$ with $z=-0.6$. At $t=1$, it returned the expected mean and preserved the generator state. When connecting the loop above, pass `alpha_bar=alpha_bar, betas=betas, generator=generator` to match the implemented signature.

Juan implemented `sample_loop` and recorded the timestep labels received by a constant model. His smoke check confirmed that both images visited $3,2,1$ in order and the output was finite with shape `(2, 1, 4, 4)`. The tutor also compared the loop with the Week 16 notebook using the same untrained `TinyDenoiser`. With seed 16, the output tensors and final generator states matched exactly for both the one-step and three-step CPU runs.

Juan moved `TinyDenoiser` into `model.py`. His check paired two MNIST-shaped inputs with timestep labels `[1, 3]` and confirmed the noise predictions were finite and had the input shape. The tutor also passed the same image twice and swapped the labels. The two predictions differed and swapped with the labels. With identical weights and inputs, the extracted model and the Week 16 notebook produced identical CPU predictions and parameter gradients.

Juan extracted `train_step` and cloned the parameters before the Adam update so the check could detect a weight change. On the seeded synthetic batch from `prepare_batch`, the tutor verified a finite noise MSE of 0.9693 and identical updated parameters in the extracted and notebook implementations. Review found that the smoke block still needed an explicit assertion for the finite loss. A rerun of the separate model smoke check found 16 images paired with the original two timestep labels.

Juan added `assert math.isfinite(loss)` and restored the two-image batch for labels `[1, 3]`. Both scripts passed on rerun, including the finite-loss and weight-change assertions.
