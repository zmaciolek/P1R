import sys
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y=np.sin(x)

def method_1(*args, **kwargs):
    print(args, kwargs)

method_1(1,2,3,a=5)

def plot_with_params(x,y,**params):
    plt.plot(x,y, **params)
    plt.legend()
    plt.show()

plot_with_params(x,y, label = 'yo', linestyle = 'dotted')

def method_2(a, b, *args, c=None, **kwargs):
    plt.plot(x*a+y*b, **kwargs)
    plt.legend()
    plt.show()


method_2(1,2,label="k")

