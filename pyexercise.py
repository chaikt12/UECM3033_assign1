import sympy as sy
import numpy as np 



def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(2.0*x)*sy.sin(x), (x,0,1.0))
    return ans

def my_solution():
    A = np.array( [[3,1,-10], [4,2,-9],[5,3,-8]] )
    b = np.array([-1,5,11])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1300929
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())