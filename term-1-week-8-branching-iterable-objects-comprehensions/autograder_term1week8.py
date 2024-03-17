import numpy.testing as npt
import time
from numpy import allclose
from itertools import islice
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
        assert(_globals['alist'] == [36, 18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1])
    except:
        print('Incorrect values!')
    else:
        print('Correct values!')
        score += 1
    try:
        assert(all([isinstance(n,int) for n in _globals['alist']]))
    except:
        print('The values are not all integers!')
        score *= 0
    else:
        print('The values are all integers!')
        score *= 1
    #return score 
    if score > 0:
        print('Question 1a passed!')
        return score
    else: 
        raise AssertionError('Test failed!!')
def question1b(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(_globals['alist'] == [36, 18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    except:
        print('Incorrect values!')
    else:
        print('Correct values!')
        score += 1
    try:
        assert(all([isinstance(n,int) for n in _globals['alist']]))
    except:
        print('The values are not all integers!')
        score *= 0
    else:
        print('The values are all integers!')
        score *= 1
    #return score 
    if score > 0:
        print('Question 1b passed!')
        return score
    else: 
        raise AssertionError('Test failed!!')
def question1c(_globals):
    score = 0
    score0 = 0
    score1 = 0
    number_of_tests = 1
    try:
        assert(_globals['factor_sum'] == 60)
    except:
        print('Question 1c failed! (Wrong value of the factor sum)')
        pass
    else:
        print('Correct value of the factor sum!')
        score0 += 1
    try:
        assert(_globals['r'] < 6)
    except:
        print('Question 1c failed! (Too many iterations)')
        pass
    else:
        print('Good number of iterations!')
        score1 += 1
    score = score0 * score1    
    if score > 0:
        print('Question 1c passed!')
        return score
    else: 
        raise AssertionError('Test failed!!') 
        
def factor_sum_fn(a):
    from math import sqrt
    sqrta = int(sqrt(a))
    factor_sum = 0
    for r in range(1,sqrta+1):
        if a%r == 0:
            factor_sum += r + a//r
    if sqrta**2 == a:
        factor_sum -= sqrta
    return factor_sum

def question1d(_globals):
    score = 0
    score1 = 0
    score2 = 0
    number_of_tests = 1
    correct_a = factor_sum_fn(_globals['a'])
    try:
        assert(_globals['factor_sum'] == correct_a)
    except:
        print('Question 1d failed! (Wrong value of the factor sum)')
        print('Given: {}'.format(_globals['factor_sum']))
        print('Correct: {}'.format(correct_a))
        pass
    else:
        print('Correct value of the factor sum!')
        score1 += 1
    try:
        assert(_globals['r'] < 8)
    except:
        print('Question 1d failed! (Too many iterations)')
        pass
    else:
        print('Good number of iterations!')
        score2 += 1
    #return score
    score = score1 * score2    
    if score > 0:
        print('Question 1d passed!')
        if _globals['a'] != 36:
            print('Remember to set a = 36 before submitting')
        return score
    else: 
        raise AssertionError('Test failed!!')  

def question2i(_globals):
    score = 0
    number_of_tests = 4
    try:
        assert(_globals['q2ia_answer'] == [84, 104, 101, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110, 32, 102, 111, 120, 32, 106, 117, 109, 112, 115, 32, 111, 118, 101, 114, 32, 116, 104, 101, 32, 108, 97, 122, 121, 32, 100, 111, 103])
    except:
        print('Question 2(i)a failed!')
        pass
    else:
        print('Question 2(i)a passed!')
        score += 1
        
    try:
        assert(allclose(_globals['q2ib_answer'],[9.16515138991168, 10.198039027185569, 10.04987562112089, 5.656854249492381, 10.63014581273465, 10.816653826391969, 10.246950765959598, 9.9498743710662, 10.344080432788601, 5.656854249492381, 9.899494936611665, 10.677078252031311, 10.535653752852738, 10.908712114635714, 10.488088481701515, 5.656854249492381, 10.099504938362077, 10.535653752852738, 10.954451150103322, 5.656854249492381, 10.295630140987, 10.816653826391969, 10.44030650891055, 10.583005244258363, 10.723805294763608, 5.656854249492381, 10.535653752852738, 10.862780491200215, 10.04987562112089, 10.677078252031311, 5.656854249492381, 10.770329614269007, 10.198039027185569, 10.04987562112089, 5.656854249492381, 10.392304845413264, 9.848857801796104, 11.045361017187261, 11.0, 5.656854249492381, 10.0, 10.535653752852738, 10.14889156509222]))
    except:
        print('Question 2(i)b failed!')
        pass
    else:
        print('Question 2(i)b passed!')
        score += 1
        
    try:
        assert(allclose(_globals['q2ic_answer'],[(84, 9.16515138991168), (104, 10.198039027185569), (101, 10.04987562112089), (32, 5.656854249492381), (113, 10.63014581273465), (117, 10.816653826391969), (105, 10.246950765959598), (99, 9.9498743710662), (107, 10.344080432788601), (32, 5.656854249492381), (98, 9.899494936611665), (114, 10.677078252031311), (111, 10.535653752852738), (119, 10.908712114635714), (110, 10.488088481701515), (32, 5.656854249492381), (102, 10.099504938362077), (111, 10.535653752852738), (120, 10.954451150103322), (32, 5.656854249492381), (106, 10.295630140987), (117, 10.816653826391969), (109, 10.44030650891055), (112, 10.583005244258363), (115, 10.723805294763608), (32, 5.656854249492381), (111, 10.535653752852738), (118, 10.862780491200215), (101, 10.04987562112089), (114, 10.677078252031311), (32, 5.656854249492381), (116, 10.770329614269007), (104, 10.198039027185569), (101, 10.04987562112089), (32, 5.656854249492381), (108, 10.392304845413264), (97, 9.848857801796104), (122, 11.045361017187261), (121, 11.0), (32, 5.656854249492381), (100, 10.0), (111, 10.535653752852738), (103, 10.14889156509222)]))
    except:
        print('Question 2(i)c failed!')
        pass
    else:
        print('Question 2(i)c passed!')
        score += 1
        
    try:
        assert(allclose(_globals['q2id_answer'],[(84, 9.16515138991168), (104, 10.198039027185569), (101, 10.04987562112089), (32, 5.656854249492381), (113, 10.63014581273465), (117, 10.816653826391969), (105, 10.246950765959598), (99, 9.9498743710662), (107, 10.344080432788601), (32, 5.656854249492381), (98, 9.899494936611665), (114, 10.677078252031311), (111, 10.535653752852738), (119, 10.908712114635714), (110, 10.488088481701515), (32, 5.656854249492381), (102, 10.099504938362077), (111, 10.535653752852738), (120, 10.954451150103322), (32, 5.656854249492381), (106, 10.295630140987), (117, 10.816653826391969), (109, 10.44030650891055), (112, 10.583005244258363), (115, 10.723805294763608), (32, 5.656854249492381), (111, 10.535653752852738), (118, 10.862780491200215), (101, 10.04987562112089), (114, 10.677078252031311), (32, 5.656854249492381), (116, 10.770329614269007), (104, 10.198039027185569), (101, 10.04987562112089), (32, 5.656854249492381), (108, 10.392304845413264), (97, 9.848857801796104), (122, 11.045361017187261), (121, 11.0), (32, 5.656854249492381), (100, 10.0), (111, 10.535653752852738), (103, 10.14889156509222)]))
    except:
        print('Question 2(i)d failed!')
        pass
    else:
        print('Question 2(i)d passed!')
        score += 1
 
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
def question2ii(_globals):
    score = 0
    number_of_tests = 3
    try:
        assert(_globals['q2iia_answer'] == [('a', True), ('b', True), ('c', True), ('d', True), ('e', False), ('f', False), ('g', True), ('h', True), ('i', True), ('j', False), ('k', True), ('l', True), ('m', True), ('n', True), ('o', True), ('p', True), ('q', False), ('r', True), ('s', True), ('t', True), ('u', True), ('v', False), ('w', True), ('x', False), ('y', True), ('z', False)])
    except:
        print('Question 2(ii)a failed!')
        pass
    else:
        print('Question 2(ii)a passed!')
        score += 1
        
    try:
        assert(_globals['q2iib_answer'] == [1, 2, 4, 8, 16, 32, 64, 33, 66, 37, 74, 53, 11, 22, 44, 88, 81, 67, 39, 78, 61, 27, 54, 13, 26, 52, 9, 18, 36, 72, 49, 3, 6, 12, 24, 48, 1, 2, 4, 8, 16, 32, 64, 33, 66, 37, 74, 53, 11, 22, 44, 88, 81, 67, 39, 78, 61, 27, 54, 13, 26, 52, 9, 18, 36, 72, 49, 3, 6, 12, 24, 48, 1, 2, 4, 8, 16, 32, 64, 33, 66, 37, 74, 53, 11, 22, 44, 88, 81, 67, 39, 78, 61, 27, 54])
    except:
        print('Question 2(ii)b failed!')
        pass
    else:
        print('Question 2(ii)b passed!')
        score += 1
        
    try:
        assert(_globals['q2iic_answer'] == [(0, False), (1, True), (2, True), (3, True), (4, True), (5, False), (6, True), (7, False), (8, True), (9, True), (10, False), (11, True), (12, True), (13, True), (14, False), (15, False), (16, True), (17, False), (18, True), (19, False), (20, False), (21, False), (22, True), (23, False), (24, True), (25, False), (26, True), (27, True), (28, False), (29, False), (30, False), (31, False), (32, True), (33, True), (34, False), (35, False), (36, True), (37, True), (38, False), (39, True), (40, False), (41, False), (42, False), (43, False), (44, True), (45, False), (46, False), (47, False), (48, True), (49, True), (50, False), (51, False), (52, True), (53, True), (54, True), (55, False), (56, False), (57, False), (58, False), (59, False), (60, False), (61, True), (62, False), (63, False), (64, True), (65, False), (66, True), (67, True), (68, False), (69, False), (70, False), (71, False), (72, True), (73, False), (74, True), (75, False), (76, False), (77, False), (78, True), (79, False), (80, False), (81, True), (82, False), (83, False), (84, False), (85, False), (86, False), (87, False), (88, True), (89, False), (90, False), (91, False), (92, False), (93, False), (94, False)])
    except:
        print('Question 2(ii)c failed!')
        pass
    else:
        print('Question 2(ii)c passed!')
        score += 1
 
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
def question3i(_globals):
    score = 0
    number_of_tests = 4
    try:
        assert(_globals['ciphertext_numbers'] == [82, 31, 37, 20, 7, 19, 11, 37, 15, 25, 37, 71, 21, 20, 10, 49, 37, 79, 7, 19, 11, 25, 37, 71, 21, 20, 10, 51])
    except:
        print('Ciphertext numbers incorrect!')
        pass
    else:
        print('Ciphertext numbers correct!')
        score += 1
        
    try:
        assert(_globals['decrypt_numbers'] == [45, 89, 0, 78, 65, 77, 69, 0, 73, 83, 0, 34, 79, 78, 68, 12, 0, 42, 65, 77, 69, 83, 0, 34, 79, 78, 68, 14])
    except:
        print('Decrypt numbers incorrect!')
        pass
    else:
        print('Decrypt numbers correct!')
        score += 1
        
    try:
        assert(_globals['decrypt'] == 'My name is Bond, James Bond.')
    except:
        print('Decrypted message string incorrect!')
        pass
    else:
        print('Decrypted message string correct!')
        score += 1
        
    try:
        assert(_globals['d'] > 0)
    except:
        print('Your d should be positive!')
        pass
    else:
        print('Your d is in the correct range!')
        score += 1
 
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!') 
def question3iia(_globals):
    score = 0
    number_of_tests = 3
    try:
        assert(_globals['plaintext_numbers'] == [39, 79, 79, 68, 0, 69, 86, 69, 78, 73, 78, 71, 12, 0, 45, 82, 0, 34, 79, 78, 68, 12, 0, 41, 7, 86, 69, 0, 66, 69, 69, 78, 0, 69, 88, 80, 69, 67, 84, 73, 78, 71, 0, 89, 79, 85, 14])
    except:
        print('Plaintext numbers incorrect!')
        pass
    else:
        print('Plaintext numbers correct!')
        score += 1
        
    try:
        assert(_globals['ciphertext_numbers'] == [18, 73, 73, 46, 0, 83, 47, 83, 36, 41, 36, 62, 64, 0, 50, 89, 0, 23, 73, 36, 46, 64, 0, 92, 69, 47, 83, 0, 67, 83, 83, 36, 0, 83, 26, 15, 83, 9, 68, 41, 36, 62, 0, 63, 73, 10, 43])
    except:
        print('Ciphertext numbers incorrect!')
        pass
    else:
        print('Ciphertext numbers correct!')
        score += 1
        
    try:
        assert(_globals['ciphertext'] == '2iiN sOsDID^` Ry 7iDN` |eOs cssD s:/s)dID^ _i*K')
    except:
        print('Ciphertext incorrect!')
        pass
    else:
        print('Ciphertext correct!')
        score += 1
   
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')

def question3iibcd(_globals):
    score = 0
    number_of_tests = 5
    try:
        assert(_globals['residue_tuples'] == [(0, 0), (1, 37), (2, 74), (3, 16), (4, 53), (5, 90), (6, 32), (7, 69), (8, 11), (9, 48), (10, 85), (11, 27), (12, 64), (13, 6), (14, 43), (15, 80), (16, 22), (17, 59), (18, 1), (19, 38), (20, 75), (21, 17), (22, 54), (23, 91), (24, 33), (25, 70), (26, 12), (27, 49), (28, 86), (29, 28), (30, 65), (31, 7), (32, 44), (33, 81), (34, 23), (35, 60), (36, 2), (37, 39), (38, 76), (39, 18), (40, 55), (41, 92), (42, 34), (43, 71), (44, 13), (45, 50), (46, 87), (47, 29), (48, 66), (49, 8), (50, 45), (51, 82), (52, 24), (53, 61), (54, 3), (55, 40), (56, 77), (57, 19), (58, 56), (59, 93), (60, 35), (61, 72), (62, 14), (63, 51), (64, 88), (65, 30), (66, 67), (67, 9), (68, 46), (69, 83), (70, 25), (71, 62), (72, 4), (73, 41), (74, 78), (75, 20), (76, 57), (77, 94), (78, 36), (79, 73), (80, 15), (81, 52), (82, 89), (83, 31), (84, 68), (85, 10), (86, 47), (87, 84), (88, 26), (89, 63), (90, 5), (91, 42), (92, 79), (93, 21), (94, 58)])
    except:
        print('Residue tuples incorrect!')
        pass
    else:
        print('Residue tuples correct!')
        score += 1
        
    try:
        assert(_globals['d'] == 18)
    except:
        print('Decryption key d incorrect!')
        pass
    else:
        print('Decryption key d correct!')
        score += 1
        
    try:
        assert(_globals['ciphertext_numbers'] == [18, 73, 73, 46, 0, 83, 47, 83, 36, 41, 36, 62, 64, 0, 50, 89, 0, 23, 73, 36, 46, 64, 0, 92, 69, 47, 83, 0, 67, 83, 83, 36, 0, 83, 26, 15, 83, 9, 68, 41, 36, 62, 0, 63, 73, 10, 43])
    except:
        print('Ciphertext numbers incorrect!')
        pass
    else:
        print('Ciphertext numbers correct!')
        score += 1
        
    try:
        assert(_globals['decrypt_numbers'] == [39, 79, 79, 68, 0, 69, 86, 69, 78, 73, 78, 71, 12, 0, 45, 82, 0, 34, 79, 78, 68, 12, 0, 41, 7, 86, 69, 0, 66, 69, 69, 78, 0, 69, 88, 80, 69, 67, 84, 73, 78, 71, 0, 89, 79, 85, 14])
    except:
        print('Decrypt numbers incorrect!')
        pass
    else:
        print('Decrypt numbers correct!')
        score += 1
        
    try:
        assert(_globals['decrypt'] == "Good evening, Mr Bond, I've been expecting you.")
    except:
        print('Decrypted message incorrect!')
        pass
    else:
        print('Decrypted message correct!')
        score += 1
   
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')

def question3e():
    return 3

def question3iii(_globals):
    score = 0
    number_of_tests = 3
    try:
        assert(_globals['ciphertext'] == '8.dka MaJtK#K, scake# #.t stKJJed[')
    except:
        print('Ciphertext incorrect!')
        pass
    else:
        print('Ciphertext correct!')
        score += 1
        
    try:
        assert(_globals['d'] == 61)
    except:
        print('Decryption key d incorrect!')
        pass
    else:
        print('Decryption key d correct!')
        score += 1
                
    try:
        assert(_globals['decrypt'] == 'Vodka Martini, shaken not stirred.')
    except:
        print('Decrypted message incorrect!')
        pass
    else:
        print('Decrypted message correct!')
        score += 1
   
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')

def question4a(_globals):
    score = 0
    score0 = 0
    score1 = 0
    number_of_tests = 4
    try:
        assert(list(_globals['myrange']) == [97, 98, 99, 100, 101, 102])
    except:
        print('myrange contains the wrong values!')
        pass
    else:
        print('myrange contains the right values!')
        score0 += 1
    try:
        assert(isinstance(_globals['myrange'],range))
    except:
        print("myrange doesn't seem to be a range object; can you fix this?\n")
        pass
    else:
        print('myrange is a range object!\n')
        score1 += 1    
    score += score0 * score1  
    
    score0 = 0
    score1 = 0
    try:
        assert(_globals['mylist'] == [97, 98, 99, 100, 101, 102])
    except:
        print('mylist contains the wrong values!')
        pass
    else:
        print('mylist contains the right values!')
        score0 += 1
    try:
        assert(isinstance(_globals['mylist'],list))
    except:
        print("mylist doesn't seem to be a list; can you fix this?\n")
        pass
    else:
        print('mylist is a list!\n')
        score1 += 1    
    score += score0 * score1  
    
    score0 = 0
    score1 = 0
    try:
        assert(_globals['mytuple'] == (97, 98, 99, 100, 101, 102))
    except:
        print('mytuple contains the wrong values!')
        pass
    else:
        print('mytuple contains the right values!')
        score0 += 1
    try:
        assert(isinstance(_globals['mytuple'],tuple))
    except:
        print("mytuple doesn't seem to be a tuple; can you fix this?\n")
        pass
    else:
        print('mytuple is a tuple!\n')
        score1 += 1    
    score += score0 * score1 
    
    score0 = 0
    score1 = 0
    try:
        assert(list(_globals['myslice']) == [97, 98, 99, 100, 101, 102])
    except:
        print('myslice contains the wrong values!')
        pass
    else:
        print('myslice contains the right values!')
        score0 += 1
    try:
        assert(isinstance(_globals['myslice'],islice))
    except:
        print("myslice doesn't seem to be an islice object; can you fix this?\n")
        pass
    else:
        print('myslice is an islice object!\n')
        score1 += 1    
    score += score0 * score1 
   
    print(f'{score} out of {number_of_tests} tests passed')
    
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!!') 
def question4b():
    return 2
def question4c():
    return {4}
def question5a(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(_globals['ints'] == list(range(2,401)))
    except:
        print('Question 5a failed!')
        pass
    else:
        print('Question 5a passed!')
        score += 1
def question5b():
    return 4
def question5c(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(_globals['ints'] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397])
    except:
        print('Question 5c failed!')
        pass
    else:
        print('Question 5c passed!')
        score += 1
def question5d(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(_globals['q5d_answer'] == 'prime' or _globals['q5d_answer'] == 'primes')
    except:
        print('Question 5d failed!')
        pass
    else:
        print('Question 5d passed!')
        score += 1
        

        

def question6(n1, n2):
    score = 0
    number_of_tests = 2
    try:
        assert(n1 == (20, 9))
    except:
        print("Value for n1 is incorrect!")
    else:
        print("Value for n1 is correct!!")
        score += 1
    try:
        assert(n2 == (179, 871))
    except:
        print("Value for n2 is incorrect!")
    else:
        print("Value for n2 is correct!!")
        score += 1
    
    print(f'{score} out of {number_of_tests} tests passed')
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!') 
        
def question6_timed(_globals):
    start      = time.time()
    x          = _globals['longest_sequence'](1000000)
    time_limit = 15
    try:
        assert((525, 837799) == x)
    except:
        raise AssertionError("Solution is incorrect!")
    if abs(time.time() - start) < time_limit:    
        print('All Tests Passed!!!')
        return 2
    else:
        raise AssertionError('Program Too Slow!!!')
