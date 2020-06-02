import random
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scsp
from scipy.stats import chi2
Score = np.array([2,3,4,5,6,7,8,9,10,11,12])
Ys1 = np.array([4,10,10,13,20,18,18,11,13,14,13])
Ys2 = np.array([3,7,11,15,19,24,21,17,13,9,5])
nps = np.array([4,8,12,16,20,24,20,16,12,8,4])


a = Ys1 - nps
a = np.square(a)
a1 = np.zeros(len(nps))
for i in range(len(nps)):
        a1[i] = a[i]/nps[i]

print(a1)
V1 = sum(a1) #"chi-square statistic" in the first run
print("V1=",V1)


b = Ys2 - nps
b = np.square(b)
b1 = np.zeros(len(nps))
for i in range(len(nps)):
        b1[i] = b[i]/nps[i]

print(b1)
V2 = sum(b1) #"chi-square statistic" in the second run
print("V2=",V2)




def f(t):
        if (t<0.01 or t>0.99):
                return "not sufficiently random"
        elif(0.01<t<0.05 or 0.95<t<0.99):
                return "are suspect"
        elif(0.05<t<0.1 or 0.90<t<0.95):
                return "almost suspect"
        elif(0.1<t<0.9):
                return "sufficiently random"
           

                
k = len(nps)-1
#chi-square test for the first run
e1 = 1.0 - chi2.cdf(V1, k)
print("e1=",e1)

k = len(nps)-1
#chi-square test for the second run
e2 = 1.0 - chi2.cdf(V2, k)
print("e2=",e2)

print("run1 random numbers are" ,f(e1)) 
print("run2 random numbers are" ,f(e2)) 








