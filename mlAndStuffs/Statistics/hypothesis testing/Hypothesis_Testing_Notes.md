# Hypothesis Testing Notes

---

## 📚 What's In These Notes — Study Topics

> Read this first to plan what you need to study before an exam or assignment.

| # | Topic | Difficulty | What You'll Learn |
|---|---|---|---|
| 1 | **One-Sample T-Test** | 🟢 Easy | Test if a sample mean matches a claimed value (e.g., "avg marks = 70?") |
| 2 | **One-Sample Z-Test (Proportions)** | 🟢 Easy | Test if a sample proportion matches a claim (e.g., "60% users like product?") |
| 3 | **Independent Two-Sample T-Test** | 🟡 Medium | Compare two different groups (e.g., online vs offline students) |
| 4 | **Paired T-Test** | 🟡 Medium | Compare the same group before and after something (e.g., weight before/after gym) |
| 5 | **Chi-Square Goodness of Fit** | 🟡 Medium | Check if observed frequencies match expected (e.g., is a dice fair?) |
| 6 | **Chi-Square Test of Independence** | 🟡 Medium | Check if two categorical variables are related (e.g., smoking & lung disease) |
| 7 | **Covariance & Correlation** | 🟢 Easy | Measure how strongly two numeric variables move together |
| 8 | **Yulu Case Study (Full EDA + Testing)** | 🔴 Hard | Apply all tests to real data — the assignment pattern |

### 🗺️ How Topics Connect

```
All Hypothesis Tests follow the same 5 steps:
  1. State H₀ and H₁
  2. Choose the right test (use the cheatsheet at the bottom)
  3. Set significance level α (usually 0.05)
  4. Run the test → get p-value
  5. If p ≤ α → Reject H₀ | If p > α → Fail to reject H₀
```

### ⚠️ The 3 Things Most People Get Wrong
1. **Confusing independent vs paired t-test** — ask yourself: "Is it the SAME people measured twice, or TWO different groups?"
2. **Forgetting the alpha level changes the conclusion** — p=0.10 is rejected at α=0.10 but NOT at α=0.05.
3. **Using t-test on categorical data** — if your data is categories (yes/no, colours, products), always use **Chi-Square**, not T-test.

---



> **Lectures covered:** Other Distributions, One-Sample Tests (Mar 26), Two-Sample Tests (Mar 31), Chi-Square (Apr 2), Yulu Case Study (Apr 7)

---

## 🧠 The Big Picture — What is Hypothesis Testing?

Hypothesis testing is how you use **data from a sample** to make a decision about a **claim on the whole population**.

You always define two competing statements:
- **H₀ (Null Hypothesis):** The default claim. "Nothing happened." "It's equal."
- **H₁ (Alternate Hypothesis):** The challenge. "Something is different."

**The golden rule:**
> If `p-value ≤ α` → **Reject H₀** (the evidence is strong enough)
> If `p-value > α` → **Fail to reject H₀** (not enough evidence)

The significance level **α = 0.05** (5%) is the standard threshold used in most problems unless stated otherwise.

---

## 1) One-Sample Tests

Use when you are testing **one group against a fixed claimed value**.

### Which test to use?

| Data Type | Test | When |
|---|---|---|
| Numerical (means) | **T-test** | Sample mean vs claimed mean |
| Categorical (proportions) | **Z-test** | Sample proportion vs claimed proportion |

---

### 1a. One-Sample T-Test (for means)

**Question type:** "A college claims the average marks = 70. Is this true?"

**Steps:**
1. State H₀ and H₁
2. Run `stats.ttest_1samp(data, mu)`
3. Compare p-value with α

```python
import scipy.stats as stats

data = [72, 68, 75, 70, 69, 74, 71, 73, 67, 76]
mu = 70      # the claimed population mean
alpha = 0.05

t_stat, p_value = stats.ttest_1samp(data, mu)
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value <= alpha:
    print("Reject H₀: Average is significantly different from 70")
else:
    print("Fail to reject H₀: No significant difference from 70")
# Result: P-Value = 0.15 → Fail to reject H₀
```

**Real examples from lecture:**
- *Coaching institute claims average study time = 6 hrs/day.* → Sample of 12 students, p = 0.22 → No significant difference.
- *Gym claims average weight loss = 3 kg.* → Use same pattern.

---

### 1b. One-Sample Z-Test (for proportions)

**Question type:** "A company claims 60% of users like their product. Survey shows 52/100 like it. Is the claim valid?"

```python
import statsmodels.stats.proportion as smp

success = 52   # number of successes in sample
n = 100        # sample size
p0 = 0.6       # claimed proportion
alpha = 0.05

z_stat, p_value = smp.proportions_ztest(success, n, p0, alternative="two-sided")
print("Z-Statistic:", z_stat)
print("P-Value:", p_value)

if p_value <= alpha:
    print("Reject H₀: Proportion is significantly different from 60%")
else:
    print("Fail to reject H₀: Proportion is not significantly different")
# Result: p = 0.109 → Fail to reject H₀ at α=0.05
# But if α=0.10, it would be rejected!
```

> 💡 **Key insight:** The alpha level you choose matters a lot. Changing α from 0.05 to 0.10 can flip the conclusion!

---

## 2) Two-Sample Tests

Use when you want to **compare two separate groups** against each other.

### Which test to use?

| Situation | Test |
|---|---|
| Two **independent** groups (e.g., online vs offline class) | **Independent T-Test** (`ttest_ind`) |
| **Same group, measured twice** (e.g., before/after training) | **Paired T-Test** (`ttest_rel`) |

---

### 2a. Independent Two-Sample T-Test

**Question:** "Do online students perform differently from offline students?"

```python
import scipy.stats as stats

Online  = [62, 65, 70, 68, 72, 66, 64]
Offline = [75, 78, 74, 77, 80, 76, 79]

t_stat, p_value = stats.ttest_ind(Online, Offline)
print("T-Statistic:", t_stat)    # -6.62
print("P-Value:", p_value)       # 0.0000247

if p_value <= 0.05:
    print("Reject H₀: Significant difference in performance")
# Result: p ≈ 0.000025 → Reject H₀
# Offline mean (77) is clearly higher than Online mean (66.7)
```

---

### 2b. Paired T-Test (Before vs After)

**Question:** "Did a 4-week gym program significantly reduce weight?"

- Same people, measured **before** AND **after**. The measurements are paired/linked.
- Use `ttest_rel` instead of `ttest_ind`.

```python
Before = [82, 85, 78, 90, 88, 76, 80]
After  = [78, 82, 75, 86, 84, 74, 77]

t_stat, p_value = stats.ttest_rel(After, Before)
print("T-Statistic:", t_stat)    # -11.5
print("P-Value:", p_value)       # 0.000026

if p_value <= 0.05:
    print("Reject H₀: Training significantly reduced weight")
# Result: Reject H₀ — the program WORKS.
```

> 💡 **Paired vs Independent — Simple Rule:**
> - **Same people, two timepoints** → Paired (`ttest_rel`)
> - **Two different groups** → Independent (`ttest_ind`)

---

## 3) Chi-Square Tests

Use when your data is **categorical** (e.g., colours, yes/no, product names). There's no mean to compare — you compare **counts/frequencies**.

Two flavours:

| Test | Question |
|---|---|
| **Goodness of Fit** | Does the observed distribution match the expected? |
| **Test of Independence** | Are two categorical variables related to each other? |

---

### 3a. Chi-Square Goodness of Fit

**Question:** "Is the dice fair? We rolled 60 times and got [8, 12, 9, 11, 10, 10]. Expected = 10 each."

```python
import scipy.stats as stats

observed = [8, 12, 9, 11, 10, 10]
expected = [10, 10, 10, 10, 10, 10]   # fair dice → each face equally likely

chi2, p_value = stats.chisquare(observed, expected)
print("Chi-Square:", chi2)    # 1.0
print("P-Value:", p_value)    # 0.963

if p_value < 0.05:
    print("Reject H₀: Dice is NOT fair")
else:
    print("Fail to reject H₀: Dice IS fair")
# Result: p = 0.96 → Dice is fair. The small differences are just random chance.
```

**Another example:** "Company claims preferences are Product A=50%, B=30%, C=20%. Survey of 200: [90, 70, 40]."

```python
observed = [90, 70, 40]
total = sum(observed)  # 200
expected = [0.5*total, 0.3*total, 0.2*total]   # [100, 60, 40]

chi2, p_value = stats.chisquare(observed, expected)
# Result: p = 0.26 → Fail to reject → survey matches the claimed distribution
```

---

### 3b. Chi-Square Test of Independence

**Question:** "Is smoking related to lung disease?" (Two categorical variables, observed in a contingency table.)

```python
import numpy as np
import scipy.stats as stats

# Contingency table:
#              Disease   No Disease
# Smoker         60         40
# Non-Smoker     30         70
data = np.array([
    [60, 40],
    [30, 70]
])

chi2, p_value, dof, expected = stats.chi2_contingency(data)
print("Chi2:", chi2)        # 16.99
print("P-Value:", p_value)  # 0.0000376
print("DoF:", dof)          # 1 (degrees of freedom)
print("Expected:\n", expected)

if p_value < 0.05:
    print("Reject H₀: Smoking and lung disease ARE related")
# Result: Clearly related — Reject H₀.
```

> 💡 The **expected table** printed by `chi2_contingency` shows what the counts would look like if the two variables were completely **independent**. The further the observed is from expected, the higher the chi2 statistic and the lower the p-value.

---

## 4) Covariance & Correlation (from Apr 2 lecture)

These measure the **relationship between two numeric variables**.

```python
import numpy as np

X = np.array([2, 4, 6, 8, 10])
Y = np.array([50, 60, 65, 70, 75])

# Covariance — direction of relationship (positive/negative)
cov_mat = np.cov(X, Y, bias=True)
cov_xy = cov_mat[0, 1]
print("Covariance:", cov_xy)     # 24.0

# Correlation — strength + direction, always between -1 and +1
corr = np.corrcoef(X, Y)[0, 1]
print("Correlation:", corr)      # 0.986 → very strong positive relationship
```

| Correlation Value | Meaning |
|---|---|
| ~1.0 | Perfect positive (as X↑, Y↑) |
| ~0.0 | No relationship |
| ~-1.0 | Perfect negative (as X↑, Y↓) |

---

## 5) Yulu Case Study — Hypothesis Testing in Practice

**Context:** Yulu is India's electric bike rental service. Revenue dropped. The task is to find what factors affect demand using hypothesis testing.

**Dataset columns:** `datetime`, `season`, `holiday`, `workingday`, `weather`, `temp`, `humidity`, `windspeed`, `casual`, `registered`, `count`

### EDA Steps Applied

```python
import pandas as pd

df = pd.read_csv("bike_sharing.csv")

# Basic inspection
df.info()
df.isnull().sum()       # check for nulls
df.drop_duplicates(inplace=True)  # remove duplicate rows

# Feature engineering from datetime
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour']    = df['datetime'].dt.hour
df['weekday'] = df['datetime'].dt.weekday

# Drop highly correlated feature (atemp ≈ temp)
df.drop('atemp', axis=1, inplace=True)
```

### Hypothesis Tests to Run (What the assignment asks)

| Question | Test |
|---|---|
| Weekday vs Weekend bike rides different? | Independent T-test (`ttest_ind`) |
| Average daily demand = 500? | One-sample T-test (`ttest_1samp`) |
| Average temp on high-demand days ≠ 25°C? | One-sample T-test |
| Working day vs Weekend demand different? | Independent T-test |
| Demand before/after a promotion? | Paired T-test (`ttest_rel`) |
| Customer preferences match expected %? | Chi-Square Goodness of Fit |
| Weather condition and demand related? | Chi-Square Independence (`chi2_contingency`) |
| Weather differs across seasons? | Chi-Square Independence |

---

## 🔑 Master Cheatsheet — Which Test to Use?

```
Data is NUMERICAL?
  └─ Comparing ONE group to a fixed value?
       └─ → One-Sample T-Test  (stats.ttest_1samp)
  └─ Comparing TWO groups?
       └─ Same people, before/after?
            └─ → Paired T-Test  (stats.ttest_rel)
       └─ Different people/groups?
            └─ → Independent T-Test  (stats.ttest_ind)

Data is CATEGORICAL?
  └─ Does observed distribution match expected percentages?
       └─ → Chi-Square Goodness of Fit  (stats.chisquare)
  └─ Are two categorical variables related?
       └─ → Chi-Square Independence  (stats.chi2_contingency)

Comparing a PROPORTION to a fixed value?
  └─ → Z-Test for Proportions  (smp.proportions_ztest)
```

---

## 📌 Key Terms Summary

| Term | Meaning |
|---|---|
| **H₀** | Null hypothesis — the default/status quo claim |
| **H₁** | Alternative hypothesis — what you're trying to prove |
| **α (alpha)** | Significance level, usually 0.05 (5% chance of wrong rejection) |
| **p-value** | Probability of observing your result if H₀ were true. Low p → reject H₀ |
| **T-statistic** | How many standard errors apart the sample is from the claimed value |
| **Chi-square (χ²)** | Measures how different observed counts are from expected counts |
| **Degrees of Freedom (DoF)** | Number of independent values free to vary in the calculation |
| **Paired test** | Same subjects measured twice (before/after) |
| **Independent test** | Two completely separate groups |
