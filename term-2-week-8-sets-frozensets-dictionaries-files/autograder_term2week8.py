import numpy.testing as npt
from time import time
import numpy as np
import math
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
def question1ia(_globals):
    number_of_tests = 2
    score = 0
    score00, score01, score02, score03 = 0,0,0,0
    score10, score11, score12, score13 = 0,0,0,0
    try:
        assert(list(_globals['list1']) == list(range(13,104,2)))
    except:
        print("list1 does not contain the correct data")
    else:
        print("list1 contains the correct data")
        score00 += 1
    try:
        assert(list(_globals['tuple1']) == list(range(13,104,2)))
    except:
        print("tuple1 does not contain the correct data")
    else:
        print("tuple1 contains the correct data")
        score01 += 1
    try:
        assert(set(_globals['set1']) == set(range(13,104,2)))
    except:
        print("set1 does not contain the correct data")
    else:
        print("set1 contains the correct data")
        score02 += 1
    try:
        assert(set(_globals['fs1']) == set(range(13,104,2)))
    except:
        print("fs1 does not contain the correct data")
    else:
        print("fs1 contains the correct data")
        score03 += 1
    score0 = score00 * score01 * score02 * score03
    try:
        assert(isinstance(_globals['list1'],list))
    except:
        print("\nlist1 is not a list")
    else:
        print("\nlist1 is a list")
        score10 += 1
    try:
        assert(isinstance(_globals['tuple1'],tuple))
    except:
        print("tuple1 is not a tuple")
    else:
        print("tuple1 is a tuple")
        score11 += 1
    try:
        assert(isinstance(_globals['set1'],set))
    except:
        print("set1 is not a set")
    else:
        print("set1 is a set")
        score12 += 1
    try:
        assert(isinstance(_globals['fs1'],frozenset))
    except:
        print("fs1 is not a frozenset")
    else:
        print("fs1 is a frozenset")
        score13 += 1
    score1 = score10 * score11 * score12 * score13
    score = score0+score1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ib(_globals):
    number_of_tests = 4
    score = 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    score20, score21, score30, score31 = 0, 0, 0, 0
    try:
        assert(_globals['list2'] == _globals['list1'])
    except:
        print("list2 does not contain the same elements as list1")
    else:
        print("list2 contains the same elements as list1")
        score00 += 1
    try:
        assert(_globals['list2'] is _globals['list1'])
    except:
        print("list2 is not the same object as list1, which is incorrect")
    else:
        print("list2 is the same object as list1, which is correct")
        score01 += 1
    score += score00*score01
    try:
        assert(_globals['list3'] == _globals['list1'])
    except:
        print("\nlist3 does not contain the same elements as list1")
    else:
        print("\nlist3 contains the same elements as list1")
        score10 += 1
    try:
        assert(not(_globals['list3'] is _globals['list1']))
    except:
        print("list3 is the same object as list1, which is incorrect")
    else:
        print("list3 is not the same object as list1, which is correct")
        score11 += 1
    score += score10*score11
    try:
        assert(_globals['set2'] == _globals['set1'])
    except:
        print("\nset2 does not contain the same elements as set1")
    else:
        print("\nset2 contains the same elements as set2")
        score20 += 1
    try:
        assert(_globals['set2'] is _globals['set1'])
    except:
        print("set2 is not the same object as set1, which is incorrect")
    else:
        print("set2 is the same object as set1, which is correct")
        score21 += 1
    score += score20*score21
    try:
        assert(_globals['set3'] == _globals['set1'])
    except:
        print("\nset3 does not contain the same elements as set1")
    else:
        print("\nset3 contains the same elements as set1")
        score30 += 1
    try:
        assert(not(_globals['set3'] is _globals['set1']))
    except:
        print("set3 is the same object as set1, which is incorrect")
    else:
        print("set3 is not the same object as set1, which is correct")
        score31 += 1
    score += score30*score31
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1ic(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['list1'] == [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105])
    except:
        print("list1 is not correct")
    else:
        print("list1 is correct")
        score += 1
    try:
        assert(_globals['set1'] == {13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105})
    except:
        print("set1 is not correct")
    else:
        print("set1 is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1id():   
    return 3

def question1ie(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['list1'] == [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 105])
    except:
        print("list1 is not correct")
    else:
        print("list1 is correct")
        score += 1
    try:
        assert(_globals['set1'] == {13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105})
    except:
        print("set1 is not correct")
    else:
        print("set1 is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1if():   
    return 5

def question1ig(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals['list1'] == list(range(1005,1310,5)))
    except:
        print("list1 is not correct")
    else:
        print("list1 is correct")
        score += 1
    try:
        assert(_globals['set1'] == set(range(1005,1310,5)))
    except:
        print("set1 is not correct")
    else:
        print("set1 is correct")
        score += 1
    if score > 0:
        print('{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1ih():   
    return 2

def question1iia(_globals):
    number_of_tests = 3
    score = 0
    score10, score11, score20, score21 = 0, 0, 0, 0
    try:
        assert(_globals['list_of_lists1'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("list_of_lists1 does not contain the right values")
    else:
        print("list_of_lists1 contains the right values")
        score += 1
    try:
        assert(_globals['list_of_lists2'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists2 does not contain the right values")
    else:
        print("\nlist_of_lists2 contains the right values")
        score10 += 1
    try:
        assert(_globals['list_of_lists2'] is _globals['list_of_lists1'])
    except:
        print("list_of_lists2 is not the same object as list_of_lists1, which is incorrect")
    else:
        print("list_of_lists2 is the same object as list_of_lists1, which is correct")
        score11 += 1
    score += score10*score11
    try:
        assert(_globals['list_of_lists3'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists3 does not contain the right values")
    else:
        print("\nlist_of_lists3 contains the right values")
        score20 += 1
    try:
        assert(not(_globals['list_of_lists3'] is _globals['list_of_lists1']))
    except:
        print("list_of_lists2 is the same object as list_of_lists1, which is incorrect")
    else:
        print("list_of_lists3 is not the same object as list_of_lists1, which is correct")
        score21 += 1
    score += score20*score21
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iib():   
    return 1

def question1iic(_globals):
    number_of_tests = 4
    score = 0
    score10, score11 = 0, 0  
    try:
        assert(_globals['list_of_lists1'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("list_of_lists1 does not contain the right values")
    else:
        print("list_of_lists1 contains the right values")
        score += 1
    try:
        assert(_globals['list_of_lists4'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists4 does not contain the right values")
    else:
        print("\nlist_of_lists4 contains the right values")
        score += 1
    try:
        assert(not(_globals['list_of_lists4'] is _globals['list_of_lists1']))
    except:
        print("\nlist_of_lists4 is the same object as list_of_lists1, which is incorrect")
    else:
        print("\nlist_of_lists4 is not the same object as list_of_lists1, which is correct")
        score += 1
    try:
        assert(
            not(
                (_globals['list_of_lists4'][0] is _globals['list_of_lists1'][0]) or
                (_globals['list_of_lists4'][1] is _globals['list_of_lists1'][1]) or
                (_globals['list_of_lists4'][2] is _globals['list_of_lists1'][2])
            )
        )
    except:
        print("\nlist_of_lists4 is not a deep copy: its rows are not all separate objects from those of list_of_lists1")
    else:
        print("\nlist_of_lists4 is a deep copy: its rows are separate objects from those of list_of_lists1")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iid(_globals):
    number_of_tests = 4
    score = 0
    score10, score11 = 0, 0
    try:
        assert(_globals['list_of_lists1'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("list_of_lists1 does not contain the right values")
    else:
        print("list_of_lists1 contains the right values")
        score += 1
    try:
        assert(_globals['list_of_lists5'] == [[1, 3, 5], [1, 4, 7], [1, 5, 9]])
    except:
        print("\nlist_of_lists5 does not contain the right values")
    else:
        print("\nlist_of_lists5 contains the right values")
        score += 1
    try:
        assert(not(_globals['list_of_lists5'] is _globals['list_of_lists1']))
    except:
        print("\nlist_of_lists5 is the same object as list_of_lists1, which is incorrect")
    else:
        print("\nlist_of_lists5 is not the same object as list_of_lists1, which is correct")
        score += 1
    try:
        assert(
            not(
                (_globals['list_of_lists5'][0] is _globals['list_of_lists1'][0]) or
                (_globals['list_of_lists5'][1] is _globals['list_of_lists1'][1]) or
                    (_globals['list_of_lists5'][2] is _globals['list_of_lists1'][2])
            )
        )
    except:
        print("\nlist_of_lists5 is not a deep copy: its rows are not all separate objects from those of list_of_lists1")
    else:
        print("\nlist_of_lists5 is a deep copy: its rows are separate objects from those of list_of_lists1")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question1iie():   
    return 2
        
def question2ia(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['radius_list'] == [2400000.0, 6100000.0, 6300000.0, 3400000.0, 69000000.0, 57000000.0, 25000000.0, 25000000.0])
    except:
        print("radius_list is not correct")
    else:
        print("radius_list is correct")
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
        assert(_globals['mass_set'] == {6e+24, 5.6e+26, 3.3e+23, 4.9e+24, 1.9e+27, 6.4e+23, 1e+26, 8.7e+25})
    except:
        print("mass_set is not correct")
    else:
        print("mass_set is correct")
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
        assert(_globals['name_set'] == {'mars', 'venus', 'saturn', 'uranus', 'mercury', 'neptune', 'jupiter', 'earth'})
    except:
        print("name_set is not correct")
    else:
        print("name_set is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2id(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['ev_dict'] == {'mercury': 4300.0, 'venus': 10000.0, 'earth': 11000.0, 'mars': 5000.0, 'jupiter': 60000.0, 'saturn': 36000.0, 'uranus': 22000.0, 'neptune': 24000.0})
    except:
        print("ev_dict is not correct")
    else:
        print("ev_dict is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2iia(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(isinstance(_globals['xylene_isomers'],dict))
    except:
        print("xylene_isomers seems not to be a dictionary")
    else:
        print("xylene_isomers is a dictionary")
        score += 1
    try:
        assert(list(_globals['xylene_isomers'].values()) == ['orthoxylene', 'metaxylene', 'paraxylene'])
    except:
        print("\nxylene_isomers does not have the right values")
    else:
        print("\nxylene_isomers has the right values")
        score += 1
    try:
        assert(
            isinstance(list(_globals['xylene_isomers'].keys())[0], tuple) and
            isinstance(list(_globals['xylene_isomers'].keys())[1], tuple) and
            isinstance(list(_globals['xylene_isomers'].keys())[2], tuple)
        )
    except:
        print("\nFor your keys, you don't seem to be using tuples, which we think is the best choice.")
    else:
        print("\nFor your keys, you seem to be using tuples, which we think is the best choice.")
        score += 1
    try:
        assert(
            (list(_globals['xylene_isomers'].keys())[0] == (1, 2)) and
            (list(_globals['xylene_isomers'].keys())[1] == (1, 3)) and
            (list(_globals['xylene_isomers'].keys())[2] == (1, 4))
        )
    except:
        print("\nYour keys don't seem to have the correct values.")
    else:
        print("\nYour keys have the correct values.")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2iib():   
    return {1,2,3,4,6,9}
        
def question2iic():   
    return {1,2,3,4,5,6,7,8,9,10}

def question3(_globals):
    number_of_tests = 4
    score = 0
    try:
        assert(_globals['power_set']({0, 1}) == {frozenset(), frozenset({1}), frozenset({0}), frozenset({0, 1})})
    except:
        print("power_set({0, 1}) does not return the correct value")
    else:
        print("power_set({0, 1}) returns the correct value")
        score += 1
    try:
        assert(_globals['power_set']({'a','b','c','d'}) == {frozenset({'d', 'c'}), frozenset({'b'}), frozenset({'a', 'd', 'b'}), frozenset({'a', 'b'}), frozenset({'d', 'c', 'b'}), frozenset({'d'}), frozenset({'a', 'd', 'c'}), frozenset({'d', 'b'}), frozenset({'a', 'd', 'c', 'b'}), frozenset({'c'}), frozenset(), frozenset({'a', 'c'}), frozenset({'c', 'b'}), frozenset({'a'}), frozenset({'a', 'd'}), frozenset({'a', 'c', 'b'})})
    except:
        print("power_set({'a','b','c','d'}) does not return the correct value")
    else:
        print("power_set({'a','b','c','d'}) returns the correct value")
        score += 1
    try:
        assert(_globals['power_set']({7}) == {frozenset(), frozenset({7})})
    except:
        print("power_set({7}) does not return the correct value")
    else:
        print("power_set({7}) returns the correct value")
        score += 1
    try:
        assert(_globals['power_set'](set()) == {frozenset()})
    except:
        print("power_set(set()) does not return the correct value")
    else:
        print("power_set(set()) returns the correct value")
        score += 1
    if score > 0:
        print('\n{} out of {}'.format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4a(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers_string'] == "{(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'}")
    except:
        print("xylene_isomers_string is not correct")
    else:
        print("xylene_isomers_string is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4c(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers_string2'] == "{(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'}")
    except:
        print("xylene_isomers_string2 is not correct")
    else:
        print("xylene_isomers_string2 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4d(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers2'] == {(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'})
    except:
        print("xylene_isomers2 is not correct")
    else:
        print("xylene_isomers2 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4f(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['xylene_isomers3'] == {(1, 2): 'orthoxylene', (1, 3): 'metaxylene', (1, 4): 'paraxylene'})
    except:
        print("xylene_isomers3 is not correct")
    else:
        print("xylene_isomers3 is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4g(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['new_cos'] == math.cos)
    except:
        print("new_cos is not correct")
    else:
        print("new_cos is correct")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4h(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(_globals['new_power_set']({0, 1}) == {frozenset(), frozenset({1}), frozenset({0}), frozenset({0, 1})})
    except:
        print("new_power_set({0, 1}) does not return the correct value")
    else:
        print("new_power_set({0, 1}) returns the correct value")
        score += 1
    try:
        assert(_globals['new_power_set']({'a','b','c','d'}) == {frozenset({'d', 'c'}), frozenset({'b'}), frozenset({'a', 'd', 'b'}), frozenset({'a', 'b'}), frozenset({'d', 'c', 'b'}), frozenset({'d'}), frozenset({'a', 'd', 'c'}), frozenset({'d', 'b'}), frozenset({'a', 'd', 'c', 'b'}), frozenset({'c'}), frozenset(), frozenset({'a', 'c'}), frozenset({'c', 'b'}), frozenset({'a'}), frozenset({'a', 'd'}), frozenset({'a', 'c', 'b'})})
    except:
        print("new_power_set({'a','b','c','d'}) does not return the correct value")
    else:
        print("new_power_set({'a','b','c','d'}) returns the correct value")
        score += 1
    try:
        assert(_globals['new_power_set']({7}) == {frozenset(), frozenset({7})})
    except:
        print("new_power_set({7}) does not return the correct value")
    else:
        print("new_power_set({7}) returns the correct value")
        score += 1
    try:
        assert(_globals['new_power_set'](set()) == {frozenset()})
    except:
        print("new_power_set({}) does not return the correct value")
    else:
        print("new_power_set({}) returns the correct value")
        score += 1
    if score == 4:
        print('Test passed!')
        return 1
    else: 
        raise AssertionError('Test failed overall!')
