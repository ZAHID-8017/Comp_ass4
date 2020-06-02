import numpy as np
import matplotlib.pyplot as plt

def fn(t):
    g = np.sqrt(1/np.pi)
    return g*np.exp(-(t**2)/2)

def g(t):
    if 0.0< t <10.0:
        return 2
    else:
        return 0
       
def env(t):
    return 1.5*np.exp(-x)




x = np.random.rand(10000)*(10.0)

y = np.random.rand(10000)*2
x_good = x[y<fn(x)]
print(len(x_good))
y_good = y[y<fn(x)]
x_bad = x[y>fn(x)]
y_bad = y[y>fn(x)]
plt.figure()
plt.plot(x,y,"r.")
plt.legend()
plt.title("points uniformly distributed")

plt.figure()
plt.plot(x,fn(x),"*" ,label = "err function")
plt.legend()
plt.xlabel("x")
plt.ylabel("err(x)")

plt.figure()
plt.plot(x_bad,y_bad,"r*")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("points outside the err fns")

plt.figure()
plt.plot(x_good,y_good,"g*")
plt.legend()
plt.title("points inside the err fns")
plt.figure()
plt.plot(x,fn(x),"*")
bin = 20
plt.hist(x_good,bin, range = (0.0,10.0),density = True, ec = "black")
plt.legend()
plt.title("Histogram with rectangle as envelope")
plt.show()

#####################################################################################################################################


n=10000
x = np.random.rand(n)
x = -np.log(x)
#print(x)
y = np.random.rand(n)*env(x)
x_good = x[y<fn(x)]
print(len(x_good))
y_good = y[y<fn(x)]
x_bad = x[y>fn(x)]
y_bad = y[y>fn(x)]
plt.figure()
plt.plot(x,y,"*")
plt.title("points distribute  under exp env")
plt.legend()

plt.figure()
plt.plot(x_bad,y_bad,"r*")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("points outside the exponential env")

plt.figure()
plt.plot(x_good,y_good,"g*")
plt.legend()
plt.title("points inside the exponential env")
plt.figure()
plt.plot(x,fn(x),"*")
bin = 20
plt.hist(x_good,bin, range = (0.0,10.0),density = True, ec = "black")
plt.legend()
plt.title("Histogram with exponential as envelope")
plt.show()






