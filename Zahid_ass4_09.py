import numpy as np
import random
from scipy.stats import norm
import matplotlib.pyplot as plt

def fn(t):
    if (3.0<t<7.0):
        return 1
    else:
        return 0
N = 100000
x= np.zeros(N)
x[0]=5.25
for i in range(N-1):
    theta_prime = np.random.normal(x[i],1)
    r = np.random.rand()
    if fn(theta_prime)/fn(x[i])>r:
        x[i+1] = theta_prime
    else:
        x[i+1] = x[i]
y_an = []
for i in range(N):
    y_an.append(fn(x[i])/4)
    
plt.plot(x,y_an,"r.",label = "uniform dist")        
plt.hist(x,bins=50,density=True,ec ="black",label="using Markov chain")
plt.title("Density histogram")
plt.legend()
plt.show()

