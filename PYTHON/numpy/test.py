import numpy as np
sample=100000
result=np.random.randint(1,11,size=sample)
test=np.random.randint(1,101,size=sample)
hasD=(result==1)
noD=(result>1)
posiT=hasD & (test<=95)
negaT=noD & (test<=5)
testP=negaT|posiT
print((posiT.sum())/(testP.sum()))
