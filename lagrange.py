from scipy import integrate
import math

def f(x):
    return math.exp(- x ** 2)

v, err = integrate.quad(f, 0, 1)
print(v)

sum += np.sqrt((y[i] - S(x[i]))**2)