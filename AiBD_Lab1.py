import matplotlib.pyplot as plt
import numpy as np


def fun(x, f=lambda a: a ** 2 + 5):
    y = np.ndarray(shape=[len(x)])
    for i in range(len(x)):
        y[i] = f(x[i])
    return y

x = np.linspace(-7, 7, 10000)
plt.plot(x,fun(x),label = 'x (-1,1)')
plt.grid()
plt.xlim(-1,1)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('f=x^2+5')
plt.show()
plt.plot(x,fun(x),label = 'x (-6,6)')
plt.grid()
plt.xlim(-6,6)
plt.legend()
plt.show()
plt.plot(x,fun(x), label = 'x (-5,5)')
plt.grid()
plt.xlim(-5,5)
plt.legend()
plt.show()