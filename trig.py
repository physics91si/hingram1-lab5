#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt


# TODO fill in this function
def integrate(y):
    a = y * 0.01
    return np.sum(a)

    

# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y 
x = np.arange(0, np.pi, .01) 
y = np.sin(x)
plt.plot(x,y) 
plt.show()