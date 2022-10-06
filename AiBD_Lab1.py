import matplotlib
import numpy as np

print('dupa')


def fun(x: np.ndarray, f=lambda a: a ** 2 + 5):
    for i in range(len(x)):
        return f(x)


x = np.linspace(-5, 5, 100)
print(x)
print(fun(x))
