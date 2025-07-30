import math

def ncr(n, r):
    if r > n or n < 0 or r < 0:
        return "Invalid input"
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def npr(n, r):
    if r > n or n < 0 or r < 0:
        return "Invalid input"
    return math.factorial(n) // math.factorial(n - r)

def bernoulli_Trials(prob, num_trials, total_num):
    if not (0 <= prob <= 1) or num_trials < 0 or total_num < 0:
        return "Invalid input"
    return ((ncr(total_num, num_trials)) * (prob ** num_trials) * ((1 - prob) ** (total_num - num_trials)))

def geo_dist(prob, num_trials):
    if not (0 <= prob <= 1) or num_trials < 0:
        return "Invalid input"
    return (prob * ((1 - prob) ** (num_trials - 1)))
