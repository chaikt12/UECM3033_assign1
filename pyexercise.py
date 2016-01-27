import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(x)*sy.sin(x), (x,0,np.pi))
    return ans

def my_solution():
    A = np.array( [[1,2,3,4,5,6,7,8,9,10], [2,3,4,5,6,7,8,9,10,11],[11,12,13,14,15,16,17,18,19,20],[8,-7,-6,5,-4,-3,2,-1,-9,-10],[7,6,13,4,2,15,-8,-5,12,13],[3,-4,5,-6,6,6,-4,8,-8,1],[4,-4,2,-8,4,5,6,5,12,-11],[-7,4,3,5,6,7,3,2,3,-4],[7,4,7,8,-7,5,3,-5,-2,4],[2,4,-6,-6,9,2,8,3,9,12]] )
    b = np.array([385,440,935,-217,316,26,100,126,66,306])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1300929
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())