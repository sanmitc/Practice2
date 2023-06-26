import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2


x = np.arange(1, 2, 0.1)
y = f(x)

x=plt.plot(x, y)
plt.show()
plt.savefig()

