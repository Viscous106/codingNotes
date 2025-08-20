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

########Joint PMF:
###How to find probability for more than one variable:

#if P(X=x) and  p(Y=y) is given:
'''laws are that p(x,y) must be >=0 and that the sum of P(X=x)and P(Y=y) must be 1...'''

########Marginal PMF:
'''sum of a rows or coloummns joint pmf is a marginal pmf'''

###coditional pmf with do variable dependenency:
'''Q(t')=P(Y=t'|X=t)= fxy(t,t')/fx(t)'''#table problems

###Poision Pmf:
#when two events occurs simultaneously and independently:
'''P(X=k)=(e^(-Lam))((lam)^k)/k!'''

###How to check independence:
'''iif fXY(x,y)=fX(x)*fY(y)'''

###Independent and identical distribution:
'''/home/viscous/#Viscous/codingNotes/statsNotesPythonStyle/Independence.png'''

###Poissons distribution:
'''X=lam1
   Y=lam2
   Z=X+Y
   then P(Z)=(((lam1)+(lam2))^k)(e^(-((lam1+(lam2)))))/k!'''

###Poisons distribution for x given z:
'''X|Z=~Binomial (k,(lam1)/((lam1)+(lam2)))'''

###Cumulative distributive frequency:
#Max:
'''cum of maximum Z=max(X,Y)
FZ(z)=FX(z)+FY(z)
'''
#Min:
'''cum of maximum freq Z=min(x,y)
FZ(z)=P(min(X,Y)<=z)
FZ(z)=1-P(min(X,Y)>z)
FZ(z)=1-(1-FX(z)(1-FY(z)))
'''

#Expected value of  discrete RV OR Mean:
'''E[X]=sum(t.fx(t))'''

#refer this:
'''/home/viscous/#Viscous/codingNotes/statsNotesPythonStyle/PMF E[X.png'''

#property:
'''E[aX+bY]=aE[X]+bE[Y]'''