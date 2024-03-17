import numpy.testing as npt
from time import time
import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt
from plotchecker import LinePlotChecker
import csv
usernamefile = open('usernames.csv', 'r')
usernames = list(csv.reader(usernamefile))[0]
usernamefile.close()
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")


def question0(_globals):
    score = 0
    myusernamefile = open('my_username.txt', 'r')
    my_username = myusernamefile.read().strip().replace('\'','').replace('\"','')
    myusernamefile.close()
    try:
        assert(not(my_username == 'Delete this text, and insert your short form user name'))
    except:
        print('You don\'t seem to have changed the contents of the file.')
        print(f'\n0 out of 5 marks')
        return 0
    else:
        print('You\'ve changed the contents of the file; thank you!')
        score += 1
    try:
        assert(my_username in usernames)
    except:
        print('Unfortunately, your username has not been recognised; contact Phil or Sam.')
        pass
    else:
        print('Your username has been recognised; thank you!')
        score += 4
    print(f'\n{score} out of 5 marks')
    return score
def question1ia(_globals):
    number_of_tests = 1
    score = 0
    score0, score1 = 0, 0
    try:
        assert(_globals['x'] == sp.Symbol('x'))
    except:
        print("The symbol x is not defined correctly")
    else:
        print("The symbol x is defined correctly")
        score0 += 1
    try:
        assert(_globals['t'] == sp.Symbol('t'))
    except:
        print("The symbol t is not defined correctly")
    else:
        print("The symbol t is defined correctly")
        score1 += 1
    score = score0*score1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        x = sp.Symbol('x')
        assert(_globals['expr'] == (x-2)*(x+1)*(x-(2+sp.I))*(x-(2-sp.I)))
    except:
        print("The expression expr is not defined correctly")
    else:
        print("The expression expr is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ic(_globals):
    number_of_tests = 1
    score = 0
    try:
        x = sp.Symbol('x')
        assert(_globals['expr2'] == sp.expand((x-2)*(x+1)*(x-(2+sp.I))*(x-(2-sp.I))))
    except:
        print("The expression expr2 is not defined correctly")
    else:
        print("The expression expr2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1id(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['expr2_zeros'] == [-1, 2, 2 - sp.I, 2 + sp.I])
    except:
        print("The list expr2_zeros is not defined correctly")
    else:
        print("The list expr2_zeros is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ie(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['int_expr'] == sp.Rational(816,5))
    except:
        print("The Rational int_expr is not defined correctly")
    else:
        print("The Rational int_expr is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1if(_globals):
    number_of_tests = 2
    score = 0
    try:
        t = sp.Symbol('t')
        assert(_globals['f'] == sp.Function('f')(t))
    except:
        print("The symbolic function f is not defined correctly")
    else:
        print("The symbolic function f is defined correctly")
        score += 1
    try:
        t = sp.Symbol('t')
        x = sp.Symbol('x')
        f = sp.Function('f')(t)
        assert(_globals['fexpr'] == _globals['expr2'].subs(x,f))
    except:
        print("The expression fexpr is not defined correctly")
    else:
        print("The expression fexpr is defined correctly")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ig(_globals):
    number_of_tests = 1
    score = 0
    try:
        t = sp.Symbol('t')
        x = sp.Symbol('x')
        f = sp.Function('f')(t)
        assert(sp.simplify(_globals['gen_sol'].lhs - (t - sp.log(f - 2)/3 + sp.log(f + 1)/30 + 3*sp.log(f**2 - 4*f + 5)/20 + sp.atan(f - 2)/10))==0 or sp.simplify(_globals['gen_sol'].lhs + (t - sp.log(f - 2)/3 + sp.log(f + 1)/30 + 3*sp.log(f**2 - 4*f + 5)/20 + sp.atan(f - 2)/10))==0)
    except:
        print("The expression gen_sol is not defined correctly")
    else:
        print("The expression gen_sol is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2ia(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['x'] == sp.Integer(3))
    except:
        print('The value of x is incorrect\n')
    else:
        print('The value of x is correct\n')
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['x'] == (9 - 4*sp.sqrt(5))**sp.Rational(1,3) + (4*sp.sqrt(5) + 9)**sp.Rational(1,3))
    except:
        print('The value of x is incorrect\n')
    else:
        print('The value of x is correct\n')
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2ic(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['q2ic_answer'] == {4, 5} or _globals['q2ic_answer'] == {5})
    except:
        print('Either {4, 5} or just {5} has been marked correct here; the answer seems to change with version number. Let us know if your version is doing something different still.\n')
    else:
        print('Either {4, 5} or just {5} has been marked correct here; the answer seems to change with version number. Let us know if your version is doing something different still.\n')
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2id():   
    return 3

def question2ie(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['x'] == sp.Integer(3))
    except:
        print('The value of x is incorrect\n')
    else:
        print('The value of x is correct\n')
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2if():   
    return 4

def question2iia(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(_globals['pi_cf'] == [3, 7, 15, 1, 292, 1, 1, 1, 2, 1])
    except:
        print('The value of pi_cf is incorrect\n')
    else:
        print('The value of pi_cf is correct\n')
        score += 1
    try:
        assert(_globals['sqrt2_cf'] == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    except:
        print('The value of sqrt2_cf is incorrect\n')
    else:
        print('The value of sqrt2_cf is correct\n')
        score += 1
    try:
        assert(_globals['phi_cf'] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    except:
        print('The value of phi_cf is incorrect\n')
    else:
        print('The value of phi_cf is correct\n')
        score += 1
    try:
        assert(_globals['rat_cf'] == [3, 7])
    except:
        print('The value of rat_cf is incorrect\n')
    else:
        print('The value of rat_cf is correct\n')
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2iib():   
    return 2

def question2iic(_globals):
    number_of_tests = 5
    score = 0
    try:
        assert(_globals['from_continued_fraction']([3, 7, 15, 1, 292, 1, 1, 1, 2, 1]) == sp.Rational(1146408,364913))
    except:
        print('from_continued_fraction([3, 7, 15, 1, 292, 1, 1, 1, 2, 1]) gives incorrect output\n')
    else:
        print('from_continued_fraction([3, 7, 15, 1, 292, 1, 1, 1, 2, 1]) gives correct output\n')
        score += 1
    try:
        assert(_globals['from_continued_fraction']([1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == sp.Rational(3363, 2378))
    except:
        print('from_continued_fraction([1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) gives incorrect output\n')
    else:
        print('from_continued_fraction([1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) gives correct output\n')
        score += 1
    try:
        assert(_globals['from_continued_fraction']([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == sp.Rational(89, 55))
    except:
        print('from_continued_fraction([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) gives incorrect output\n')
    else:
        print('from_continued_fraction([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) gives correct output\n')
        score += 1
    try:
        assert(_globals['from_continued_fraction']([3, 7]) == sp.Rational(22, 7))
    except:
        print('from_continued_fraction([3, 7]) gives incorrect output\n')
    else:
        print('from_continued_fraction([3, 7]) gives correct output\n')
        score += 1
    try:
        assert(len(_globals['from_continued_fraction'].__doc__)>0)
    except:
        print('This function does not seem to have a docstring\n')
    else:
        print('This function seems to have a docstring\n')
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2iid(_globals):
    number_of_tests = 5
    score = 0
    try:
        assert(_globals['rational_sequence'](sp.pi,5) == [sp.Rational(3,1), sp.Rational(22,7), sp.Rational(333,106), sp.Rational(355,113), sp.Rational(103993,33102)])
    except:
        print('rational_sequence(sp.pi, 5) gives incorrect output\n')
    else:
        print('rational_sequence(sp.pi, 5) gives correct output\n')
        score += 1
    try:
        assert(_globals['rational_sequence']((1+sp.sqrt(5))/2,5) == [sp.Rational(1,1), sp.Rational(2,1), sp.Rational(3,2), sp.Rational(5,3), sp.Rational(8,5)])
    except:
        print('rational_sequence((1+sp.sqrt(5))/2,5) gives incorrect output\n')
    else:
        print('rational_sequence((1+sp.sqrt(5))/2,5) gives correct output\n')
        score += 1
    try:
        assert(_globals['rational_sequence'](sp.sqrt(2),1) == [sp.Rational(1,1)])
    except:
        print('rational_sequence(sp.sqrt(2), 1) gives incorrect output\n')
    else:
        print('rational_sequence(sp.sqrt(2), 1) gives correct output\n')
        score += 1
    try:
        assert(_globals['rational_sequence'](sp.Rational(22,7),2) == [sp.Rational(3,1),sp.Rational(22,7)])
    except:
        print('rational_sequence(sp.Rational(22,7),2) gives incorrect output\n')
    else:
        print('rational_sequence(sp.Rational(22,7),2) gives correct output\n')
        score += 1
    try:
        assert(_globals['rational_sequence'](sp.Rational(22,7),5) == [sp.Rational(3,1),sp.Rational(22,7)])
    except:
        print('rational_sequence(sp.Rational(22,7),5) gives incorrect output\n')
    else:
        print('rational_sequence(sp.Rational(22,7),5) gives correct output\n')
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2iie_plot(_globals):
    pc = LinePlotChecker(_globals["ax"])
    score = 0
    try:
        pc.assert_x_data_allclose([np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]), np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]), np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])])
    except:
        score = 0
        print('Incorrect horizontal coordinates')
    else:
        score = 1
        print('Correct horizontal coordinates')
    try:
        pc.assert_y_data_allclose([np.array([3.        , 3.14285714, 3.14150943, 3.14159292, 3.14159265,
       3.14159265, 3.14159265, 3.14159265, 3.14159265, 3.14159265]), np.array([1.        , 1.5       , 1.4       , 1.41666667, 1.4137931 ,
       1.41428571, 1.41420118, 1.41421569, 1.4142132 , 1.41421362]), np.array([1.        , 2.        , 1.5       , 1.66666667, 1.6       ,
       1.625     , 1.61538462, 1.61904762, 1.61764706, 1.61818182])])
    except:
        score = 0
        print('Incorrect vertical coordinates')
    else:
        score *= 1
        print('Correct vertical coordinates')
    if score==1:
        print('Plot correct!!')
    else:
        print('Plot incorrect!!')
    return score

def question3a(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['x'] == sp.Symbol('x',real=True))
    except:
        print("The symbol x is not defined correctly")
    else:
        print("The symbol x is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3b(_globals):
    number_of_tests = 1
    score = 0
    try:
        x = sp.Symbol('x',real=True)
        assert(_globals['y'] == x**4-8*x**3+26*x**2-40*x+21)
    except:
        print("The symbol y is not defined correctly")
    else:
        print("The symbol y is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3d(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['y_zeros'] == [1, 3])
    except:
        print("The list y_zeros is not defined correctly")
    else:
        print("The list y_zeros is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3e(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.isclose(_globals['yfunc'](2.0), -3.0))
    except:
        print("The function yfunc does not seem to work on a typical float")
    else:
        print("The function yfunc seems to work on a typical float")
        score += 1
    try:
        assert(np.allclose(_globals['yfunc'](np.linspace(-1.0,5.0,7)), np.array([96., 21.,  0., -3.,  0., 21., 96.])))
    except:
        print("The function yfunc does not seem to work on a typical array of floats")
    else:
        print("The function yfunc seems to work on a typical array of floats")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3f_plot(_globals):
    pc = LinePlotChecker(_globals["ax"])
    score = 0
    try:
        pc.assert_x_data_allclose([np.linspace(-1,5,101)])
    except:
        score = 0
        print('Incorrect horizontal coordinates')
    else:
        score = 1
        print('Correct horizontal coordinates')
    try:
        x = sp.symbols('x',real=True)
        yfunc = sp.lambdify(x, x**4-8*x**3+26*x**2-40*x+21, 'numpy')
        pc.assert_y_data_allclose([yfunc(pc.x_data[0])])
    except:
        score = 0
        print('Incorrect vertical coordinates')
    else:
        score *= 1
        print('Correct vertical coordinates')
    if score==1:
        print('Plot correct!!')
    else:
        print('Plot incorrect!!')
    return score

def question3g_plot(_globals):
    pc = LinePlotChecker(_globals["ax"])
    score = 0
    try:
        assert(
            (np.allclose(pc.x_data[0],np.linspace(-1,5,101)) and np.allclose(pc.x_data[1],np.array([1,3]))) or 
            (np.allclose(pc.x_data[1],np.linspace(-1,5,101)) and np.allclose(pc.x_data[0],np.array([1,3])))
        )
    except:
        score = 0
        print('Incorrect horizontal coordinates')
    else:
        score = 1
        print('Correct horizontal coordinates')
    try:
        x = sp.symbols('x',real=True)
        yfunc = sp.lambdify(x, x**4-8*x**3+26*x**2-40*x+21, 'numpy')        
        assert(
            np.allclose(pc.y_data[0],yfunc(pc.x_data[0])) and np.allclose(pc.y_data[1],yfunc(pc.x_data[1]))
        )
    except:
        score = 0
        print('Incorrect vertical coordinates')
    else:
        score *= 1
        print('Correct vertical coordinates')
    if score==1:
        print('Plot correct!!')
    else:
        print('Plot incorrect!!')
    return score

def question3h(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['x_stat'] == [2])
    except:
        print("The list x_stat is not correct")
    else:
        print("The list x_stat is correct")
        score += 1
    try:
        assert(_globals['y_stat'] == [-3])
    except:
        print("The list y_stat is not correct")
    else:
        print("The list y_stat is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')



def question3j_plot(_globals):
    pc = LinePlotChecker(_globals["ax"])
    score = 0
    try:
        assert(
            (np.allclose(pc.x_data[0],np.linspace(-1,5,101)) and np.allclose(pc.x_data[1],np.array([2]))) or 
            (np.allclose(pc.x_data[1],np.linspace(-1,5,101)) and np.allclose(pc.x_data[0],np.array([2])))
        )
    except:
        score = 0
        print('Incorrect horizontal coordinates')
    else:
        score = 1
        print('Correct horizontal coordinates')
    try:
        x = sp.symbols('x',real=True)
        yfunc = sp.lambdify(x, x**4-8*x**3+26*x**2-40*x+21, 'numpy')        
        assert(
            np.allclose(pc.y_data[0],yfunc(pc.x_data[0])) and np.allclose(pc.y_data[1],yfunc(pc.x_data[1]))
        )
    except:
        score = 0
        print('Incorrect vertical coordinates')
    else:
        score *= 1
        print('Correct vertical coordinates')
    if score==1:
        print('Plot correct!!')
    else:
        print('Plot incorrect!!')
    return score

def question4a(_globals):
    number_of_tests = 6
    score = 0
    x = sp.Symbol('x')
    try:
        assert(np.isclose(_globals['newton_sympy'](x-sp.cos(x), x, 1.0, 8, method='float'), 0.739085133215161))
    except:
        print('newton_sympy does not seem to work with method set to float\n')
    else:
        print('newton_sympy seems to work with method set to float\n')
        score += 1
    try:
        assert(_globals['newton_sympy'](x**2 - 2, x, 1, 5) == sp.Rational(886731088897, 627013566048))
    except:
        print('newton_sympy does not seem to work with the default method, symbolic\n')
    else:
        print('newton_sympy seems to work with the default method, symbolic\n')
        score += 1
    try:
        assert(np.isclose(_globals['newton_sympy'](x**3 -1, x, (0+2.0j), 8, method='complex'), (-0.5+0.8660254037844386j)))
    except:
        print('newton_sympy does not seem to work with method set to complex\n')
    else:
        print('newton_sympy seems to work with method set to complex\n')
        score += 1
    try:
        assert(np.allclose(_globals['newton_sympy'](x**3 -1, x, np.array([2.0,(0+2.0j),(0-2.0j)]), 8, method='lambdify') , np.array([ 1. +0.j       , -0.5+0.8660254j, -0.5-0.8660254j])))
    except:
        print('newton_sympy does not seem to work with method set to lambdify\n')
    else:
        print('newton_sympy seems to work with method set to lambdify\n')
        score += 1
    try:
        a = sp.Symbol('a')
        assert(_globals['newton_sympy'](x**2 - 2, x, a, 3, method='simplify')==(a**8 + 56*a**6 + 280*a**4 + 224*a**2 + 16)/(8*a*(a**6 + 14*a**4 + 28*a**2 + 8)))
    except:
        print('newton_sympy does not seem to work with method set to simplify\n')
    else:
        print('newton_sympy seems to work with method set to simplify\n')
        score += 1
    try:
        assert(len(_globals['newton_sympy'].__doc__)>0)
    except:
        print('This function does not seem to have a docstring\n')
    else:
        print('This function seems to have a docstring\n')
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4b(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['sqrt2_frac'] == sp.Rational(886731088897, 627013566048))
    except:
        print("sqrt2_frac is not correct")
    else:
        print("sqrt2_frac is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question4c(_globals):
    number_of_tests = 3
    score = 0
    try:
        assert(np.isclose(_globals['root0'], 1.0))
    except:
        print('root0 is incorrect\n')
    else:
        print('root0 is correct\n')
        score += 1
    try:
        assert(np.isclose(_globals['root1'], (-0.5+0.8660254037844386j)))
    except:
        print('root1 is incorrect\n')
    else:
        print('root1 is correct\n')
        score += 1
    try:
        assert(np.isclose(_globals['root2'], (-0.5-0.8660254037844386j)))
    except:
        print('root2 is incorrect\n')
    else:
        print('root2 is correct\n')
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4d(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(np.allclose(_globals['roots'],np.array([ 1. +0.j       , -0.5+0.8660254j, -0.5-0.8660254j])))
    except:
        print("roots is not correct")
    else:
        print("roots is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4e(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(np.allclose(_globals['roots'],np.array([ 1. +0.j       , -0.5+0.8660254j, -0.5-0.8660254j])))
    except:
        print("roots is not correct")
    else:
        print("roots is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def newton_sympy(expr, var, x0, niterate, *, method='symbolic'):
    """
    Solves expr == 0 using Newton's method; differentiation is symbolic
    """
    from sympy import diff, simplify, lambdify
    
    # derivative of expr wrt var
    dexpr = diff(expr, var)
    
    # expression to be iterated
    newt_expr = var - expr/dexpr
    
    # initialize
    x = x0
    
    # lambdify method
    if method == 'lambdify':
        newt_expr_func = lambdify(var, newt_expr, 'numpy')
        for n in range(niterate):
            x = newt_expr_func(x)
    
    # anything else
    else: 
        for n in range(niterate):
            x = newt_expr.subs(var,x)
            if method == 'simplify':
                x = simplify(x)
            elif method == 'float':
                x = float(x)
            elif method == 'complex':
                x = complex(x)
                
    return x

def question4f(_globals):
    number_of_tests = 3
    score = 0
    try:
        assert(
            np.allclose(_globals['x_values0'],np.linspace(-2.0, 2.0, 400)) and
            np.allclose(_globals['y_values0'],np.linspace(-2.0, 2.0, 400))
        )
    except:
        print('x_values0, y_values0 at least partly incorrect')
    else:
        print('x_values0, y_values0 correct')
        score += 1
    try:
        x0, y0 = np.meshgrid(np.linspace(-2.0, 2.0, 400), np.linspace(-2.0, 2.0, 400))
        z0 = x0 + 1j*y0
        assert(
            np.allclose(_globals['x0'],x0) and
            np.allclose(_globals['y0'],y0) and
            np.allclose(_globals['z0'],z0)
        )
    except:
        print('x0, y0, z0 at least partly incorrect')
    else:
        print('x0, y0, z0 correct')
        score += 1
    try:
        z = sp.symbols('z')
        roots = newton_sympy(z**3 - 1, z, _globals['z0'], 100, method='lambdify')
        assert(
            np.allclose(_globals['roots'],roots) 
        )
    except:
        print('roots incorrect')
    else:
        print('roots correct')
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
    