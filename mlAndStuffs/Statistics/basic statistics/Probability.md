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
- ---
  ---

## 3) Data Analysis Libraries
### NumPy
- Array creation and math operations.
- **Descriptive stats**: `np.mean()`, `np.median()`, `np.var()`, `np.std()`.
- **Random simulation**:
  - `np.random.random()`: floats between 0.0 and 1.0.
  - `np.random.randint()`: random integers.
  - `np.random.choice()`: pick items given weights/probabilities.
  - `np.random.normal(loc, scale, size)`: normal distribution.
  - `np.random.uniform()`: uniform distribution.

### Pandas & Matplotlib
- **DataFrames**: 2D data tables. Column filtering e.g., `df[df["column"] == "value"]`.
- `value_counts(normalize=True)` helps calculate relative frequencies (empirical probability).
- `pd.crosstab()` calculates marginal/joint probabilities.
- **Plotting**: `plt.hist()` (distributions), `plt.bar()` (counts), `sns.boxplot()` (outliers), `sns.heatmap()` (correlation matrices).

---

## 4) Core Probability Concepts

- **Conditional Probability**: The probability of $A$ given $B$ has occurred.
  $$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$
- **Independent Events**: Occurrence of one does not affect the other.
- **Mutually Exclusive**: Events cannot happen together ($P(A \cap B) = 0$).

### Bayes' Theorem
Used to update probabilities when new evidence is observed.
$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$
- **Prior probability ($P(A)$)**: Belief before evidence.
- **Likelihood ($P(B|A)$)**: Probability of evidence given the condition.
- **Posterior probability ($P(A|B)$)**: Updated belief after evidence.

---

## 5) Statistical Distributions

### Uniform Distribution
- All outcomes are equally likely (e.g., rolling a fair die).
- Constant probability density across the interval.

### Normal Distribution
- Continuous, bell-shaped, and symmetric.
- Center of distribution: $Mean = Median = Mode$.
- **Empirical Rule**:
  - ~68% of data falls within 1 standard deviation ($\mu \pm 1\sigma$).
  - ~95% of data falls within 2 standard deviations ($\mu \pm 2\sigma$).
- **Central Limit Theorem Application**: The distribution of sample means follows a normal distribution even if the population does not.

### Binomial Distribution
- Models the number of successes in $n$ independent trials (e.g., tossing coins), where $p$ is the probability of success.
- $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$

---

## 6) Hypothesis Testing (One Sample)

Used to test claims (e.g., "The average score is 70") against sample data using a significance level (often $\alpha = 0.05$).

- **One-Sample T-Test** (For numerical data means, e.g., test scores, weights):
  - Used generally when the sample size is small or standard deviation is unknown.
  - Python: `scipy.stats.ttest_1samp(data, mu)`
- **One-Sample Z-Test for Proportions** (For categorical fractions e.g., "60% of users like it"):
  - Python: `statsmodels.stats.proportion.proportions_ztest(success, n, p0)`
- **Decision Rule**:
  - Calculate the **p-value**.
  - If **$p \leq \alpha$**: **Reject** the null hypothesis (the difference is significant).
  - If **$p > \alpha$**: **Fail to reject** the null hypothesis (the difference is not significant).

---

## 7) Exploratory Data Analysis (EDA) — Aerofit Case Study

EDA is the process of **understanding your data before modeling** using descriptive stats and visualizations.

### Step-by-Step EDA Workflow

1. **Load & Inspect**
   ```python
   df = pd.read_csv(url)
   df.head()       # first 5 rows
   df.shape        # (rows, columns)
   df.info()       # data types & nulls
   df.describe()   # statistical summary
   df.isnull().sum() # check missing values
   ```

2. **Univariate Analysis** (one variable at a time)
   - Categorical → `sns.countplot(x="Product", data=df)`
   - Numerical → `sns.histplot(df["Age"], bins=20)` or `sns.boxplot(x=df["Income"])`

3. **Bivariate Analysis** (relationship between two variables)
   - Categorical vs Categorical → `sns.countplot(x="Product", hue="Gender", data=df)`
   - Categorical vs Numerical → `sns.boxplot(x="Product", y="Income", data=df)`

4. **Outlier Detection**
   - Use **boxplots** — points outside the whiskers are outliers.
   - Compare `mean` vs `median`: a large gap often signals outliers pulling the mean.

5. **Correlation Analysis** (how strongly two numeric variables relate)
   - Ranges from **-1** (perfect negative) to **+1** (perfect positive). Near 0 = no relation.
   ```python
   corr = df.corr(numeric_only=True)
   sns.heatmap(corr, annot=True)  # visual matrix of correlations
   ```

---

### Probability Tables with crosstab

| Type | What it shows | Code |
|---|---|---|
| **Marginal Probability** | Single-event probability e.g., P(KP281) | `pd.crosstab(df["Product"], columns="Prob", normalize=True)` |
| **Joint/Conditional Probability** | e.g., P(KP781 \| Male) | `pd.crosstab(df["Gender"], df["Product"], normalize="index")` |

---

### Customer Profiling
Group data by a category and compute average characteristics:
```python
df.groupby("Product")[["Age", "Income", "Fitness", "Miles"]].mean()
```
**Aerofit Insights (example findings):**
- **KP281** (entry-level, $1500): mostly bought by lower-income customers (~$46k), 3x/week usage.
- **KP781** (advanced, $2500): higher income (~$75k), high fitness rating, 5x/week, 160 miles/week.
- Males buy more treadmills than females; KP781 is almost exclusively male buyers.
- Income > $70k → almost exclusively KP781 purchases.
- Miles and Usage have the strongest correlation (0.76).

---

## 🔑 Quick-Reference Summary

| Topic | Key Formula / Concept |
|---|---|
| Empirical Probability | `count of event / n trials` |
| Conditional Probability | `P(A\|B) = P(A∩B) / P(B)` |
| Bayes' Theorem | `P(A\|B) = P(B\|A)·P(A) / P(B)` |
| Binomial | `P(X=k) = C(n,k)·p^k·(1-p)^(n-k)` |
| Normal 68-95-99.7 | 68% within ±1σ, 95% within ±2σ |
| Variance | `σ² = Σ(xᵢ - x̄)² / n` |
| T-Test (mean) | `scipy.stats.ttest_1samp(data, mu)` |
| Z-Test (proportion) | `smp.proportions_ztest(success, n, p0)` |
| Reject H₀ if | `p-value ≤ α` |
