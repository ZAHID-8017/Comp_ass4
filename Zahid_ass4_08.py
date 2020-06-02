from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scsp
N=100000
n = int(input("give the dimension of the sphere=", ))

d = np.random.uniform(-1,1,N)


x = np.zeros((n,N))

i = 0
while(i<n):
        m = d
        shuffle(m)
        x[i:i+1] = m
        i = i+1
x1 = np.square(x)


k = 0
for i in range(N):
        e = np.sum(x1[:,i])
        if (e<1):
                k = k +1
        


V_numerical = (2**n/N)*k
V_analytical=np.pi**(n/2)/scsp.gamma(1+n/2)
error = abs(V_numerical - V_analytical)

print("numerical value of volume of", n,"dim spher=", V_numerical)

print("analytical value of volume of", n,"dim spher=", V_analytical)
        
print("Error=", error)










