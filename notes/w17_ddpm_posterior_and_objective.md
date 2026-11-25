# Week 17 — The DDPM Posterior and Objective

Days 1 and 2 are complete. This note brings together Juan’s study conversation and his five handwritten pages. [Week 17 plan](w17_study_plan.md)

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

Juan remembered using Bayes with one observation in Week 4 and asked how to handle two conditioning values. The tutor suggested holding $x_0$ fixed first. On paper, Juan set $A=X_{t-1}$ and $B=X_t$, then used $P_c$ for the law conditional on $X_0=c$. Ordinary Bayes under $P_c$ then gives the density identity below. [Week 4 Bayes derivation](w04_conditioning_in_diffusion.md#checkpoint-21-complete-derivation) · [Handwritten Bayes setup](figures/w17_day2_01_conditional_bayes_handwritten.png)

$$
q(y\mid x_t,x_0)
=\frac{q(x_t\mid y,x_0)\,q(y\mid x_0)}{q(x_t\mid x_0)}
\propto q(x_t\mid y)\,q(y\mid x_0),
\qquad y=x_{t-1}.
$$

The denominator is constant in $y$. The forward Markov property gives $q(x_t\mid y,x_0)=q(x_t\mid y)$. Juan identified the first factor as one forward step and the second as accumulated corruption through $t-1$. His first page used $\epsilon\ne0$ to justify the nondegenerate case. The tutor clarified that the condition is on the **variance**, $1-\bar\alpha_{t-1}>0$, which holds for $t>1$ under this schedule. [Week 15 forward laws](w15_forward_process_discrete.md#the-direct-conditional-distribution)

### Read the Gaussian parameters from the log density

Write $\alpha_t=1-\beta_t$ and $\bar\alpha_t=\alpha_t\bar\alpha_{t-1}$. In one dimension the two factors have means $\sqrt{\alpha_t}\,y$ and $\sqrt{\bar\alpha_{t-1}}\,x_0$, respectively. Juan used the Week 4 approach of expanding both squares while keeping $x_0$ and $x_t$ fixed. [Handwritten Gaussian factors and expansion](figures/w17_day2_02_gaussian_factors_handwritten.png)

$$
\log q(y\mid x_t,x_0)
=-\frac{(x_t-\sqrt{\alpha_t}\,y)^2}{2\beta_t}
 -\frac{(y-\sqrt{\bar\alpha_{t-1}}\,x_0)^2}{2(1-\bar\alpha_{t-1})}
 +C(x_t,x_0).
$$

The terms involving $y$ were correct on the first expansion. The tutor flagged the constant inside the second square, $\bar\alpha_{t-1}x_0^2$. Juan corrected it and collected the terms independent of $y$ into $C(x_t,x_0)$. With prompts to name the two brackets and compare them with a Gaussian log density, he obtained the following coefficients. [Handwritten coefficient matching](figures/w17_day2_03_matching_coefficients_handwritten.png)

$$
\log q(y\mid x_t,x_0)=-\tfrac12 A y^2+B y+C(x_t,x_0),
$$

$$
A=\frac{\alpha_t}{\beta_t}+\frac{1}{1-\bar\alpha_{t-1}},
\qquad
B=\frac{\sqrt{\alpha_t}\,x_t}{\beta_t}
+\frac{\sqrt{\bar\alpha_{t-1}}\,x_0}{1-\bar\alpha_{t-1}}.
$$

Matching powers of $y$ gave $A=1/\sigma^2$ and $B=\mu/\sigma^2$. The tutor suggested keeping the denominator factored. Juan used $\alpha_t(1-\bar\alpha_{t-1})+\beta_t=1-\bar\alpha_t$ to simplify $1/A$, then multiplied $B$ by that variance to get the mean. He compared his result with Equation 7 **after** doing the algebra. [Handwritten mean and variance](figures/w17_day2_04_mean_and_variance_handwritten.png) · [DDPM, Equations 6–7](https://arxiv.org/pdf/2006.11239#page=3)

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

[Handwritten paper comparison and boundary check](figures/w17_day2_05_paper_and_boundary_handwritten.png)

## Where Day 3 starts

Juan has a mean for the case where both endpoints are given. The next question is how to combine those means when only the noisy image is observed. The discussion stopped at that question. The predicted-noise form and the weighted versus simplified loss follow later in the session. [Day 3 plan](w17_study_plan.md#day-3--from-the-posterior-to-predicted-noise)
