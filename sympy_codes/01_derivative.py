from sympy import lambdify, diff, sympify, symbols
from typing import Callable


def derivative(expr):
    x = symbols('x')
    f = lambdify(x, sympify(expr))
    f_prime = lambdify(x, diff(expr))
    return f, f_prime



expr = "x**2 - 4*x - 7"

result = derivative(expr)

func = result[0]
d_func = result[1]


print(func(2))
print(d_func(10))

