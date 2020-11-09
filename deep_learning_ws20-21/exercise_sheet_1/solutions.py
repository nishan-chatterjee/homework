# absolutely no regard for reusability apparently
# I should probably consider writing a homework parser for
# generalized use cases which can take pdf's as input and provide
# solutions for output

import numpy as np
from sympy import *
from math import e

# exercise 1.1
x = np.array([[-2], [4], [-2]])
b = np.array([[-8], [-5], [6]])
alpha = 1 / 7
y = alpha * x + b
y = np.round(y, 3)
print("Output of 1.1: ", y, "\n\n")

# exercise 1.2
x = np.array([[2], [-10], [10]])
y = np.array([[-2], [-9], [10]])
z = 0
for x_index, y_index in zip(x, y):
    z += x_index*y_index
print("Output of 1.2: ", z, "\n\n")

# exercise 1.3
a = np.array([[-9, 9], [2, -1]])
b = np.array([[-2, 5], [10, -6], [-10, 2]])
try:
    c = np.dot(a, b)
except:
    c = "none"
print("Output of 1.3: ", c, "\n\n")

# exercise 1.4
d = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
p = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
try:
    f = np.dot(d, p)
except:
    f = "none"
print("Output of 1.4: ", f, "\n\n")

# exercise 2.1
x = Symbol('x')
fx = (7*x + 6)**2
fx_prime = fx.diff(x)
print("Output of 2.1: ", fx_prime, "\n\n")

# exercise 2.2
x, y = symbols('x y', real=True)
gxy = - 2*(x**2) - 3*x - 8*y
p_gxy_prime = gxy.diff(x)
print("Output of 2.2: ", p_gxy_prime, "\n\n")

# exercise 2.3
x = Symbol('x')
hx_prime = []
hx = np.array([[(x**2)*log(x)], [-1*x]])
for row in hx:
    row_prime = []
    for column in row:
        row_prime.append(column.diff(x))
    hx_prime.append(row_prime)
print("Output of 2.3: ", hx_prime, "\n\n")

# exercise 3.1
x1 = Symbol('x1')
x2 = Symbol('x2')
x = [x1, x2]
fx = 8*x1 - 2
fx_prime = []
for index in x:
    fx_prime.append(fx.diff(index))
print("Output of 3.1: ", fx_prime, "\n\n")

# exercise 3.2
x1 = Symbol('x1')
x2 = Symbol('x2')
gx = [e**(-x1-9), (1/6)*e**(-4*x2), 4*x1*2*x2]
gx_prime = []
for index in gx:
    index_x1_prime = index.diff(x1)
    index_x2_prime = index.diff(x2)
    gx_prime.append([index_x1_prime, index_x2_prime])
print("Output of 3.2: ", gx_prime)
