import sympy as sy
import numpy as np
import pylab as p

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(x)*sy.sin(x), (x,0,np.pi))
    return ans

def my_solution():
    A = p.randn(10,10)
    b = p.randn(10,1)
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1300929
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())