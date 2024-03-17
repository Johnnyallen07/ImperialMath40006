import numpy.testing as npt
from time import time
import numpy as np
from plotchecker import LinePlotChecker
import csv
usernamefile = open('usernames.csv', 'r')
usernames = list(csv.reader(usernamefile))[0]
usernamefile.close()
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")
def fn1(data, already_sorted):
    global cc
    next_item = data[already_sorted]
    insertion_index = already_sorted-1
    cc += 1
    while next_item < data[insertion_index] and insertion_index > -1:
        cc += 1
        insertion_index -= 1    
    if insertion_index == -1:
        cc -= 1
    data[insertion_index+2:already_sorted+1] = \
    data[insertion_index+1:already_sorted]
    data[insertion_index+1] = next_item
def fn2(data):
    for already_sorted in range(1,len(data)):
        fn1(data, already_sorted)
def fn3(left_buffer, right_buffer, data):
    global cc
    left_index = right_index = main_index = 0
    while left_index < len(left_buffer) and right_index < len(right_buffer):
        cc += 1
        if left_buffer[left_index] < right_buffer[right_index]:
            data[main_index] = left_buffer[left_index]
            left_index += 1
        else:
            data[main_index] = right_buffer[right_index]
            right_index += 1
        main_index += 1
    if left_index < len(left_buffer):
        data[main_index:] = left_buffer[left_index:]
    else:
        data[main_index:] = right_buffer[right_index:]
def fn4(data):
    ndata = len(data)
    if ndata > 1:
        half_length = ndata//2
        left_half = data[0:half_length]
        right_half = data[half_length:ndata]
        fn4(left_half)
        fn4(right_half)
        fn3(left_half,right_half,data)
def reg1(x, y):
    n = len(x)
    return (n*np.dot(x, y) - sum(x)*sum(y))/(n*np.dot(x,x)-sum(x)**2)
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
def question1ia(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == _globals['masterList'])
    except:
        print("data does not consist of the correct list")
    else:
        print("data consists of the correct list")
        score += 1
    try:
        assert(not (_globals['data'] is _globals['masterList']))
    except:
        print("data seems to be the same object as masterList; did you use the copy function?")
    else:
        print("data is a separate object from masterList, which is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ic(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] == 120)
    except:
        print("comparison_count is not correct")
    else:
        print("comparison_count is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1id():   
    return 1

def question1ie(_globals):
    number_of_tests = 2
    score = 0
    score00, score01 = 0, 0
    score10, score11 = 0, 0
    try:
        assert([_globals['bubble_sort_simple_max'](n) for n in range(1,21)] == [n*(n-1)//2 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_max seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_simple_max seems to return the correct numbers")
        score00 += 1
    try:
        assert([isinstance(_globals['bubble_sort_simple_max'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_max seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_simple_max seems to return ints")
        score01 += 1
    score += score00*score01
    try:
        assert([_globals['bubble_sort_simple_min'](n) for n in range(1,21)] == [n*(n-1)//2 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_min seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_simple_min seems to return the correct numbers")
        score10 += 1
    try:
        assert([isinstance(_globals['bubble_sort_simple_min'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_simple_min seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_simple_min seems to return ints")
        score11 += 1
    score += score10*score11
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1if():   
    return 1

def question1iia(_globals):
    number_of_tests = 3
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['bubble_sort_enhanced'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("bubble_sort_enhanced does not seem to sort lists correctly")
    else:
        print("bubble_sort_enhanced seems to sort lists correctly")
        score += 1
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['bubble_sort_enhanced'](test_data)
        assert(_globals['comparison_count'] < 190)
    except:
        print("Your function seems to be requiring too many comparisons; is the tracking of orderedness working?")
    else:
        if _globals['comparison_count'] == 187:
            print("Your function requires exactly the same number of comparisons as ours")
        elif _globals['comparison_count'] > 187:
            print("Your function seems to require slightly more comparisons than ours; can it be further improved?")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    try:
        assert(len(_globals['bubble_sort_enhanced'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iib(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] <= 120)
    except:
        print("Your function seems to be requiring too many comparisons; is the tracking of orderedness working?")
    else:
        if _globals['comparison_count'] == 120:
            print("Your function requires exactly the same number of comparisons as ours")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iic():   
    return 3

def question1iid(_globals):
    number_of_tests = 2
    score = 0
    score00, score01 = 0, 0
    score10, score11 = 0, 0
    try:
        assert([_globals['bubble_sort_enhanced_max'](n) for n in range(1,21)] == [n*(n-1)//2 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_max seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_enhanced_max seems to return the correct numbers")
        score00 += 1
    try:
        assert([isinstance(_globals['bubble_sort_enhanced_max'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_max seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_enhanced_max seems to return ints")
        score01 += 1
    score += score00*score01
    try:
        assert([_globals['bubble_sort_enhanced_min'](n) for n in range(1,21)] == [n-1 for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_min seems not to return the correct numbers")
    else:
        print("The lambda-expression bubble_sort_enhanced_min seems to return the correct numbers")
        score10 += 1
    try:
        assert([isinstance(_globals['bubble_sort_enhanced_min'](n), int) for n in range(1,21)])
    except:
        print("The lambda-expression bubble_sort_enhanced_min seems not to return ints")
    else:
        print("The lambda-expression bubble_sort_enhanced_min seems to return ints")
        score11 += 1
    score += score10*score11
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1iie():   
    return 2
        
def question2a(_globals):
    number_of_tests = 2
    score = 0
    try:
        test_data = [5, 12, 13, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['insertion_pass'](test_data, 3)
        assert(test_data == [5, 8, 12, 13, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18])
    except:
        print("insertion_pass does not seem to be working correctly")
    else:
        print("insertion_pass seems be working correctly")
        score += 1
    try:
        assert(len(_globals['insertion_pass'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2b(_globals):
    number_of_tests = 2
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['insertion_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("insertion_sort does not seem to sort lists correctly")
    else:
        print("insertion_sort seems to sort lists correctly")
        score += 1
    try:
        assert(len(_globals['insertion_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2c(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2d():   
    return 120

def question2e(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['insertion_sort_length16_worstcase']
        fn2(data)
        assert(cc == 120)
    except:
        print("We think this is incorrect, and that it doesn't require the maximum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'worst case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
    
def question2f():   
    return 15

def question2g(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['insertion_sort_length16_bestcase']
        fn2(data)
        assert(cc == 15)
    except:
        print("We think this is incorrect, and that it requires more than the minimum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'best case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2hfunc(_globals):
    number_of_tests = 3
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['insertion_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("insertion_sort does not seem to sort lists correctly")
    else:
        print("insertion_sort seems to sort lists correctly")
        score += 1
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['insertion_sort'](test_data)
        assert(_globals['comparison_count'] < 190)
    except:
        print("Your function seems to be requiring too many comparisons")
    else:
        if _globals['comparison_count'] == 118:
            print("Your function requires exactly the same number of comparisons as ours")
        elif _globals['comparison_count'] > 118:
            print("Your function seems to require slightly more comparisons than ours; can it be further improved?")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    try:
        assert(len(_globals['insertion_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2htest(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] < 120)
    except:
        print("Your function seems to be requiring too many comparisons")
    else:
        if _globals['comparison_count'] == 83:
            print("Your function requires exactly the same number of comparisons as ours")
        elif _globals['comparison_count'] > 83:
            print("Your function seems to require slightly more comparisons than ours; can it be further improved?")
        else:
            print("Your function seems to require fewer comparisons than ours; very well done if so! It's worth double-checking that you're counting them all, though.")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2j():   
    return 4

def question3ia(_globals):
    number_of_tests = 2
    score = 0
    try:
        left_buffer = [2,5,9,12]
        right_buffer = [1,4,7,8]
        data = [0,0,0,0,0,0,0,0]
        _globals['merge'](left_buffer,right_buffer,data)
        assert(data == [1,2,4,5,7,8,9,12])
    except:
        print("merge does not seem to be working correctly")
    else:
        print("merge seems to be working correctly")
        score += 1
    try:
        assert(len(_globals['merge'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3ib():
    return 8

def question3ic():   
    return 15

def question3iia(_globals):
    number_of_tests = 2
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['merge_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("merge_sort does not seem to sort lists correctly")
    else:
        print("merge_sort seems to sort lists correctly")
        score += 1
    try:
        assert(len(_globals['merge_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3iib():   
    return 32

def question3iic():   
    return 49

def question3iid(_globals):
    number_of_tests = 1
    score = 0
    score0, score1 = 0, 0
    try:
        assert([_globals['merge_sort_min'](m) for m in range(1,5)] == [m*2**(m-1) for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_min seems not to return the correct numbers")
    else:
        print("The lambda-expression merge_sort_min seems to return the correct numbers")
        score0 += 1
    try:
        assert([isinstance(_globals['merge_sort_min'](m), int) for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_min seems not to return ints")
    else:
        print("The lambda-expression merge_sort_min seems to return ints")
        score1 += 1
    score += score0*score1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question3iie(_globals):
    number_of_tests = 1
    score = 0
    score0, score1 = 0, 0
    try:
        assert([_globals['merge_sort_max'](m) for m in range(1,5)] == [(m-1)*2**m+1 for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_max seems not to return the correct numbers")
    else:
        print("The lambda-expression merge_sort_max seems to return the correct numbers")
        score0 += 1
    try:
        assert([isinstance(_globals['merge_sort_max'](m), int) for m in range(1,5)])
    except:
        print("The lambda-expression merge_sort_max seems not to return ints")
    else:
        print("The lambda-expression merge_sort_max seems to return ints")
        score1 += 1
    score += score0*score1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iif():   
    return 2

def question3iiiafunc(_globals):
    number_of_tests = 3
    score = 0
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['merge_sort'](test_data)
        assert(test_data == list(range(1,21)))
    except:
        print("merge_sort does not seem to sort lists correctly")
    else:
        print("merge_sort seems to sort lists correctly")
        score += 1
    try:
        test_data = [12, 13, 5, 8, 19, 20, 6, 15, 10, 3, 4, 14, 11, 17, 1, 16, 9, 2, 7, 18]
        _globals['comparison_count'] = 0
        _globals['merge_sort'](test_data)
        assert(_globals['comparison_count'] == 66)
    except:
        print("Your comparison count is different from ours; can you check?")
    else:
        print("Your function requires exactly the same number of comparisons as ours")
        score += 1
    try:
        assert(len(_globals['merge_sort'].__doc__)>0)
    except:
        print("Your function does not seem to have a docstring")
    else:
        print("Your function seems to have a docstring")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iiiatest(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['data'] == [3, 5, 7, 12, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 34, 40])
    except:
        print("data has not been sorted correctly")
    else:
        print("data has been sorted correctly")
        score += 1
    try:
        assert(_globals['comparison_count'] == 47)
    except:
        print("Your comparison count is different from ours; can you check?")
    else:
        print("Your function requires exactly the same number of comparisons as ours")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iiib(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['merge_sort_length16_bestcase']
        fn4(data)
        assert(cc == 32)
    except:
        print("We think this is incorrect, and that it requires more than the minimum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'best case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')      
        
def question3iiic(_globals):
    number_of_tests = 1
    score = 0
    global cc
    try:
        cc = 0
        data = _globals['merge_sort_length16_worstcase']
        fn4(data)
        assert(cc == 49)
    except:
        print("We think this is incorrect, and that it requires more than the minimum number of comparisons; can you check again?")
    else:
        print("We agree: this seems to be a good 'worst case'")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!') 
        
def question4a(_globals):
    number_of_tests = 4
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        y_student = [_globals['pyTriple0_bigO'](n) for n in range(100, 1000)]
    except:
        print('Your definition of pyTriple0_bigO does not appear to work as a lambda-expression.')
        works = False
        score0 = 0
    else:
        print('Your definition of pyTriple0_bigO works as a lambda-expression.')
        works = True
        score0 = 1
    try:
        assert(abs(reg1(np.log(np.array(range(100, 1000))),np.log(y_student))-3.0) < 0.2)
    except:
        if works:
            print('Your definition of pyTriple0_bigO does not seem to give the right big O dependence.')
        score0 = 0
        rightdep = False
    else:
        print('Your definition of pyTriple0_bigO gives broadly the right big O dependence.')
        rightdep = True
        
    try:
        assert(y_student == [n**3 for n in range(100, 1000)])
    except:
        if works and rightdep:
            print('However, the convention is to give the big O dependence in as simple a form as possible, and you don\'t seem to have done that.')
        score0 = 0
    else:
        print('You have given the big O dependence in as simple a form as possible; well done.')
    print(f'Score for pyTriple0_bigO: {score0}\n')
    try:
        y_student = [_globals['pyTriple1_bigO'](n) for n in range(100, 1000)]
    except:
        print('Your definition of pyTriple1_bigO does not appear to work as a lambda-expression.')
        works = False
        score1 = 0
    else:
        print('Your definition of pyTriple1_bigO works as a lambda-expression.')
        works = True
        score1 = 1
    try:
        assert(abs(reg1(np.log(np.array(range(100, 1000))),np.log(y_student))-2.0) < 0.2)
    except:
        if works:
            print('Your definition of pyTriple1_bigO does not seem to give the right big O dependence.')
        score1 = 0
        rightdep = False
    else:
        print('Your definition of pyTriple1_bigO gives broadly the right big O dependence.')
        rightdep = True
    try:
        assert(y_student == [n**2 for n in range(100, 1000)])
    except:
        if works and rightdep:
            print('However, the convention is to give the big O dependence in as simple a form as possible, and you don\'t seem to have done that.')
        score1 = 0
    else:
        print('You have given the big O dependence in as simple a form as possible; well done.')
    print(f'Score for pyTriple1_bigO: {score1}\n')
    try:
        y_student = [_globals['pyTriple2_bigO'](n) for n in range(100, 1000)]
    except:
        print('Your definition of pyTriple2_bigO does not appear to work as a lambda-expression.')
        works = False
        score2 = 0
    else:
        print('Your definition of pyTriple2_bigO works as a lambda-expression.')
        works = True
        score2 = 1
    try:
        assert(abs(reg1(np.log(np.array(range(100, 1000))),np.log(y_student))-2.0) < 0.2)
    except:
        if works:
            print('Your definition of pyTriple2_bigO does not seem to give the right big O dependence.')
        rightdep = False
        score2 = 0
    else:
        print('Your definition of pyTriple2_bigO gives broadly the right big O dependence.')
        rightdep = True
    try:
        assert(y_student == [n**2 for n in range(100, 1000)])
    except:
        if works and rightdep:
            print('However, the convention is to give the big O dependence in as simple a form as possible, and you don\'t seem to have done that.')
        score2 = 0
    else:
        print('You have given the big O dependence in as simple a form as possible; well done.')    
    print(f'Score for pyTriple2_bigO: {score2}\n')
    try:
        y_student = [_globals['pyTriple3_bigO'](n) for n in range(100, 1000)]
    except:
        print('Your definition of pyTriple3_bigO does not appear to work as a lambda-expression.')
        works = False
        score3 = 0
    else:
        print('Your definition of pyTriple3_bigO works as a lambda-expression.')
        works = True
        score3 = 1
    try:
        assert(abs(reg1(np.log(np.array(range(100, 1000))),np.log(y_student))-1.0) < 0.2)
    except:
        if works:
            print('Your definition of pyTriple3_bigO does not seem to give the right big O dependence.')
        score3 = 0
        rightdep = False
    else:
        print('Your definition of pyTriple3_bigO gives broadly the right big O dependence.')
        rightdep = True
    try:
        assert(y_student == [n for n in range(100, 1000)])
    except:
        if works and rightdep:
            print('However, the convention is to give the big O dependence in as simple a form as possible, and you don\'t seem to have done that.')
        score3 = 0
    else:
        print('You have given the big O dependence in as simple a form as possible; well done.')   
    print(f'Score for pyTriple3_bigO: {score3}\n')
    score = score0 + score1 + score2 + score3
    if score > 0:
        print(f'{score} out of {number_of_tests}')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4b(_globals):
    score = 0
    try:
        assert(abs(reg1(np.log(_globals['n_values0']),np.log(_globals['iteration_counts0']))-3.0)<0.2)
    except:
        print('Something\'s wrong; your iteration count does not seem to exhibit the right kind of big O dependence on n.')
        score = 0
    else:
        print('Your iteration count exhibits the right kind of big O dependence on n.')
        score = 1
    try:
        assert(_globals['n_values0'] == [14, 16, 18, 20, 22, 26, 28, 32, 34, 38, 42, 44, 46, 50, 52, 54, 58, 62, 64, 66, 68, 74, 76, 78, 82, 86, 88, 92, 94, 98, 100, 102])
    except:
        print('We don\'t agree with your value of n_values0; for us, the values of n that give no Pythagorean triple are\n[14, 16, 18, 20, 22, 26, 28, 32, 34, 38, 42, 44, 46, 50, 52, 54, 58, 62, 64, 66, 68, 74, 76, 78, 82, 86, 88, 92, 94, 98, 100, 102]')
        score = 0
    else:
        print('We had the same n values; well done.')
    try:
        assert(_globals['iteration_counts0'] == [1728, 2744, 4096, 5832, 8000, 13824, 17576, 27000, 32768, 46656, 64000, 74088, 85184, 110592, 125000, 140608, 175616, 216000, 238328, 262144, 287496, 373248, 405224, 438976, 512000, 592704, 636056, 729000, 778688, 884736, 941192, 1000000])
    except:
        print('We don\'t agree with your value of iteration_counts0; we get\n[1728, 2744, 4096, 5832, 8000, 13824, 17576, 27000, 32768, 46656, 64000, 74088, 85184, 110592, 125000, 140608, 175616, 216000, 238328, 262144, 287496, 373248, 405224, 438976, 512000, 592704, 636056, 729000, 778688, 884736, 941192, 1000000]')
        score = 0
    else:
        print('We had the same iteration counts; well done.')
    if score > 0:
        print('\nTest passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question4c(_globals):    
    pc = LinePlotChecker(_globals["ax"])
    try: 
        assert(np.allclose(pc.x_data[0],np.array([2.63905733, 2.77258872, 2.89037176, 2.99573227, 3.09104245, 
                                                  3.25809654, 3.33220451, 3.4657359 , 3.52636052, 3.63758616, 
                                                  3.73766962, 3.78418963, 3.8286414 , 3.91202301, 3.95124372, 
                                                  3.98898405, 4.06044301, 4.12713439, 4.15888308, 4.18965474, 
                                                  4.21950771, 4.30406509, 4.33073334, 4.35670883, 4.40671925, 
                                                  4.4543473 , 4.47733681, 4.52178858, 4.54329478, 4.58496748,
                                                  4.60517019, 4.62497281])))
    except:
        print('We don\'t have the same data on the horizontal axis; please recheck.')
        score = 0
    else:
        print('Data correct on the horizontal axis.')
        score = 1
    try:
        assert(len(pc.y_data[1])>0)
    except:
        print('You don\'t seem to have superimposed a plot to illustrate the big-O dependence.')
        plotthere = False
        score = 0
    else:
        print('You have superimposed a plot to illustrate the big-O dependence.')
        plotthere = True
    try:
        assert(abs(reg1(pc.x_data[1],pc.y_data[1])-3.0)<0.2)
    except:
        if plotthere:
            print('However, this plot doesn\'t seem to illustrate the correct dependence.');
        score = 0
    else:
        print('This superimposed plot illustrates the correct dependence.')
    if score > 0:
        print('\nTest passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question4e_1(_globals):
    number_of_tests = 2
    score0 = 0
    try:
        assert(abs(reg1(np.log(_globals['n_values1']),np.log(_globals['iteration_counts1']))-2.0)<0.2)
    except:
        print('Something\'s wrong; your iteration count does not seem to exhibit the right kind of big O dependence on n.')
        score0 = 0
    else:
        print('Your iteration count exhibits the right kind of big O dependence on n.')
        score0 = 1
    try:
        assert(_globals['n_values1'] == [102, 122, 142, 162, 202, 222, 242, 262, 282, 302, 322, 342, 362, 382, 402, 422, 482, 502, 522, 542, 562, 582, 602, 622, 642, 662, 682, 722, 742, 762, 802, 822, 842, 862, 902, 922, 942, 962, 982, 1002])
    except:
        print('We don\'t agree with your value of n_values1; for us, the values of n that give no Pythagorean triple are\n[102, 122, 142, 162, 202, 222, 242, 262, 282, 302, 322, 342, 362, 382, 402, 422, 482, 502, 522, 542, 562, 582, 602, 622, 642, 662, 682, 722, 742, 762, 802, 822, 842, 862, 902, 922, 942, 962, 982, 1002]')
        score0 = 0
    else:
        print('We had the same n values; well done.')
    try:
        assert(_globals['iteration_counts1'] == [1395, 2072, 2882, 3825, 6112, 7455, 8932, 10542, 12285, 14162, 16172, 18315, 20592, 23002, 25545, 28222, 37052, 40262, 43605, 47082, 50692, 54435, 58312, 62322, 66465, 70742, 75152, 84372, 89182, 94125, 104412, 109755, 115232, 120842, 132462, 138472, 144615, 150892, 157302, 163845])
    except:
        print('We don\'t agree with your value of iteration_counts1; we get\n[1395, 2072, 2882, 3825, 6112, 7455, 8932, 10542, 12285, 14162, 16172, 18315, 20592, 23002, 25545, 28222, 37052, 40262, 43605, 47082, 50692, 54435, 58312, 62322, 66465, 70742, 75152, 84372, 89182, 94125, 104412, 109755, 115232, 120842, 132462, 138472, 144615, 150892, 157302, 163845]')
        score0 = 0
    else:
        print('We had the same iteration counts; well done.')
    print(f'Score for n values and iteration counts: {score0}\n')
    pc = LinePlotChecker(_globals["ax"])
    try: 
        assert(np.allclose(pc.x_data[0],np.array([4.62497281, 4.80402104, 4.95582706, 5.08759634, 5.3082677 ,
       5.40267738, 5.48893773, 5.5683445 , 5.64190707, 5.71042702,
       5.77455155, 5.83481074, 5.89164421, 5.94542061, 5.99645209,
       6.04500531, 6.17794411, 6.21860012, 6.25766759, 6.295266  ,
       6.33150185, 6.36647045, 6.40025745, 6.43294009, 6.4645883 ,
       6.49526556, 6.52502966, 6.58202514, 6.60934924, 6.63594656,
       6.68710861, 6.7117404 , 6.73578001, 6.75925527, 6.80461452,
       6.82654522, 6.84800527, 6.86901445, 6.88959131, 6.90975328])))
    except:
        print('We don\'t have the same data on the horizontal axis; please recheck.')
        score1 = 0
    else:
        print('Data correct on the horizontal axis.')
        score1 = 1
    try:
        assert(len(pc.y_data[1])>0)
    except:
        print('You don\'t seem to have superimposed a plot to illustrate the big-O dependence.')
        plotthere = False
        score1 = 0
    else:
        print('You have superimposed a plot to illustrate the big-O dependence.')
        plotthere = True
    try:
        assert(abs(reg1(pc.x_data[1],pc.y_data[1])-2.0)<0.2)
    except:
        if plotthere:
            print('However, this plot doesn\'t seem to illustrate the correct dependence.');
        score1 = 0
    else:
        print('This superimposed plot illustrates the correct dependence.') 
    print(f'Score for plot: {score1}\n')
    score = score0 + score1
    if score > 0:
        print(f'{score} out of {number_of_tests}')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question4e_2(_globals):
    number_of_tests = 2
    score0 = 0
    try:
        assert(abs(reg1(np.log(_globals['n_values2']),np.log(_globals['iteration_counts2']))-2.0)<0.2)
    except:
        print('Something\'s wrong; your iteration count does not seem to exhibit the right kind of big O dependence on n.')
        score0 = 0
    else:
        print('Your iteration count exhibits the right kind of big O dependence on n.')
        score0 = 1
    try:
        assert(_globals['n_values2'] == [102, 122, 142, 162, 202, 222, 242, 262, 282, 302, 322, 342, 362, 382, 402, 422, 482, 502, 522, 542, 562, 582, 602, 622, 642, 662, 682, 722, 742, 762, 802, 822, 842, 862, 902, 922, 942, 962, 982, 1002])
    except:
        print('We don\'t agree with your value of n_values2; for us, the values of n that give no Pythagorean triple are\n[102, 122, 142, 162, 202, 222, 242, 262, 282, 302, 322, 342, 362, 382, 402, 422, 482, 502, 522, 542, 562, 582, 602, 622, 642, 662, 682, 722, 742, 762, 802, 822, 842, 862, 902, 922, 942, 962, 982, 1002]')
        score0 = 0
    else:
        print('We had the same n values; well done.')
    try:
        assert(_globals['iteration_counts2'] == [255, 346, 493, 620, 969, 1146, 1324, 1592, 1812, 2037, 2357, 2624, 2887, 3284, 3592, 3900, 5052, 5544, 5945, 6341, 6914, 7348, 7791, 8402, 8891, 9375, 10048, 11100, 11841, 12416, 13777, 14387, 14995, 15844, 17151, 18066, 18776, 19463, 20423, 21163])
    except:
        print('We don\'t agree with your value of iteration_counts2; we get\n[255, 346, 493, 620, 969, 1146, 1324, 1592, 1812, 2037, 2357, 2624, 2887, 3284, 3592, 3900, 5052, 5544, 5945, 6341, 6914, 7348, 7791, 8402, 8891, 9375, 10048, 11100, 11841, 12416, 13777, 14387, 14995, 15844, 17151, 18066, 18776, 19463, 20423, 21163]')
        score0 = 0
    else:
        print('We had the same iteration counts; well done.')
    print(f'Score for n values and iteration counts: {score0}\n')
    pc = LinePlotChecker(_globals["ax"])
    try: 
        assert(np.allclose(pc.x_data[0],np.array([4.62497281, 4.80402104, 4.95582706, 5.08759634, 5.3082677 ,
       5.40267738, 5.48893773, 5.5683445 , 5.64190707, 5.71042702,
       5.77455155, 5.83481074, 5.89164421, 5.94542061, 5.99645209,
       6.04500531, 6.17794411, 6.21860012, 6.25766759, 6.295266  ,
       6.33150185, 6.36647045, 6.40025745, 6.43294009, 6.4645883 ,
       6.49526556, 6.52502966, 6.58202514, 6.60934924, 6.63594656,
       6.68710861, 6.7117404 , 6.73578001, 6.75925527, 6.80461452,
       6.82654522, 6.84800527, 6.86901445, 6.88959131, 6.90975328])))
    except:
        print('We don\'t have the same data on the horizontal axis; please recheck.')
        score1 = 0
    else:
        print('Data correct on the horizontal axis.')
        score1 = 1
    try:
        assert(len(pc.y_data[1])>0)
    except:
        print('You don\'t seem to have superimposed a plot to illustrate the big-O dependence.')
        plotthere = False
        score1 = 0
    else:
        print('You have superimposed a plot to illustrate the big-O dependence.')
        plotthere = True
    try:
        assert(abs(reg1(pc.x_data[1],pc.y_data[1])-2.0)<0.2)
    except:
        if plotthere:
            print('However, this plot doesn\'t seem to illustrate the correct dependence.');
        score1 = 0
    else:
        print('This superimposed plot illustrates the correct dependence.') 
    print(f'Score for plot: {score1}\n')
    score = score0 + score1
    if score > 0:
        print(f'{score} out of {number_of_tests}')
        return score
    else: 
        raise AssertionError('Test failed overall!')


def question4e_1(_globals):
    number_of_tests = 2
    score0 = 0
    try:
        assert(abs(reg1(np.log(_globals['n_values1']),np.log(_globals['iteration_counts1']))-2.0)<0.2)
    except:
        print('Something\'s wrong; your iteration count does not seem to exhibit the right kind of big O dependence on n.')
        score0 = 0
    else:
        print('Your iteration count exhibits the right kind of big O dependence on n.')
        score0 = 1
    try:
        assert(_globals['n_values1'] == [102, 122, 142, 162, 202, 222, 242, 262, 282, 302, 322, 342, 362, 382, 402, 422, 482, 502, 522, 542, 562, 582, 602, 622, 642, 662, 682, 722, 742, 762, 802, 822, 842, 862, 902, 922, 942, 962, 982, 1002])
    except:
        print('We don\'t agree with your value of n_values1; for us, the values of n that give no Pythagorean triple are\n[102, 122, 142, 162, 202, 222, 242, 262, 282, 302, 322, 342, 362, 382, 402, 422, 482, 502, 522, 542, 562, 582, 602, 622, 642, 662, 682, 722, 742, 762, 802, 822, 842, 862, 902, 922, 942, 962, 982, 1002]')
        score0 = 0
    else:
        print('We had the same n values; well done.')
    try:
        assert(_globals['iteration_counts1'] == [1395, 2072, 2882, 3825, 6112, 7455, 8932, 10542, 12285, 14162, 16172, 18315, 20592, 23002, 25545, 28222, 37052, 40262, 43605, 47082, 50692, 54435, 58312, 62322, 66465, 70742, 75152, 84372, 89182, 94125, 104412, 109755, 115232, 120842, 132462, 138472, 144615, 150892, 157302, 163845])
    except:
        print('We don\'t agree with your value of iteration_counts1; we get\n[1395, 2072, 2882, 3825, 6112, 7455, 8932, 10542, 12285, 14162, 16172, 18315, 20592, 23002, 25545, 28222, 37052, 40262, 43605, 47082, 50692, 54435, 58312, 62322, 66465, 70742, 75152, 84372, 89182, 94125, 104412, 109755, 115232, 120842, 132462, 138472, 144615, 150892, 157302, 163845]')
        score0 = 0
    else:
        print('We had the same iteration counts; well done.')
    print(f'Score for n values and iteration counts: {score0}\n')
    pc = LinePlotChecker(_globals["ax"])
    try: 
        assert(np.allclose(pc.x_data[0],np.array([4.62497281, 4.80402104, 4.95582706, 5.08759634, 5.3082677 ,
       5.40267738, 5.48893773, 5.5683445 , 5.64190707, 5.71042702,
       5.77455155, 5.83481074, 5.89164421, 5.94542061, 5.99645209,
       6.04500531, 6.17794411, 6.21860012, 6.25766759, 6.295266  ,
       6.33150185, 6.36647045, 6.40025745, 6.43294009, 6.4645883 ,
       6.49526556, 6.52502966, 6.58202514, 6.60934924, 6.63594656,
       6.68710861, 6.7117404 , 6.73578001, 6.75925527, 6.80461452,
       6.82654522, 6.84800527, 6.86901445, 6.88959131, 6.90975328])))
    except:
        print('We don\'t have the same data on the horizontal axis; please recheck.')
        score1 = 0
    else:
        print('Data correct on the horizontal axis.')
        score1 = 1
    try:
        assert(len(pc.y_data[1])>0)
    except:
        print('You don\'t seem to have superimposed a plot to illustrate the big-O dependence.')
        plotthere = False
        score1 = 0
    else:
        print('You have superimposed a plot to illustrate the big-O dependence.')
        plotthere = True
    try:
        assert(abs(reg1(pc.x_data[1],pc.y_data[1])-2.0)<0.2)
    except:
        if plotthere:
            print('However, this plot doesn\'t seem to illustrate the correct dependence.');
        score1 = 0
    else:
        print('This superimposed plot illustrates the correct dependence.') 
    print(f'Score for plot: {score1}\n')
    score = score0 + score1
    if score > 0:
        print(f'{score} out of {number_of_tests}')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question4e_3(_globals):
    number_of_tests = 2
    score0 = 0
    try:
        assert(abs(reg1(np.log(_globals['n_values3']),np.log(_globals['iteration_counts3']))-1.0)<0.2)
    except:
        print('Something\'s wrong; your iteration count does not seem to exhibit the right kind of big O dependence on n.')
        score0 = 0
    else:
        print('Your iteration count exhibits the right kind of big O dependence on n.')
        score0 = 1
    try:
        assert(_globals['n_values3'] == [1002, 1202, 1402, 1602, 1802, 2202, 2402, 2602, 2802, 3002, 3202, 3602, 3802, 4202, 4402, 4802, 5602, 5802, 6002, 6202, 6402, 6602, 6802, 7002, 7202, 7402, 7602, 8002, 8202, 8402, 8802, 9002, 9202, 9402, 9602, 9802, 10002])
    except:
        print('We don\'t agree with your value of n_values3; for us, the values of n that give no Pythagorean triple are\n[1002, 1202, 1402, 1602, 1802, 2202, 2402, 2602, 2802, 3002, 3202, 3602, 3802, 4202, 4402, 4802, 5602, 5802, 6002, 6202, 6402, 6602, 6802, 7002, 7202, 7402, 7602, 8002, 8202, 8402, 8802, 9002, 9202, 9402, 9602, 9802, 10002]')
        score0 = 0
    else:
        print('We had the same n values; well done.')
    try:
        assert(_globals['iteration_counts3'] == [166, 199, 233, 266, 299, 366, 399, 433, 466, 499, 533, 599, 633, 699, 733, 799, 933, 966, 999, 1033, 1066, 1099, 1133, 1166, 1199, 1233, 1266, 1333, 1366, 1399, 1466, 1499, 1533, 1566, 1599, 1633, 1666])
    except:
        print('We don\'t agree with your value of iteration_counts3; we get\n[166, 199, 233, 266, 299, 366, 399, 433, 466, 499, 533, 599, 633, 699, 733, 799, 933, 966, 999, 1033, 1066, 1099, 1133, 1166, 1199, 1233, 1266, 1333, 1366, 1399, 1466, 1499, 1533, 1566, 1599, 1633, 1666]')
        score0 = 0
    else:
        print('We had the same iteration counts; well done.')
    print(f'Score for n values and iteration counts: {score0}\n')
    pc = LinePlotChecker(_globals["ax"])
    try: 
        assert(np.allclose(pc.x_data[0],np.array([6.90975328, 7.09174212, 7.24565507, 7.37900813, 7.49665244,
       7.69712132, 7.784057  , 7.86403566, 7.93808873, 8.00703401,
       8.07153089, 8.18924453, 8.24328252, 8.34331588, 8.38981426,
       8.47678778, 8.63087896, 8.66595796, 8.69984803, 8.7326271 ,
       8.76436572, 8.79512791, 8.82497197, 8.8539511 , 8.88211404,
       8.90950551, 8.93616665, 8.98744679, 9.01213331, 9.03622505,
       9.08273425, 9.10520205, 9.12717613, 9.14867771, 9.16972669,
       9.19034173, 9.21054035])))
    except:
        print('We don\'t have the same data on the horizontal axis; please recheck.')
        score1 = 0
    else:
        print('Data correct on the horizontal axis.')
        score1 = 1
    try:
        assert(len(pc.y_data[1])>0)
    except:
        print('You don\'t seem to have superimposed a plot to illustrate the big-O dependence.')
        plotthere = False
        score1 = 0
    else:
        print('You have superimposed a plot to illustrate the big-O dependence.')
        plotthere = True
    try:
        assert(abs(reg1(pc.x_data[1],pc.y_data[1])-1.0)<0.2)
    except:
        if plotthere:
            print('However, this plot doesn\'t seem to illustrate the correct dependence.');
        score1 = 0
    else:
        print('This superimposed plot illustrates the correct dependence.') 
    print(f'Score for plot: {score1}\n')
    score = score0 + score1
    if score > 0:
        print(f'{score} out of {number_of_tests}')
        return score
    else: 
        raise AssertionError('Test failed overall!')