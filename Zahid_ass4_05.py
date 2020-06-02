import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x1 = np.random.rand(10000)
x2 = np.random.rand(10000)
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.hist(x1,range=(0.0,1.0), ec="black",density  =True,label = "uniform")
plt.title("PDF for x1")
plt.legend()
plt.show()

plt.hist(x1,range=(0.0,1.0),ec="black", density  =True, label = "uniform")
plt.title("PDF for x2")
plt.legend()
plt.show()
bin = 100
plt.hist(y1 ,bin,range=(-4.0,4.0),ec="black", density  =True,label="Box-Muller method")

mean = 0
standard_deviation = 1
x_values = np.arange(-5, 5, 0.1)
y_values = norm(mean, standard_deviation)
plt.plot(x_values, y_values.pdf(x_values),label="Gaussian PDF")
plt.title("PDF for y1")
plt.legend()
plt.show()
bin = 100
plt.hist(y2 ,bin,range=(-4.0,4.0),ec="black", density  =True,label="Box-Muller method")
mean = 0
standard_deviation = 1
x_values = np.arange(-5, 5, 0.1)
y_values = norm(mean, standard_deviation)
plt.plot(x_values, y_values.pdf(x_values),label="Gaussian PDF")
plt.title("PDF for y2")
plt.legend()
plt.show()



        
    































