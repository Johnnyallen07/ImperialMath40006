import numpy.testing as npt
from time import time
from numpy import isclose, allclose
from math import cos, exp, sin, pi
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
def question1a(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals['Elist1'],[1.5707963267948966, 2.5207963267948967, 2.1233952617855856, 2.379401380369645, 2.2267790252052713, 2.3236228059783635, 2.264067672197098, 2.301497907757926, 2.2782673649466303, 2.292803843066782, 2.283752791950874]))
    except:
        pass
    else:
        score += 1
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
def question1b(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals['Elist2'],[1.5707963267948966, 2.0457963267948966, 2.2307103695659016, 2.2760246901225174, 2.285105692211478, 2.286835289752431, 2.2871613522757923, 2.28722270121186, 2.2872342398078462, 2.287236409852908, 2.2872368179644407]))
    except:
        pass
    else:
        score += 1
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
def question1c(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals['Elist3'],[1.5707963267948966, 2.520796326794897, 2.296623574573425, 2.287256163407903, 2.287236912575581, 2.28723691249383, 2.28723691249383, 2.28723691249383, 2.28723691249383, 2.28723691249383, 2.28723691249383]))
    except:
        pass
    else:
        score += 1
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
        
def question1d(_globals):
    score = 0
    score0, score1 = 0, 0
    score10, score11 = 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        assert(isclose(_globals['eccentric_anomaly'](pi/2, 0.95, 5),2.28723691249383))
    except:
        print('eccentric_anomaly(pi/2, 0.95, 5) returned the incorrect output')
        pass
    else:
        print('eccentric_anomaly(pi/2, 0.95, 5) returned the correct output')
        score0 += 1
    print('\nTesting: edge cases')
    try:
        assert(isclose(_globals['eccentric_anomaly'](pi/2, 0.95, 0),pi/2))
    except:
        print('eccentric_anomaly(pi/2, 0.95, 0) returned the incorrect output')
        pass
    else:
        print('eccentric_anomaly(pi/2, 0.95, 0) returned the correct output')
        score10 += 1
    try:
        assert(isclose(_globals['eccentric_anomaly'](pi/2, 0, 5),pi/2))
    except:
        print('eccentric_anomaly(pi/2, 0, 5) returned the incorrect output')
        pass
    else:
        print('eccentric_anomaly(pi/2, 0, 5) returned the correct output')
        score11 += 1
    score1 = score10*score11
    score = score0 + score1
    if score > 0:
        print('\nQuestion 1d: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question2a(_globals):
    score = 0
    score0, score1, score2 = 0, 0, 0
    score00, score01, score02, score10, score11, score12, score20, score21, score22 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    number_of_tests = 3
    print('Testing: arguments by position')
    try:
        assert(_globals['integer_digits'](6,2) == [1,1,0])
    except:
        print('integer_digits(6,2) returned the incorrect output')
        pass
    else:
        print('integer_digits(6,2) returned the correct output')
        score00 += 1
    try:
        assert(_globals['integer_digits'](347,2) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(347,2) returned the incorrect output')
        pass
    else:
        print('integer_digits(347,2) returned the correct output')
        score01 += 1
    try:
        assert(_globals['integer_digits'](347,10) == [3,4,7])
    except:
        print('integer_digits(347,10) returned the incorrect output')
        pass
    else:
        print('integer_digits(347,10) returned the correct output')
        score02 += 1
    score0 = score00*score01*score02
    print('\nTesting: arguments by keyword')
    try:
        assert(_globals['integer_digits'](number=6,base=2) == [1,1,0])
    except:
        print('integer_digits(number=6,base=2) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=6,base=2) returned the correct output')
        score10 += 1
    try:
        assert(_globals['integer_digits'](base=2,number=347) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(base=2,number=347) returned the incorrect output')
        pass
    else:
        print('integer_digits(base=2,number=347) returned the correct output')
        score11 += 1
    try:
        assert(_globals['integer_digits'](number=347,base=10) == [3,4,7])
    except:
        print('integer_digits(number=347,base=10) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=347,base=10) returned the correct output')
        score12 += 1
    score1 = score10*score11*score12
    print('\nTesting: edge cases')
    try:
        assert(_globals['integer_digits'](1,2) == [1])
    except:
        print('integer_digits(1,2) returned the incorrect output')
        pass
    else:
        print('integer_digits(1,2) returned the correct output')
        score20 += 1
    try:
        assert(_globals['integer_digits'](base=7,number=1) == [1])
    except:
        print('integer_digits(base=7,number=1) returned the incorrect output')
        pass
    else:
        print('integer_digits(base=7,number=1) returned the correct output')
        score21 += 1
    try:
        assert(_globals['integer_digits'](0,10) == [])
    except:
        print('integer_digits(0,10) returned the incorrect output')
        pass
    else:
        print('integer_digits(0,10) returned the correct output')
        score22 += 1
    score2 = score20*score21*score22
    score = score0 + score1 + score2
    if score > 0:
        print('\nQuestion 2a: {} out of 3'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')

def question2b(_globals):
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    score00, score01, score02, score10, score11, score12, score20, score21, score22, score30, score31, score32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    number_of_tests = 4
    print('Testing: arguments by position')
    try:
        assert(_globals['integer_digits'](6,2) == [1,1,0])
    except:
        print('integer_digits(6,2) returned the incorrect output')
        pass
    else:
        print('integer_digits(6,2) returned the correct output')
        score00 += 1
    try:
        assert(_globals['integer_digits'](347,2) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(347,2) returned the incorrect output')
        pass
    else:
        print('integer_digits(347,2) returned the correct output')
        score01 += 1
    try:
        assert(_globals['integer_digits'](347,10) == [3,4,7])
    except:
        print('integer_digits(347,10) returned the incorrect output')
        pass
    else:
        print('integer_digits(347,10) returned the correct output')
        score02 += 1
    score0 = score00*score01*score02
    print('\nTesting: arguments by keyword')
    try:
        assert(_globals['integer_digits'](number=6,base=2) == [1,1,0])
    except:
        print('integer_digits(number=6,base=2) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=6,base=2) returned the correct output')
        score10 += 1
    try:
        assert(_globals['integer_digits'](base=2,number=347) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(base=2,number=347) returned the incorrect output')
        pass
    else:
        print('integer_digits(base=2,number=347) returned the correct output')
        score11 += 1
    try:
        assert(_globals['integer_digits'](number=347,base=10) == [3,4,7])
    except:
        print('integer_digits(number=347,base=10) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=347,base=10) returned the correct output')
        score12 += 1
    score1 = score10*score11*score12
    print('\nTesting: edge cases')
    try:
        assert(_globals['integer_digits'](1,2) == [1])
    except:
        print('integer_digits(1,2) returned the incorrect output')
        pass
    else:
        print('integer_digits(1,2) returned the correct output')
        score20 += 1
    try:
        assert(_globals['integer_digits'](base=7,number=1) == [1])
    except:
        print('integer_digits(base=7,number=1) returned the incorrect output')
        pass
    else:
        print('integer_digits(base=7,number=1) returned the correct output')
        score21 += 1
    try:
        assert(_globals['integer_digits'](0,10) == [])
    except:
        print('integer_digits(0,10) returned the incorrect output')
        pass
    else:
        print('integer_digits(0,10) returned the correct output')
        score22 += 1
    score2 = score20*score21*score22
    print('\nTesting: default value')
    try:
        assert(_globals['integer_digits'](347) == [3,4,7])
    except:
        print('integer_digits(347) returned the incorrect output')
        pass
    else:
        print('integer_digits(347) returned the correct output')
        score30 += 1
    try:
        assert(_globals['integer_digits'](number=347) == [3,4,7])
    except:
        print('integer_digits(number=347) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=347) returned the correct output')
        score31 += 1
    try:
        assert(_globals['integer_digits'](number=0) == [])
    except:
        print('integer_digits(number=0) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=0) returned the correct output')
        score32 += 1
    score3 = score30*score31*score32
    score = score0 + score1 + score2 + score3
    if score > 0:
        print('\nQuestion 2b: {} out of 4'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question2c(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score02, score03, score04 = 0,0,0,0,0
    number_of_tests = 2
    print('Testing: these should all work')
    try:
        assert(_globals['integer_digits'](347) == [3,4,7])
    except:
        print('integer_digits(347) returned the incorrect output')
        pass
    else:
        print('integer_digits(347) returned the correct output')
        score00 += 1
    try:
        assert(_globals['integer_digits'](number=347) == [3,4,7])
    except:
        print('integer_digits(number=347) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=347) returned the correct output')
        score01 += 1
    try:
        assert(_globals['integer_digits'](347,base=2) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(347,base=2) returned the incorrect output')
        pass
    else:
        print('integer_digits(347,base=2) returned the correct output')
        score02 += 1
    try:
        assert(_globals['integer_digits'](number=347,base=2) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(number=347,base=2) returned the incorrect output')
        pass
    else:
        print('integer_digits(number=347,base=2) returned the correct output')
        score03 += 1
    try:
        assert(_globals['integer_digits'](base=2,number=347) == [1, 0, 1, 0, 1, 1, 0, 1, 1])
    except:
        print('integer_digits(base=2,number=347) returned the incorrect output')
        pass
    else:
        print('integer_digits(base=2,number=347) returned the correct output')
        score04 += 1
    score0 = score00*score01*score02
    print('\nTesting: this one should fail')
    try:
        _globals['integer_digits'](347,2)
    except:
        print('integer_digits(347,2) failed, as it should have')
        score1 += 1
    else:
        print('integer_digits(347,2) did not fail, which it should have')
        pass
    score = score0 + score1
    if score > 0:
        print('\nQuestion 2c: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')

def question3a(_globals):
    score = 0
    score0, score1 = 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        assert(_globals['hailstone_sequence'](11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    except:
        print('hailstone_sequence(11) returned the incorrect output')
        pass
    else:
        print('hailstone_sequence(11) returned the correct output')
        score0 += 1
    print('\nTesting: edge case')
    try:
        assert(_globals['hailstone_sequence'](1) == [1])
    except:
        print('hailstone_sequence(1) returned the incorrect output')
        pass
    else:
        print('hailstone_sequence(1) returned the correct output')
        score1 += 1
    score = score0 + score1
    if score > 0:
        print('\nQuestion 3a: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')

def question3b(_globals):
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    number_of_tests = 4
    print('Testing: typical case')
    try:
        assert(_globals['aliquot_chain'](282) == [282, 294, 390, 618, 630, 1242, 1638, 2730, 5334, 6954, 7926, 7938, 12753, 7267, 785, 163, 1, 0, 0])
    except:
        print('aliquot_chain(282) returned the incorrect output')
        pass
    else:
        print('aliquot_chain(282) returned the correct output')
        score0 += 1
    print('\nTesting: edge case')
    try:
        assert(_globals['aliquot_chain'](0) == [0, 0])
    except:
        print('aliquot_chain(0) returned the incorrect output')
        pass
    else:
        print('aliquot_chain(0) returned the correct output')
        score1 += 1
    print('\nTesting: perfect number')
    try:
        assert(_globals['aliquot_chain'](28) == [28, 28])
    except:
        print('aliquot_chain(28) returned the incorrect output')
        pass
    else:
        print('aliquot_chain(28) returned the correct output')
        score2 += 1
    print('\nTesting: amicable pair')
    try:
        assert(_globals['aliquot_chain'](284) == [284, 220, 284])
    except:
        print('aliquot_chain(284) returned the incorrect output')
        pass
    else:
        print('aliquot_chain(284) returned the correct output')
        score3 += 1
    score = score0 + score1 + score2 + score3
    if score > 0:
        print('\nQuestion 3b: {} out of 4'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')

def question3c(_globals):
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    number_of_tests = 4
    print('Testing: small even number')
    try:
        assert(_globals['power_of_two_divisor2'](24) == 3)
    except:
        print('power_of_two_divisor2(24) returned the incorrect output')
        pass
    else:
        print('power_of_two_divisor2(24) returned the correct output')
        score0 += 1
    print('\nTesting: small odd number')
    try:
        assert(_globals['power_of_two_divisor2'](23) == 0)
    except:
        print('power_of_two_divisor2(23) returned the incorrect output')
        pass
    else:
        print('power_of_two_divisor2(23) returned the correct output')
        score1 += 1
    print('\nTesting: large even number')
    try:
        assert(_globals['power_of_two_divisor2'](2**103*3**89) == 103)
    except:
        print('power_of_two_divisor2(2**103*3**89) returned the incorrect output')
        pass
    else:
        print('power_of_two_divisor2(2**103*3**89) returned the correct output')
        score2 += 1
    print('\nTesting: large odd number')
    try:
        assert(_globals['power_of_two_divisor2'](5**103*3**89) == 0)
    except:
        print('power_of_two_divisor2(5**103*3**89) returned the incorrect output')
        pass
    else:
        print('power_of_two_divisor2(5**103*3**89) returned the correct output')
        score3 += 1
    score = score0 + score1 + score2 + score3
    if score > 0:
        print('\nQuestion 3c: {} out of 4'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question4a(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    number_of_tests = 2
    print('Testing: typical cases')
    try:
        assert(_globals['my_factorial'](10) == 3628800)
    except:
        print('my_factorial(10) returned the incorrect output')
        pass
    else:
        print('my_factorial(10) returned the correct output')
        score00 += 1
    try:
        assert(_globals['my_factorial'](100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)
    except:
        print('my_factorial(100) returned the incorrect output')
        pass
    else:
        print('my_factorial(100) returned the correct output')
        score01 += 1
    score0 = score00 * score01
    print('\nTesting: edge cases')
    try:
        assert(_globals['my_factorial'](1) == 1)
    except:
        print('my_factorial(1) returned the incorrect output')
        pass
    else:
        print('my_factorial(1) returned the correct output')
        score10 += 1
    try:
        assert(_globals['my_factorial'](0) == 1)
    except:
        print('my_factorial(0) returned the incorrect output')
        pass
    else:
        print('my_factorial(0) returned the correct output')
        score11 += 1    
    score1 = score10 * score11
    score = score0 + score1
    if score > 0:
        print('\nQuestion 4a: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')

def question4b(_globals):
    score = 0
    score0, score1 = 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        assert(_globals['hailstone_sequence2'](11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    except:
        print('hailstone_sequence2(11) returned the incorrect output')
        pass
    else:
        print('hailstone_sequence2(11) returned the correct output')
        score0 += 1
    print('\nTesting: edge case')
    try:
        assert(_globals['hailstone_sequence2'](1) == [1])
    except:
        print('hailstone_sequence2(1) returned the incorrect output')
        pass
    else:
        print('hailstone_sequence2(1) returned the correct output')
        score1 += 1
    score = score0 + score1
    if score > 0:
        print('\nQuestion 4b: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question4_c():   
    return 2
    
def question4d(_globals):
    score = 0
    score0, score1 = 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        assert(_globals['fibonacci_recpair'](10) == (34, 55))
    except:
        print('fibonacci_recpair(10) returned the incorrect output')
        pass
    else:
        print('fibonacci_recpair(10) returned the correct output')
        score0 += 1
    print('\nTesting: edge case')
    try:
        assert(_globals['fibonacci_recpair'](2) == (1, 1))
    except:
        print('fibonacci_recpair(2) returned the incorrect output')
        pass
    else:
        print('fibonacci_recpair(2) returned the correct output')
        score1 += 1
    score = score0 + score1
    if score > 0:
        print('\nQuestion 4d: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
    
def question4e(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    number_of_tests = 2
    print('Testing: typical cases')
    try:
        assert(_globals['fibonacci3'](10) == 55)
    except:
        print('fibonacci3(10) returned the incorrect output')
        pass
    else:
        print('fibonacci3(10) returned the correct output')
        score00 += 1
    try:
        assert(_globals['fibonacci3'](35) == 9227465)
    except:
        print('fibonacci3(35) returned the incorrect output')
        pass
    else:
        print('fibonacci3(35) returned the correct output')
        score01 += 1
    score0 = score00*score01
    print('\nTesting: edge cases')
    try:
        assert(_globals['fibonacci3'](2) == 1)
    except:
        print('fibonacci3(2) returned the incorrect output')
        pass
    else:
        print('fibonacci3(2) returned the correct output')
        score10 += 1
    try:
        assert(_globals['fibonacci3'](1) == 1)
    except:
        print('fibonacci3(1) returned the incorrect output')
        pass
    else:
        print('fibonacci3(1) returned the correct output')
        score11 += 1
    score1 = score10*score11
    score = score0 + score1
    if score > 0:
        print('\nQuestion 4e: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
    
def question4f(_globals):
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0    
    score20, score21, score30, score31 = 0, 0, 0, 0
    number_of_tests = 4
    print('Testing: typical case, pair')
    try:
        assert(_globals['fibonacci4'](10,return_pair=True) == (34, 55))
    except:
        print('fibonacci4(10,return_pair=True) returned the incorrect output')
    else:
        print('fibonacci4(10,return_pair=True) returned the correct output')
        score0 += 1
    print('\nTesting: edge case,pair')
    try:
        assert(_globals['fibonacci4'](2,return_pair=True) == (1, 1))
    except:
        print('fibonacci4(2,return_pair=True) returned the incorrect output')
    else:
        print('fibonacci4(2,return_pair=True) returned the correct output')
        score1 += 1
    print('Testing: typical cases,single value')
    try:
        assert(_globals['fibonacci4'](10) == 55)
    except:
        print('fibonacci4(10) returned the incorrect output')
    else:
        print('fibonacci4(10) returned the correct output')
        score20 += 1
    try:
        assert(_globals['fibonacci4'](35) == 9227465)
    except:
        print('fibonacci4(35) returned the incorrect output')
        pass
    else:
        print('fibonacci4(35) returned the correct output')
        score21 += 1
    score2 = score20*score21
    print('\nTesting: edge cases, single value')
    try:
        assert(_globals['fibonacci4'](2) == 1)
    except:
        print('fibonacci4(2) returned the incorrect output')
        pass
    else:
        print('fibonacci4(2) returned the correct output')
        score30 += 1
    try:
        assert(_globals['fibonacci4'](1) == 1)
    except:
        print('fibonacci4(1) returned the incorrect output')
        pass
    else:
        print('fibonacci4(1) returned the correct output')
        score31 += 1
    score3 = score30*score31
    score = score0 + score1 + score2 + score3
    if score > 0:
        print('\nQuestion 4f: {} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed!!')
    
def question4g(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    number_of_tests = 2
    print('Testing: typical cases')
    try:
        assert(_globals['fibonacci2'](10) == 55)
    except:
        print('fibonacci2(10) returned the incorrect output')
        pass
    else:
        print('fibonacci2(10) returned the correct output')
        score00 += 1
    try:
        assert(_globals['fibonacci2'](35) == 9227465)
    except:
        print('fibonacci2(35) returned the incorrect output')
        pass
    else:
        print('fibonacci2(35) returned the correct output')
        score01 += 1
    score0 = score00*score01
    print('\nTesting: edge cases')
    try:
        assert(_globals['fibonacci2'](2) == 1)
    except:
        print('fibonacci2(2) returned the incorrect output')
        pass
    else:
        print('fibonacci2(2) returned the correct output')
        score10 += 1
    try:
        assert(_globals['fibonacci2'](1) == 1)
    except:
        print('fibonacci2(1) returned the incorrect output')
        pass
    else:
        print('fibonacci2(1) returned the correct output')
        score11 += 1
    score1 = score10*score11
    score = score0 + score1
    if score > 0:
        print('\nQuestion 4g: {} out of 2'.format(score))
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question4_h():   
    return 2

def question4j(_globals):
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    score00, score01, score10, score11, score20, score21, score30, score31 = 0, 0, 0, 0, 0, 0, 0, 0
    number_of_tests = 4
    print('Testing: typical case')
    try:
        assert(_globals['aliquot_chain_inner']([282,294,390]) == [282, 294, 390, 618, 630, 1242, 1638, 2730, 5334, 6954, 7926, 7938, 12753, 7267, 785, 163, 1, 0, 0])
    except:
        print('aliquot_chain_inner([282,294,390]) returned the incorrect output')
    else:
        print('aliquot_chain_inner([282,294,390]) returned the correct output')
        score00 += 1
    try:
        assert(_globals['aliquot_chain2'](282) == [282, 294, 390, 618, 630, 1242, 1638, 2730, 5334, 6954, 7926, 7938, 12753, 7267, 785, 163, 1, 0, 0])
    except:
        print('aliquot_chain2(282) returned the incorrect output')
        pass
    else:
        print('aliquot_chain2(282) returned the correct output')
        score01 += 1
    score0 = score00*score01
    print('\nTesting: edge case')
    try:
        assert(_globals['aliquot_chain_inner']([0]) == [0, 0])
    except:
        print('aliquot_chain_inner([0]) returned the incorrect output')
    else:
        print('aliquot_chain_inner([0]) returned the correct output')
        score10 += 1
    try:
        assert(_globals['aliquot_chain2'](0) == [0, 0])
    except:
        print('aliquot_chain2(0) returned the incorrect output')
        pass
    else:
        print('aliquot_chain2(0) returned the correct output')
        score11 += 1
    score1 = score10*score11
    print('\nTesting: perfect number')
    try:
        assert(_globals['aliquot_chain_inner']([28]) == [28, 28])
    except:
        print('aliquot_chain_inner([28]) returned the incorrect output')
        pass
    else:
        print('aliquot_chain_inner([28]) returned the correct output')
        score20 += 1
    try:
        assert(_globals['aliquot_chain2'](28) == [28, 28])
    except:
        print('aliquot_chain2(28) returned the incorrect output')
        pass
    else:
        print('aliquot_chain2(28) returned the correct output')
        score21 += 1
    score2 = score20*score21
    print('\nTesting: amicable pair')
    try:
        assert(_globals['aliquot_chain_inner']([284,220]) == [284, 220, 284])
    except:
        print('aliquot_chain_inner([284,220]) returned the incorrect output')
        pass
    else:
        print('aliquot_chain_inner([284,220]) returned the correct output')
        score30 += 1
    try:
        assert(_globals['aliquot_chain2'](284) == [284, 220, 284])
    except:
        print('aliquot_chain2(284) returned the incorrect output')
        pass
    else:
        print('aliquot_chain2(284) returned the correct output')
        score31 += 1
    score3 = score30*score31
    score = score0 + score1 + score2 + score3
    if score > 0:
        print('\nQuestion 4j: {} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question4k(_globals):
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    score00, score01, score10, score11, score20, score21, score30, score31 = 0, 0, 0, 0, 0, 0, 0, 0
    number_of_tests = 4
    print('Testing: typical case')
    try:
        assert(_globals['aliquot_chain3'](390,list_so_far=[282,294]) == [282, 294, 390, 618, 630, 1242, 1638, 2730, 5334, 6954, 7926, 7938, 12753, 7267, 785, 163, 1, 0, 0])
    except:
        print('aliquot_chain3(390,list_so_far=[282,294]) returned the incorrect output')
    else:
        print('aliquot_chain3(390,list_so_far=[282,294]) returned the correct output')
        score00 += 1
    try:
        assert(_globals['aliquot_chain3'](282) == [282, 294, 390, 618, 630, 1242, 1638, 2730, 5334, 6954, 7926, 7938, 12753, 7267, 785, 163, 1, 0, 0])
    except:
        print('aliquot_chain3(282) returned the incorrect output')
        pass
    else:
        print('aliquot_chain3(282) returned the correct output')
        score01 += 1
    score0 = score00*score01
    print('\nTesting: edge case')
    try:
        assert(_globals['aliquot_chain3'](0,list_so_far=[0]) == [0, 0])
    except:
        print('aliquot_chain3(0,list_so_far=[0]) returned the incorrect output')
    else:
        print('aliquot_chain3(0,list_so_far=[0]) returned the correct output')
        score10 += 1
    try:
        assert(_globals['aliquot_chain3'](0) == [0, 0])
    except:
        print('aliquot_chain3(0) returned the incorrect output')
        pass
    else:
        print('aliquot_chain3(0) returned the correct output')
        score11 += 1
    score1 = score10*score11
    print('\nTesting: perfect number')
    try:
        assert(_globals['aliquot_chain3'](28,list_so_far=[]) == [28, 28])
    except:
        print('aliquot_chain3(28,list_so_far=[]) returned the incorrect output')
        pass
    else:
        print('aliquot_chain3(28,list_so_far=[]) returned the correct output')
        score20 += 1
    try:
        assert(_globals['aliquot_chain3'](28) == [28, 28])
    except:
        print('aliquot_chain3(28) returned the incorrect output')
        pass
    else:
        print('aliquot_chain3(28) returned the correct output')
        score21 += 1
    score2 = score20*score21
    print('\nTesting: amicable pair')
    try:
        assert(_globals['aliquot_chain3'](220,list_so_far=[284]) == [284, 220, 284])
    except:
        print('aliquot_chain3(220,list_so_far=[284]) returned the incorrect output')
        pass
    else:
        print('aliquot_chain3(220,list_so_far=[284]) returned the correct output')
        score30 += 1
    try:
        assert(_globals['aliquot_chain3'](284) == [284, 220, 284])
    except:
        print('aliquot_chain3(284) returned the incorrect output')
        pass
    else:
        print('aliquot_chain3(284) returned the correct output')
        score31 += 1
    score3 = score30*score31
    score = score0 + score1 + score2 + score3
    if score > 0:
        print('\nQuestion 4k: {} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed!!')