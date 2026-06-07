from math import sqrt

def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x,y,tolerance=1e-15):
    return abs(y - x) < tolerance

""" 
以下是计算黄金分割率 的实现 
"""

def golden_update(guess):
    return 1 + 1 / guess

def golden_close(guess):
    return approx_eq(guess * guess,guess + 1)

phi = sqrt(5) / 2 + 1 / 2

def golden_test():
    approx_phi = improve(golden_update,golden_close)
    assert approx_eq(approx_phi,phi),'phi differs from its qpproximation'

""" 
以下是计算函数平方根  的实现 
"""

def newton_update(f,df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f,df):
    def zero_close(x):
        return approx_eq(f(x),0)
    return improve(newton_update(f,df),zero_close)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f,df)

"""
n次方扩展 求跟 
"""
def nth_root(a,n):
    def f(x):
        return pow(x,n) - a
    def df(x):
        return n * pow(x,n - 1)
    return find_zero(f,df)


