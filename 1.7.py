>>> import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from math import sin

def f(x):
    return 5*cos(10*x)
    return x*sin(3*x)
x = linspace(1,10,100)

f2 = np.vectorize(f) 

plt.plot(x, f2(x), 'm:', label ='5*cos(10*x)''x*sin(3x)')
plt.legend()
plt.show
