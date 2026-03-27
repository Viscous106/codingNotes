# 1) Theoretical vs Empirical Probability

### Theoretical Probability

Computed mathematically using formula and assumptions (like fair coin/die).

### Empirical Probability

Observed from actual trials/simulations:

$$
\hat{P}(E) = \frac{\text{count of event occurrences}}{n}
$$

If you toss a coin many times, observed probability of heads may be close to 0.5, but not exactly 0.5 every time.

- `random.choice(...)` for single random outcomes.
- `numpy.random.choice(...)` for many trials.

Example concept:

- Simulate 1000 coin tosses.
- Count heads.
- Estimate probability as `heads / 1000`.

As trials increase, empirical probability usually gets closer to theoretical value.

---

## 2) Intro Statistics in the Lecture

After probability basics, lecture introduces core statistical measures:

### Mean (Average)

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

### Variance

$$
\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

### Standard Deviation

$$
\sigma = \sqrt{\sigma^2}
$$

- Variance and standard deviation measure spread.
- Standard deviation is in same unit as the data.

---
