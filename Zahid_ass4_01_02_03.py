#Q.1
import numpy as np
import matplotlib.pyplot as plt
import time
def uniform(t):
    if (0.0<t<1.0):
        return 1.0
    else:
        return 0.0
start = time.time()
a = 16664525
c = 1013904223
m = 2545134135
x = 0.0

n = 10000
results = []
for i in range(n):
    x  = (a*x + c)%m
    results.append(x/m)
theo_dist =[]
for  i in range(n):
    theo_dist.append(uniform(results[i]))
    
    
end1 = time.time() - start
plt.plot(results, theo_dist,"r.",label="theory")                     
plt.hist(results, density  ="True",histtype = "bar",ec='black',label="By linear congruential")
plt.legend()
plt.title("Q.1")
plt.show()    
##############################################################
#Q.2
start = time.time()
x = np.random.random(10000)
end = time.time() - start

plt.plot(results, theo_dist,"r.",label="theory")
plt.hist(x,  density  ="True",ec = "black",label="By numpy")
plt.legend()
plt.title("Q.2")
plt.show()
#################################################################
#Q.3
print("Time required using numpy random number generator(Q.3)=" ,end)
print("Time required using linear congruential random number generator(Q.3)  =", end1)
