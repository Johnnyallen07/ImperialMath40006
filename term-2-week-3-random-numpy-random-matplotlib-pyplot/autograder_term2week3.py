import numpy.testing as npt
from time import time
import numpy as np
import matplotlib.pyplot as plt
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
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["randlist10"],list))
    except:
        print("randlist10 is not a list")
    else:
        print("randlist10 is a list")
        score0 += 1
    try:
        assert(len(_globals["randlist10"]) == 10)
    except:
        print("randlist10 has incorrect length")
    else:
        print("randlist10 has correct length")
        score1 += 1
    try:
        assert(all([isinstance(x,float) for x in _globals["randlist10"]]))
    except:
        print("randlist10 does not consist of floats")
    else:
        print("randlist10 consists of floats")
        score2 += 1
    try:
        assert(all([x>=0 and x<=1 for x in _globals["randlist10"]]))
    except:
        print("The elements of randlist10 are not in the correct range")
    else:
        print("The elements of randlist10 are in the correct range")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
        
def question1b(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["randarray10"],np.ndarray))
    except:
        print("randarray10 is not a numpy array")
    else:
        print("randarray10 is a numpy array")
        score0 += 1
    try:
        assert(np.shape(_globals["randlist10"]) == (10,))
    except:
        print("randarray10 is not 1D and of length 10")
    else:
        print("randarray10 is 1D and of length 10")
        score1 += 1
    try:
        assert(all([isinstance(x,float) for x in _globals["randarray10"]]))
    except:
        print("randarray10 does not consist of floats")
    else:
        print("randarray10 consists of floats")
        score2 += 1
    try:
        assert(all([x>=0 and x<=1 for x in _globals["randarray10"]]))
    except:
        print("The elements of randarray10 are not in the correct range")
    else:
        print("The elements of randarray10 are in the correct range")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
        
def question1c(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["randarray20by10"],np.ndarray))
    except:
        print("randarray20by10 is not a numpy array")
    else:
        print("randarray20by10 is a numpy array")
        score0 += 1
    try:
        assert(np.shape(_globals["randarray20by10"]) == (20,10))
    except:
        print("randarray20by10 is not 20 by 10")
    else:
        print("randarray20by10 is 20 by 10")
        score1 += 1
    try:
        assert(all([[isinstance(x,float) for x in row] for row in _globals["randarray20by10"]]))
    except:
        print("randarray20by10 does not consist of floats")
    else:
        print("randarray20by10 consists of floats")
        score2 += 1
    try:
        assert(all([[x>=0 and x<=1 for x in row] for row in _globals["randarray20by10"]]))
    except:
        print("The elements of randarray20by10 are not in the correct range")
    else:
        print("The elements of randarray20by10 are in the correct range")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
        
def question1d(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["mean20"],np.ndarray))
    except:
        print("mean20 is not a numpy array")
    else:
        print("mean20 is a numpy array")
        score0 += 1
    try:
        assert(np.shape(_globals["mean20"]) == (20,))
    except:
        print("mean20 is not 1D and of length 20")
    else:
        print("mean20 is 1D and of length 20")
        score1 += 1
    try:
        assert(all([isinstance(x,float) for x in _globals["mean20"]]))
    except:
        print("mean20 does not consist of floats")
    else:
        print("mean20 consists of floats")
        score2 += 1
    try:
        assert(np.allclose(_globals["mean20"],np.mean(_globals["randarray20by10"],axis=1)))
    except:
        print("The elements of mean20 do not have the correct values")
    else:
        print("The elements of mean20 have the correct values")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 
        
def question1e(_globals):
    number_of_tests = 2
    score = 0
    score0, score1 = 0, 0
    score00, score01, score02, score03 = 0, 0, 0, 0
    score10, score11, score12, score13 = 0, 0, 0, 0
    print("Testing: typical case")
    try:
        assert(isinstance(_globals["rowmeans"](18,5),np.ndarray))
    except:
        print("Function does not return a numpy array")
    else:
        print("Function returns a numpy array")
        score00 += 1
    try:
        assert(np.shape(_globals["rowmeans"](18,5)) == (18,))
    except:
        print("Function output does not have the correct dimensions")
    else:
        print("Function output has the correct dimensions")
        score01 += 1
    try:
        assert(all([isinstance(x,float) for x in _globals["rowmeans"](18,5)]))
    except:
        print("Function output does not consist of floats")
    else:
        print("Function output consists of floats")
        score02 += 1
    try:
        assert(all([x>=0 and x<=1 for x in _globals["rowmeans"](18,5)]))
    except:
        print("The elements of the function output are not in the correct range")
    else:
        print("The elements of the function output are in the correct range")
        score03 += 1
    score0 = score00*score01*score02*score03
    print("\nTesting: edge case")
    try:
        assert(isinstance(_globals["rowmeans"](23,1),np.ndarray))
    except:
        print("Function does not return a numpy array")
    else:
        print("Function returns a numpy array")
        score10 += 1
    try:
        assert(np.shape(_globals["rowmeans"](23,1)) == (23,))
    except:
        print("Function output does not have the correct dimensions")
    else:
        print("Function output has the correct dimensions")
        score11 += 1
    try:
        assert(all([isinstance(x,float) for x in _globals["rowmeans"](23,1)]))
    except:
        print("Function output does not consist of floats")
    else:
        print("Function output consists of floats")
        score12 += 1
    try:
        assert(all([x>=0 and x<=1 for x in _globals["rowmeans"](23,1)]))
    except:
        print("The elements of the function output are not in the correct range")
    else:
        print("The elements of the function output are in the correct range")
        score13 += 1
    score1 = score10*score11*score12*score13
    score = score0 + score1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')         
        
def question1g():   
    return 2

def question2a(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.allclose(_globals["x_values1"], np.linspace(-1.2, 1.2, 25)))
        assert(np.allclose(_globals["y_values1"], np.linspace(-1.2, 1.2, 25)))
    except:
        print("x_values1 or y_values1 defined incorrectly")
    else:
        print("x_values1 and y_values1 defined correctly")
        score += 1    
    try:
        myx1, myy1 = np.meshgrid(np.linspace(-1.2, 1.2, 25),np.linspace(-1.2, 1.2, 25))
        assert(np.allclose(_globals["x1"], myx1))
        assert(np.allclose(_globals["y1"], myy1))
    except:
        print("x1 or y1 defined incorrectly")
    else:
        print("x1 and y1 defined correctly")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2c(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.allclose(_globals["x_values2"], np.linspace(-1.2, 1.2, 121)))
        assert(np.allclose(_globals["y_values2"], np.linspace(-1.2, 1.2, 121)))
    except:
        print("x_values2 or y_values2 defined incorrectly")
    else:
        print("x_values2 and y_values2 defined correctly")
        score += 1    
    try:
        myx2, myy2 = np.meshgrid(np.linspace(-1.2, 1.2, 121),np.linspace(-1.2, 1.2, 121))
        assert(np.allclose(_globals["x2"], myx2))
        assert(np.allclose(_globals["y2"], myy2))
    except:
        print("x2 or y2 defined incorrectly")
    else:
        print("x2 and y2 defined correctly")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!') 
        
def question2e():   
    return 2       

def question3a(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(_globals["n"] == 10)
        assert(np.isclose(_globals["p"], 0.3))
    except:
        print("n or p defined incorrectly")
    else:
        print("n and p defined correctly")
        score += 1    
    try:
        assert(np.allclose(_globals["r"], np.arange(0,11)))
    except:
        print("r defined incorrectly")
    else:
        print("r defined correctly")
        score += 1
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')       

def question3b(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.allclose(_globals["rfac"], np.array([1,1,2,6,24,120,720,5040,40320,362880,3628800])))
    except:
        print("rfac defined incorrectly")
    else:
        print("rfac defined correctly")
        score += 1    
    try:
        assert(np.allclose(_globals["nmrfac"], np.array([1,1,2,6,24,120,720,5040,40320,362880,3628800])[-1::-1]))
    except:
        print("nmrfac defined incorrectly")
    else:
        print("nmrfac defined correctly")
        score += 1    
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')      

def question3c(_globals):
    number_of_tests = 2
    score = 0
    try:
        assert(np.allclose(_globals["bincoef"], np.array([1.,10.,45,120.,210.,252.,210.,120.,45.,10.,1.])))
    except:
        print("bincoef defined incorrectly")
    else:
        print("bincoef defined correctly")
        score += 1    
    try:
        assert(np.allclose(_globals["binprob"], np.array([2.82475249e-02, 1.21060821e-01, 2.33474440e-01, 2.66827932e-01,2.00120949e-01, 1.02919345e-01, 3.67569090e-02, 9.00169200e-03,1.44670050e-03, 1.37781000e-04, 5.90490000e-06])))
    except:
        print("binprob defined incorrectly")
    else:
        print("binprob defined correctly")
        score += 1    
    if score > 0:
        print("\n{} out of {}".format(score, number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')    

def question3e1(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["data100"],np.ndarray))
    except:
        print("data100 is not a numpy array")
    else:
        print("data100 is a numpy array")
        score0 += 1
    try:
        assert(np.shape(_globals["data100"]) == (100,))
    except:
        print("data100 is not 1D and of length 100")
    else:
        print("data100 is 1D and of length 100")
        score1 += 1
    try:
        assert(all([isinstance(x,np.int16) or isinstance(x,np.int32) or isinstance(x,np.int64) for x in _globals["data100"]]))
    except:
        print("data100 does not consist of numpy ints")
    else:
        print("data100 consists of numpy ints")
        score2 += 1
    try:
        assert(all([x>=0 and x<=10 for x in _globals["data100"]]))
    except:
        print("The elements of data100 are not in the correct range")
    else:
        print("The elements of data100 are in the correct range")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!')    

def question3e2(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["data1000"],np.ndarray))
    except:
        print("data1000 is not a numpy array")
    else:
        print("data1000 is a numpy array")
        score0 += 1
    try:
        assert(np.shape(_globals["data1000"]) == (1000,))
    except:
        print("data1000 is not 1D and of length 1000")
    else:
        print("data1000 is 1D and of length 1000")
        score1 += 1
    try:
        assert(all([isinstance(x,np.int16) or isinstance(x,np.int32) or isinstance(x,np.int64) for x in _globals["data1000"]]))
    except:
        print("data1000 does not consist of numpy ints")
    else:
        print("data1000 consists of numpy ints")
        score2 += 1
    try:
        assert(all([x>=0 and x<=10 for x in _globals["data1000"]]))
    except:
        print("The elements of data1000 are not in the correct range")
    else:
        print("The elements of data1000 are in the correct range")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!')    

def question3e3(_globals):
    number_of_tests = 1
    score = 0
    score0, score1, score2, score3 = 0, 0, 0, 0
    try:
        assert(isinstance(_globals["data10000"],np.ndarray))
    except:
        print("data10000 is not a numpy array")
    else:
        print("data10000 is a numpy array")
        score0 += 1
    try:
        assert(np.shape(_globals["data10000"]) == (10000,))
    except:
        print("data10000 is not 1D and of length 10000")
    else:
        print("data10000 is 1D and of length 10000")
        score1 += 1
    try:
        assert(all([isinstance(x,np.int16) or isinstance(x,np.int32) or isinstance(x,np.int64) for x in _globals["data10000"]]))
    except:
        print("data10000 does not consist of numpy ints")
    else:
        print("data10000 consists of numpy ints")
        score2 += 1
    try:
        assert(all([x>=0 and x<=10 for x in _globals["data10000"]]))
    except:
        print("The elements of data10000 are not in the correct range")
    else:
        print("The elements of data10000 are in the correct range")
        score3 += 1
    score = score0*score1*score2*score3
    if score > 0:
        print("Test passed!")
        return score
    else: 
        raise AssertionError('Test failed!') 

def question4a(_globals):
    number_of_tests = 1
    score = 0
    try:        
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalue = _globals["ifs_step"](mats,vecs,np.array([0.5,0.5]))
        test0 = np.allclose(testvalue,np.array([0.25,0.25]))
        test1 = np.allclose(testvalue,np.array([0.25+0.5,0.25]))
        test2 = np.allclose(testvalue,np.array([0.25+0.25,0.25+np.sqrt(3)/4]))
        assert(test0 or test1 or test2)
    except:
        pass
    else:
        print("Test passed!")
        score += 1 
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed overall!')  

def question4b(_globals):    
    number_of_tests = 1
    score = 0
    try:
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalues = _globals["iterate_ifs"](mats,vecs,np.array([0.5,0.5]),0,3)
        test0 = np.allclose(testvalues[0,:],np.array([0.5,0.5]))
        test10 = np.allclose(testvalues[1,:],testvalues[0,:]/2)
        test11 = np.allclose(testvalues[1,:],testvalues[0,:]/2+np.array([0.5,0.0]))
        test12 = np.allclose(testvalues[1,:],testvalues[0,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test1 = test10 or test11 or test12
        test20 = np.allclose(testvalues[2,:],testvalues[1,:]/2)
        test21 = np.allclose(testvalues[2,:],testvalues[1,:]/2+np.array([0.5,0.0]))
        test22 = np.allclose(testvalues[2,:],testvalues[1,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test2 = test20 or test21 or test22
        test30 = np.allclose(testvalues[3,:],testvalues[2,:]/2)
        test31 = np.allclose(testvalues[3,:],testvalues[2,:]/2+np.array([0.5,0.0]))
        test32 = np.allclose(testvalues[3,:],testvalues[2,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test3 = test30 or test31 or test32
        assert(test0 and test1 and test2 and test3)
    except:
        pass
    else:
        print("Test passed!")
        score += 1 
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed overall!')  
        
def question4d(_globals):
    number_of_tests = 3
    score = 0
    score0, score1, score2 = 0, 0, 0
    print("Testing with default weights")
    try:        
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalue = _globals["ifs_step"](mats,vecs,np.array([0.5,0.5]))
        test0 = np.allclose(testvalue,np.array([0.25,0.25]))
        test1 = np.allclose(testvalue,np.array([0.25+0.5,0.25]))
        test2 = np.allclose(testvalue,np.array([0.25+0.25,0.25+np.sqrt(3)/4]))
        assert(test0 or test1 or test2)
    except:
        print("Test failed!")
    else:
        print("Test passed!")
        score0 += 1 
    print("\nTesting with set weights: typical case")
    try:        
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalue = _globals["ifs_step"](mats,vecs,np.array([0.5,0.5]),weights=[1,1,1])
        test0 = np.allclose(testvalue,np.array([0.25,0.25]))
        test1 = np.allclose(testvalue,np.array([0.25+0.5,0.25]))
        test2 = np.allclose(testvalue,np.array([0.25+0.25,0.25+np.sqrt(3)/4]))
        assert(test0 or test1 or test2)
    except:
        print("Test failed!")
    else:
        print("Test passed!")
        score1 += 1 
    print("\nTesting with set weights: edge case")
    try:        
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalue = _globals["ifs_step"](mats,vecs,np.array([0.5,0.5]),weights=[1,0,0])
        test0 = np.allclose(testvalue,np.array([0.25,0.25]))
        assert(test0)
    except:
        print("Test failed!")
    else:
        print("Test passed!")
        score2 += 1 
    score = score0 + score1 + score2
    if score > 0:
        print("\n{} out of {}".format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')  

def question4e(_globals):    
    number_of_tests = 3
    score = 0
    score0, score1, score2 = 0, 0, 0
    print("Testing with default weights")
    try:
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalues = _globals["iterate_ifs"](mats,vecs,np.array([0.5,0.5]),0,3)
        test0 = np.allclose(testvalues[0,:],np.array([0.5,0.5]))
        test10 = np.allclose(testvalues[1,:],testvalues[0,:]/2)
        test11 = np.allclose(testvalues[1,:],testvalues[0,:]/2+np.array([0.5,0.0]))
        test12 = np.allclose(testvalues[1,:],testvalues[0,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test1 = test10 or test11 or test12
        test20 = np.allclose(testvalues[2,:],testvalues[1,:]/2)
        test21 = np.allclose(testvalues[2,:],testvalues[1,:]/2+np.array([0.5,0.0]))
        test22 = np.allclose(testvalues[2,:],testvalues[1,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test2 = test20 or test21 or test22
        test30 = np.allclose(testvalues[3,:],testvalues[2,:]/2)
        test31 = np.allclose(testvalues[3,:],testvalues[2,:]/2+np.array([0.5,0.0]))
        test32 = np.allclose(testvalues[3,:],testvalues[2,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test3 = test30 or test31 or test32
        assert(test0 and test1 and test2 and test3)
    except:
        print("Test failed!")
    else:
        print("Test passed!")
        score0 += 1 
    print("\nTesting with set weights: typical case")
    try:
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalues = _globals["iterate_ifs"](mats,vecs,np.array([0.5,0.5]),0,3,weights=[1,1,1])
        test0 = np.allclose(testvalues[0,:],np.array([0.5,0.5]))
        test10 = np.allclose(testvalues[1,:],testvalues[0,:]/2)
        test11 = np.allclose(testvalues[1,:],testvalues[0,:]/2+np.array([0.5,0.0]))
        test12 = np.allclose(testvalues[1,:],testvalues[0,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test1 = test10 or test11 or test12
        test20 = np.allclose(testvalues[2,:],testvalues[1,:]/2)
        test21 = np.allclose(testvalues[2,:],testvalues[1,:]/2+np.array([0.5,0.0]))
        test22 = np.allclose(testvalues[2,:],testvalues[1,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test2 = test20 or test21 or test22
        test30 = np.allclose(testvalues[3,:],testvalues[2,:]/2)
        test31 = np.allclose(testvalues[3,:],testvalues[2,:]/2+np.array([0.5,0.0]))
        test32 = np.allclose(testvalues[3,:],testvalues[2,:]/2+np.array([0.25,np.sqrt(3)/4]))
        test3 = test30 or test31 or test32
        assert(test0 and test1 and test2 and test3)
    except:
        print("Test failed!")
    else:
        print("Test passed!")
        score1 += 1 
    print("\nTesting with set weights: edge case")
    try:
        mat0 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat1 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mat2 = np.array([[1.0,0.0],[0.0,1.0]])/2
        mats = np.array([mat0,mat1,mat2])
        vec0 = np.array([0.0,0.0])
        vec1 = np.array([0.5,0.0])
        vec2 = np.array([0.25,np.sqrt(3)/4])
        vecs = np.array([vec0,vec1,vec2])
        testvalues = _globals["iterate_ifs"](mats,vecs,np.array([0.5,0.5]),0,3,weights=[1,0,0])
        test0 = np.allclose(testvalues[0,:],np.array([0.5,0.5]))
        test1 = np.allclose(testvalues[1,:],testvalues[0,:]/2)
        test2 = np.allclose(testvalues[2,:],testvalues[1,:]/2)
        test3 = np.allclose(testvalues[3,:],testvalues[2,:]/2)
        assert(test0 and test1 and test2 and test3)
    except:
        print("Test failed!")
    else:
        print("Test passed!")
        score2 += 1
    score = score0 + score1 + score2
    score = score0 + score1 + score2
    if score > 0:
        print("\n{} out of {}".format(score,number_of_tests))
        return score
    else: 
        raise AssertionError('Test failed overall!')  