import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner
import csv

def fn(a,b,c,x):
    return a*x**2+b*x+c



index=[]
x=[]
y=[]
yerr=[]

with open('data2.txt', 'r') as file:
    data=csv.reader(file, delimiter='&')
    for c in data:
        index.append(float(c[0]))
        x.append(float(c[1]))
        y.append(float(c[2]))
        yerr.append(float(c[3]))
index=np.array(index)
x=np.array(x)
y=np.array(y)
yerr=np.array(yerr)

def log_likelihood(theta, x,y,yerr):
    a,b,c = theta
    model = a*x**2+b*x+c
    sigma2 = yerr**2

    # actually negative in L
    return 0.5*np.sum((y - model)**2/sigma2 + np.log(2*np.pi*2))







def log_prior(theta):
    a,b,c = theta
    if  -500.0 < a < 500 and -500.0 < b < 500.0 and -500.0 < c <500.0:
        return 0.0
    else:
        return -np.inf

def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    else:
        return lp - log_likelihood(theta, x, y, yerr)



guess = (1.0,1.0,1.0)
soln = minimize(log_likelihood,guess,args = (x,y,yerr))



nwalkers, ndim = 50, 3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)

sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x, y, yerr))

sampler.run_mcmc(pos, 5000)



samples = sampler.get_chain()
samples2 = sampler.get_chain(flat = "True")
medians = np.median(samples2,axis = 0)
a_true,b_true,c_true = medians
labels = ["a", "b", "c"]
fig = corner.corner(samples2,labels = labels, truths = [a_true, b_true,c_true])







print("The best fit value for a is=",a_true)

print("The best fit  value for b is=",b_true)

print("The best fit value for c is=",c_true)






fig=plt.subplots(3)[0]


plt.subplot(3,1,1)
plt.plot(samples[1:200,:, 0]) # a values
plt.ylabel('a')
plt.subplot(3,1,2)
plt.plot(samples[1:200, :, 1]) # b values
plt.ylabel('b')
plt.subplot(3,1,3)
plt.plot(samples[1:200, :, 2]) # cvalues
plt.ylabel('c')
plt.show()

np.random.seed(123)

# Generate some synthetic data from the model.
x0 = np.linspace(np.amin(x),np.amax(x),100)
#print(x0)
inds = np.random.randint(len(samples2), size=100)
for ind in inds:
    sam = samples2[ind]
    plt.plot(x0, np.dot(np.vander(x0, 2), sam[:2]), "C1", alpha=0.1)

plt.errorbar(x, y, yerr=yerr, fmt=".k", capsize=0)
plt.plot(x0, fn(a_true,b_true,c_true,x0),"r.", label="Best fit plot")
plt.legend(fontsize=14)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
















    
