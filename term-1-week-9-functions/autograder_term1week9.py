import numpy.testing as npt
from time import time
from numpy import isclose, allclose
from math import cos, exp
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
    score0, score1, score2 = 0, 0, 0
    number_of_tests = 1
    try:
        assert(_globals['xsqdplusone'](1) == 2)
    except:
        print('Your function returned the wrong output for the input 1')
        pass
    else:
        print('Your function returned the correct output for the input 1')
        score0 += 1
    try:
        assert(isclose(_globals['xsqdplusone'](0.357),1.127449))
    except:
        print('Your function returned the wrong output for the input 0.357')
        pass
    else:
        print('Your function returned the correct output for the input 0.357')
        score1 += 1
    try:
        assert(isclose(_globals['xsqdplusone'](3+2j),(6+12j)))
    except:
        print('Your function returned the wrong output for the input (3+2j)')
        pass
    else:
        print('Your function returned the correct output for the input (3+2j)')
        score2 += 1
    #return score 
    score = score0*score1*score2
    if score > 0:
        print('Question 1a passed!')
        return score
    else: 
        raise AssertionError('Test failed!!')

def question1b(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    number_of_tests = 2
    print('Test 1: positive odd argument')
    try:
        assert(_globals['hailstone_step'](1) == 4)
    except:
        print('Your function returned numerically wrong output for the input 1')
        pass
    else:
        print('Your function returned numerically correct output for the input 1')
        score00 += 1
    try:
        assert(type(_globals['hailstone_step'](1)) == int)
    except:
        print('Your function returned output of the wrong numerical type for the input 1')
        pass
    else:
        print('Your function returned output of the correct numerical type for the input 1')
        score01 += 1
    score0 = score00 * score01
    if score0 > 0:
        print('Test 1 passed!\n')
    else:
        print('Test 1 failed!\n')
    print('Test 2: positive even argument')
    try:
        assert(_globals['hailstone_step'](28) == 14)
    except:
        print('Your function returned numerically wrong output for the input 28')
        pass
    else:
        print('Your function returned numerically correct output for the input 28')
        score10 += 1
    try:
        assert(type(_globals['hailstone_step'](28)) == int)
    except:
        print('Your function returned output of the wrong numerical type for the input 28')
        pass
    else:
        print('Your function returned output of the correct numerical type for the input 28')
        score11 += 1
    score1 = score10 * score11
    if score1 > 0:
        print('Test 2 passed!\n')
    else:
        print('Test 2 failed!\n')
    #return score 
    score = score0 + score1
    if score == 2:
        print("2 marks out of 2")
        return score
    elif score == 1:
        print("1 mark out of 2")
        return score
    else: 
        raise AssertionError('Test failed!!')

def question1c(_globals):
    score0, score1, score2 = 0, 0, 0
    
    print('Test 1: typical case')
    try:
        assert(_globals['my_factorial'](5) == 120)
    except:
        print('Your function returned the wrong output for the input 5\nTest 1 failed!\n')
        pass
    else:
        print('Your function returned the correct output for the input 5\nTest 1 passed!\n')
        score0 += 1
    
    print('Test 2: edge case')
    try:
        assert(_globals['my_factorial'](0) == 1)
    except:
        print('Your function returned the wrong output for the input 0\nTest 2 failed!\n')
        pass
    else:
        print('Your function returned the correct output for the input 0\nTest 2 passed!\n')
        score1 += 1
    
    print('Test 3: large int output')
    try:
        assert(_globals['my_factorial'](1000) == 402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    except:
        print('Your function returned the wrong output for the input 1000\nTest 3 failed!\n')
        pass
    else:
        print('Your function returned the correct output for the input 1000\nTest 3 passed!\n')
        score2 += 1
        
    score = score0 + score1 + score2
    if score > 1:
        print(f"{score} marks out of 3")
        return score
    elif score == 1:
        print("1 mark out of 3")
        return score
    else: 
        raise AssertionError('Test failed!!')

def question1d(_globals):
    score0 = 0
    score10, score11 = 0, 0
    print('Test 1: a list of typical cases, tested with a comprehension')
    try:
        assert([_globals['fibonacci'](a) for a in range(3,11)] == [2, 3, 5, 8, 13, 21, 34, 55])
    except:
        print('Your function returned the wrong output for at least one of the integers 3, 4, ..., 10\nTest 1 failed!\n')
        pass
    else:
        print('Your function returned the correct output for all of the integers 3, 4, ..., 10\nTest 1 passed!\n')
        score0 += 1
    print('Test 2: edge cases')
    try:
        assert(_globals['fibonacci'](1) == 1)
    except:
        print('Your function returned the wrong output for the input 1')
        pass
    else:
        print('Your function returned the correct output for the input 1')
        score10 += 1
    try:
        assert(_globals['fibonacci'](2) == 1)
    except:
        print('Your function returned the wrong output for the input 2')
        pass
    else:
        print('Your function returned the correct output for the input 2')
        score11 += 1
    score1 = score10 * score11
    if score1 > 0:
        print('Test 2 passed!\n')
    else:
        print('Test 2 failed!\n')
    score = score0 + score1
    if score == 2:
        print("2 marks out of 2")
        return score
    elif score == 1:
        print("1 mark out of 2")
        return score
    else: 
        raise AssertionError('Test failed!!')
        
def question1e(_globals):    
    score0, score1, score3 = 0, 0, 0
    score20, score21 = 0, 0
    print('Test 1: typical case, non-square')    
    try:
        assert(_globals['factor_sum'](24) == 60)
    except:
        print('Your function returned the wrong output for the input 24\nTest 1 failed!\n')
        pass
    else:
        print('Your function returned the correct output for the input 24\nTest 1 passed!\n')
        score0 += 1   
    print('Test 2: typical case, square')   
    try:
        assert(_globals['factor_sum'](36) == 91)
    except:
        print('Your function returned the wrong output for the input 36\nTest 2 failed!\n')
        pass
    else:
        print('Your function returned the correct output for the input 36\nTest 2 passed!\n')
        score1 += 1  
    print('Test 3: edge cases')   
    try:
        assert(_globals['factor_sum'](1) == 1)
    except:
        print('Your function returned the wrong output for the input 1')
        pass
    else:
        print('Your function returned the correct output for the input 1')
        score20 += 1 
    try:
        assert(_globals['factor_sum'](0) == 0)
    except:
        print('Your function returned the wrong output for the input 0')
        pass
    else:
        print('Your function returned the correct output for the input 0')
        score21 += 1
    score2 = score20 * score21
    if score2 > 0:
        print('Test 3 passed!\n')
    else:
        print('Test 3 failed!\n')
    print('Test 4: efficiency')
    try:
        start = time()
        _globals['factor_sum'](1000000)
        duration = time() - start
        assert(duration < 0.01)    
    except:
        print('Your function seemed to take too long to calculate the factor sum of one million; have you implemented it as efficiently as poosible?\nTest 4 failed!\n')
        pass
    else:
        print('Your function seemed to calculate the factor sum of one million in good time.\nTest 4 passed!\n')
        score3 += 1  

    score = score0 + score1 + score2 + score3
    if score > 1:
        print(f"{score} marks out of 4")
        return score
    elif score == 1:
        print("1 mark out of 4")
        return score
    else: 
        raise AssertionError('Test failed!!')

def question1f(_globals):  
    score0, score1, score2, score3 = 0, 0, 0, 0
    print('Test 1')       
    try:
        assert(isclose(_globals['nest'](cos, 1.0, 5), 0.7013687736227566))
    except:
        print('nest(cos, 1.0, 5) returned an incorrect value\nTest 1 failed!\n')
        pass
    else:
        print('nest(cos, 1.0, 5) returned the correct value\nTest 1 passed!\n')
        score0 += 1   
    print('Test 2')       
    try:
        assert(isclose(_globals['nest'](lambda x: exp(-x), 1.0, 10), 0.5684287250290607))
    except:
        print('An attempt to iterate the function that maps x to exp(-x) 10 times with x0 = 1.0 returned an incorrect value\nTest 2 failed!\n')
        pass
    else:
        print('An attempt to iterate the function that maps x to exp(-x) 10 times with x0 = 1.0 returned the correct value\nTest 2 passed!\n')
        score1 += 1      
    print('Test 3')       
    try:
        assert(isclose(_globals['nest'](lambda x: 4*x*(1-x), 0.3, 20), 0.9417846056085262))
    except:
        print('An attempt to iterate the function that maps x to 4*x*(1-x) 20 times with x0 = 0.3 returned an incorrect value\nTest 3 failed!\n')
        pass
    else:
        print('An attempt to iterate the function that maps x to 4*x*(1-x) 20 times with x0 = 0.3 returned the correct value\nTest 3 passed!\n')
        score2 += 1       
    print('Test 4: the value of x20')       
    try:
        assert(isclose(_globals['x20'], 0.9417846056085262))
    except:
        print('Your calculated value of x20 is incorrect\nTest 4 failed!\n')
        pass
    else:
        print('Your calculated value of x20 is correct\nTest 4 passed!\n')
        score3 += 1 
    score = score0 + score1 + score2 + score3
    if score > 1:
        print(f"{score} marks out of 4")
        return score
    elif score == 1:
        print("1 mark out of 4")
        return score
    else: 
        raise AssertionError('Test failed!!')  

def question2a(_globals): 
    score0, score1, score2, score3 = 0, 0, 0, 0    
    try:
        assert(type(_globals['hailstone_sequence'](36,20)) == list)
    except:
        print('hailstone_sequence(36, 20) did not return a list')
        pass
    else:
        print('hailstone_sequence(36, 20) returned a list')
        score0 += 1         
    try:
        assert(type(_globals['hailstone_sequence'](36,2)[1]) == int)
        assert(type(_globals['hailstone_sequence'](35,2)[1]) == int)
    except:
        print('Your function does not seem to return a sequence of ints')
        pass
    else:
        print('Your function returns a sequence of ints')
        score1 += 1      
    try:
        assert(len(_globals['hailstone_sequence'](36,20)) == 21)
    except:
        print('hailstone_sequence(36, 20) did not return a sequence of the correct length')
        pass
    else:
        print('hailstone_sequence(36, 20) returned a sequence of the correct length')
        score2 += 1      
    try:
        assert(_globals['hailstone_sequence'](36,20) == [36, 18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2])
    except:
        print('hailstone_sequence(36, 20) returned an incorrect value')
        pass
    else:
        print('hailstone_sequence(36, 20) returned the correct value')
        score3 += 1 
    score = score0 + score1 + score2 + score3
    if score > 1:
        print(f"{score} marks out of 4")
        return score
    elif score == 1:
        print("1 mark out of 4")
        return score
    else: 
        raise AssertionError('Test failed!!')  

def question2b(_globals):
    score0, score10, score11 = 0, 0, 0
    print('Test 1: typical case')
    try:
        assert(_globals['fibonacci_sequence'](10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    except:
        print('fibonacci_sequence(10) returned an incorrect value\nTest 1 failed!\n')
        pass
    else:
        print('fibonacci_sequence(10) returned the correct value\nTest 1 passed!\n')
        score0 += 1    
    print('Test 2: edge cases')
    try:
        assert(_globals['fibonacci_sequence'](2) == [1, 1])
    except:
        print('fibonacci_sequence(2) returned an incorrect value')
        pass
    else:
        print('fibonacci_sequence(2) returned the correct value')
        score10 += 1
    try:
        assert(_globals['fibonacci_sequence'](1) == [1])
    except:
        print('fibonacci_sequence(1) returned an incorrect value')
        pass
    else:
        print('fibonacci_sequence(1) returned the correct value')
        score11 += 1
    score1 = score10 * score11 
    if score1 == 1:
        print('Test 2 passed!\n')
    else:
        print('Test 2 failed!\n')    
    score = score0 + score1
    if score == 2:
        print("2 marks out of 2")
        return score
    elif score == 1:
        print("1 mark out of 2")
        return score
    else: 
        raise AssertionError('Test failed!!')  

def question2c(_globals):
    score0, score10, score11, score12, score13 = 0, 0, 0, 0, 0
    print('Test 1: typical case')
    try:
        assert(_globals['aliquot_chain'](24, 5) == [24, 36, 55, 17, 1, 0])
    except:
        print('aliquot_chain(24, 5) returned an incorrect value\nTest 1 failed!\n')
        pass
    else:
        print('aliquot_chain(24, 5) returned the correct value\nTest 1 passed!\n')
        score0 += 1    
    print('Test 2: edge cases')
    try:
        assert(_globals['aliquot_chain'](24, 1) == [24, 36])
    except:
        print('aliquot_chain(24, 1) returned an incorrect value')
        pass
    else:
        print('aliquot_chain(24, 1) returned the correct value')
        score10 += 1
    try:
        assert(_globals['aliquot_chain'](24, 0) == [24])
    except:
        print('aliquot_chain(24, 0) returned an incorrect value')
        pass
    else:
        print('aliquot_chain(24, 0) returned the correct value')
        score11 += 1
    try:
        assert(_globals['aliquot_chain'](1, 5) == [1, 0, 0, 0, 0, 0])
    except:
        print('aliquot_chain(1, 5) returned an incorrect value')
        pass
    else:
        print('aliquot_chain(1, 5) returned the correct value')
        score12 += 1
    try:
        assert(_globals['aliquot_chain'](0, 5) == [0, 0, 0, 0, 0, 0])
    except:
        print('aliquot_chain(0, 5) returned an incorrect value')
        pass
    else:
        print('aliquot_chain(0, 5) returned the correct value')
        score13 += 1
    score1 = score10 * score11 * score12 * score13
    if score1 == 1:
        print('Test 2 passed!\n')
    else:
        print('Test 2 failed!\n')    
    score = score0 + score1
    if score == 2:
        print("2 marks out of 2")
        return score
    elif score == 1:
        print("1 mark out of 2")
        return score
    else: 
        raise AssertionError('Test failed!!')  

def question2d(_globals):  
    score0, score1, score2, score3 = 0, 0, 0, 0
    print('Test 1')
    try:
        assert(allclose(_globals['nest_list'](cos, 1.0, 5), [1.0, 0.5403023058681398, 0.8575532158463933, 0.6542897904977792, 0.7934803587425655, 0.7013687736227566]))
    except:
        print('nest_list(cos, 1.0, 5) returned an incorrect value\nTest 1 failed!\n')
        pass
    else:
        print('nest_list(cos, 1.0, 5) returned the correct value\nTest 1 passed!\n')
        score0 += 1   
    print('Test 2')       
    try:
        assert(allclose(_globals['nest_list'](lambda x: exp(-x), 1.0, 10), [1.0, 0.36787944117144233, 0.6922006275553464, 0.5004735005636368, 0.6062435350855974, 0.545395785975027, 0.5796123355033789, 0.5601154613610891, 0.571143115080177, 0.5648793473910495, 0.5684287250290607]))
    except:
        print('An attempt to iterate the function that maps x to exp(-x) 10 times with x0 = 1.0 returned an incorrect value\nTest 2 failed!\n')
        pass
    else:
        print('An attempt to iterate the function that maps x to exp(-x) 10 times with x0 = 1.0 returned the correct value\nTest 2 passed!\n')
        score1 += 1      
    print('Test 3')       
    try:
        assert(allclose(_globals['nest_list'](lambda x: 4*x*(1-x), 0.3, 20), [0.3, 0.84, 0.5376000000000001, 0.9943449599999999, 0.02249224209039382, 0.08794536454456375, 0.32084390959875014, 0.8716123810885569, 0.4476169528867727, 0.9890240655005337, 0.043421853445318986, 0.1661455843547689, 0.5541649166167251, 0.9882646472316129, 0.04639053705515447, 0.17695382050755523, 0.5825646636613406, 0.9727323052579588, 0.10609667026198408, 0.3793606672852156, 0.9417846056085262]))
    except:
        print('An attempt to iterate the function that maps x to 4*x*(1-x) 20 times with x0 = 0.3 returned an incorrect value\nTest 3 failed!\n')
        pass
    else:
        print('An attempt to iterate the function that maps x to 4*x*(1-x) 20 times with x0 = 0.3 returned the correct value\nTest 3 passed!\n')
        score2 += 1       
    print('Test 4: the value of xlist20')       
    try:
        assert(allclose(_globals['xlist20'], [0.3, 0.84, 0.5376000000000001, 0.9943449599999999, 0.02249224209039382, 0.08794536454456375, 0.32084390959875014, 0.8716123810885569, 0.4476169528867727, 0.9890240655005337, 0.043421853445318986, 0.1661455843547689, 0.5541649166167251, 0.9882646472316129, 0.04639053705515447, 0.17695382050755523, 0.5825646636613406, 0.9727323052579588, 0.10609667026198408, 0.3793606672852156, 0.9417846056085262]))
    except:
        print('Your calculated value of x20 is incorrect\nTest 4 failed!\n')
        pass
    else:
        print('Your calculated value of x20 is correct\nTest 4 passed!\n')
        score3 += 1 
    score = score0 + score1 + score2 + score3
    if score > 1:
        print(f"{score} marks out of 4")
        return score
    elif score == 1:
        print("1 mark out of 4")
        return score
    else: 
        raise AssertionError('Test failed!!') 
        
def question2e(_globals):  
    score0, score1, score2, score3 = 0, 0, 0, 0
    print('Test 1')       
    try:
        duffing_its = _globals['duffing_iterates'](1.0,1.0,0.5,0.5,10)
        assert(isinstance(duffing_its,tuple))
    except:
        print('Your function does not seem to return a tuple.\n')
        pass
    else:
        print('Your function returns a tuple\n')
        score0 += 1   
    print('Test 2')       
    try:
        duffing_its = _globals['duffing_iterates'](1.0,1.0,0.5,0.5,10)
        assert(isinstance(duffing_its[0],list) and isinstance(duffing_its[1],list))
    except:
        print('The elements of your tuple do not appear to be lists.\n')
        pass
    else:
        print('The elements of your tuple are lists.\n')
        score1 += 1      
    print('Test 3')       
    try:
        duffing_its = _globals['duffing_iterates'](1.0,1.0,0.5,0.5,10)
        assert(allclose(duffing_its[0],[0.5, 0.5, -0.125, -0.623046875, -0.25618792325258255, 0.38367314209093206, 0.5833824297827745, 0.0011637938109085033, -0.5822186375481271, -0.38602280653107773, 0.2537184818650942]) and allclose(duffing_its[1],[0.5, -0.125, -0.623046875, -0.25618792325258255, 0.38367314209093206, 0.5833824297827745, 0.0011637938109085033, -0.5822186375481271, -0.38602280653107773, 0.2537184818650942, 0.6234086513000829]))
    except:
        print('Your function does not seem to return the correct numbers.\n')
        pass
    else:
        print('Your function seems to return the correct numbers.\n')
        score2 += 1       
    print('Test 4')       
    try:
        xvals, yvals = _globals['duffing_iterates'](1.0,1.0,0.5,0.5,10)
        assert(allclose(xvals,[0.5, 0.5, -0.125, -0.623046875, -0.25618792325258255, 0.38367314209093206, 0.5833824297827745, 0.0011637938109085033, -0.5822186375481271, -0.38602280653107773, 0.2537184818650942]) and allclose(yvals,[0.5, -0.125, -0.623046875, -0.25618792325258255, 0.38367314209093206, 0.5833824297827745, 0.0011637938109085033, -0.5822186375481271, -0.38602280653107773, 0.2537184818650942, 0.6234086513000829]))
    except:
        print('Your function does not seem to be able to assign values to two variables at the same time.\n')
        pass
    else:
        print('Your function successfully assigns values to two variables at the same time.\n')
        score3 += 1 
    score = score0 + score1 + score2 + score3
    if score > 1:
        print(f"{score} marks out of 4")
        return score
    elif score == 1:
        print("1 mark out of 4")
        return score
    else: 
        raise AssertionError('Test failed!!') 

def question3a(_globals): 
    score0, score1, score2, score3, score4 = 0, 0, 0, 0, 0   
    try:
        assert(type(_globals['hailstone_sequence2'](36)) == list)
    except:
        print('hailstone_sequence2(30) did not return a list')
        pass
    else:
        print('hailstone_sequence2(30) returned a list')
        score0 += 1         
    try:
        assert(type(_globals['hailstone_sequence2'](36)[1]) == int)
        assert(type(_globals['hailstone_sequence2'](35)[1]) == int)
    except:
        print('Your function does not seem to return a sequence of ints')
        pass
    else:
        print('Your function returns a sequence of ints')
        score1 += 1      
    try:
        assert(_globals['hailstone_sequence2'](36)[-1] == 1)
    except:
        print('hailstone_sequence2(36) did not return a sequence terminating in 1')
        pass
    else:
        print('hailstone_sequence2(36, 20) returned a sequence terminating in 1')
        score2 += 1      
    try:
        assert(_globals['hailstone_sequence2'](36) == [36, 18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    except:
        print('hailstone_sequence2(36) returned an incorrect value')
        pass
    else:
        print('hailstone_sequence2(36) returned the correct value')
        score3 += 1      
    try:
        assert(_globals['hailstone_sequence2'](1) == [1])
    except:
        print('hailstone_sequence2(1) returned an incorrect value')
        pass
    else:
        print('hailstone_sequence2(1) returned the correct value')
        score4 += 1 
    score = score0 + score1 + score2 + score3 + score4
    if score > 1:
        print(f"{score} marks out of 5")
        return score
    elif score == 1:
        print("1 mark out of 5")
        return score
    else: 
        raise AssertionError('Test failed!!')    

def question3b(_globals): 
    score0, score1, score2, score3, score4 = 0, 0, 0, 0, 0   
    try:
        assert(_globals['aliquot_chain2'](120) == [120, 240, 504, 1056, 1968, 3240, 7650, 14112, 32571, 27333, 12161, 1, 0, 0])
    except:
        print('aliquot_chain2(120) returned an incorrect value')
        pass
    else:
        print('aliquot_chain2(120) returned the correct value')
        score0 += 1     
    try:
        assert(_globals['aliquot_chain2'](496) == [496, 496])
    except:
        print('aliquot_chain2(496) returned an incorrect value')
        pass
    else:
        print('aliquot_chain2(496) returned the correct value')
        score1 += 1          
    try:
        assert(_globals['aliquot_chain2'](1184) == [1184, 1210, 1184])
    except:
        print('aliquot_chain2(1184) returned an incorrect value')
        pass
    else:
        print('aliquot_chain2(1184) returned the correct value')
        score2 += 1          
    try:
        assert(_globals['aliquot_chain2'](1264460) == [1264460, 1547860, 1727636, 1305184, 1264460])
    except:
        print('aliquot_chain2(1264460) returned an incorrect value')
        pass
    else:
        print('aliquot_chain2(1264460) returned the correct value')
        score3 += 1          
    try:
        assert(_globals['aliquot_chain2'](0) == [0, 0])
    except:
        print('aliquot_chain2(0) returned an incorrect value')
        pass
    else:
        print('aliquot_chain2(0) returned the correct value')
        score4 += 1         
    score = score0 + score1 + score2 + score3 + score4
    if score > 1:
        print(f"{score} marks out of 5")
        return score
    elif score == 1:
        print("1 mark out of 5")
        return score
    else: 
        raise AssertionError('Test failed!!')  

def question3c(_globals):  
    score0, score1, score2 = 0, 0, 0
    print('Test 1')       
    try:
        assert(allclose(_globals['fixed_point_list'](cos, 1.0, 1e-5), [1.0, 0.5403023058681398, 0.8575532158463933, 0.6542897904977792, 0.7934803587425655, 0.7013687736227566, 0.7639596829006542, 0.7221024250267077, 0.7504177617637605, 0.7314040424225098, 0.7442373549005569, 0.7356047404363473, 0.7414250866101093, 0.7375068905132428, 0.7401473355678757, 0.7383692041223232, 0.739567202212256, 0.7387603198742114, 0.7393038923969057, 0.7389377567153446, 0.7391843997714936, 0.7390182624274122, 0.7391301765296711, 0.7390547907469175, 0.7391055719265361, 0.739071365298945, 0.7390944073790912, 0.7390788859949922, 0.7390893414033927, 0.7390822985224023]))
    except:
        print('nest_list(cos, 1.0, 1e-5) returned an incorrect value\nTest 1 failed!\n')
        pass
    else:
        print('nest_list(cos, 1.0, 1e-5) returned the correct value\nTest 1 passed!\n')
        score0 += 1   
    print('Test 2')       
    try:
        assert(allclose(_globals['fixed_point_list'](lambda x: exp(-x), 1.0, 1e-5), [1.0, 0.36787944117144233, 0.6922006275553464, 0.5004735005636368, 0.6062435350855974, 0.545395785975027, 0.5796123355033789, 0.5601154613610891, 0.571143115080177, 0.5648793473910495, 0.5684287250290607, 0.5664147331468833, 0.5675566373282834, 0.5669089119214953, 0.5672762321755696, 0.5670678983907884, 0.567186050099357, 0.5671190400572149, 0.5671570440012975, 0.5671354902062784, 0.5671477142601192, 0.567140781458298]))
    except:
        print('An attempt to iterate the function that maps x to exp(-x) with x0 = 1.0 and a tolerance of 1e-5 returned an incorrect value\nTest 2 failed!\n')
        pass
    else:
        print('An attempt to iterate the function that maps x to exp(-x) with x0 = 1.0 and a tolerance of 1e-5 returned the correct value\nTest 2 passed!\n')
        score1 += 1      
    print('Test 3')       
    try:
        assert(allclose(_globals['fixed_point_list'](lambda x: (x+2.0)/(x+1.0), 1.0, 1e-6), [1.0, 1.5, 1.4, 1.4166666666666667, 1.4137931034482758, 1.4142857142857144, 1.4142011834319526, 1.4142156862745099, 1.4142131979695431, 1.4142136248948696]))
    except:
        print('An attempt to iterate the function that maps x to (x+2.0)/(x+1.0) with x0 = 1.0 and a tolerance of 1e-6 returned an incorrect value\nTest 3 failed!\n')
        pass
    else:
        print('An attempt to iterate the function that maps x to (x+2.0)/(x+1.0) with x0 = 1.0 and a tolerance of 1e-6 returned the correct value\nTest 3 passed!\n')
        score2 += 1 
    score = score0 + score1 + score2
    if score > 1:
        print(f"{score} marks out of 3")
        return score
    elif score == 1:
        print("1 mark out of 3")
        return score
    else: 
        raise AssertionError('Test failed!!')   
        
def question3d(_globals):
    score = 0
    score0, score1, score2 = 0, 0, 0
    number_of_tests = 3
    print('Test 1: a is a power of 2\n')
    try: 
        assert(_globals['binary_digits'](2**15) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] or _globals['binary_digits'](2**15) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    except:
        print('binary_digits(2**15) did not return the correct list of digits')
    else:
        print('binary_digits(2**15) returned the correct list of digits')
        score0 += 1
    try: 
        assert(_globals['binary_digits'](2**15) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    except:
        if _globals['binary_digits'](2**15) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]:
            print('However, digits are in reverse order\n')
        else:
            print('')
        score0 = 0
    else:
        print('The digits are in the correct order\n')
    score += score0
    print('Test 2: a is not a power of 2\n')
    try: 
        assert(_globals['binary_digits'](14827) == [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1] or _globals['binary_digits'](14827) == [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1])
    except:
        print('binary_digits(14827) did not return the correct list of digits')
    else:
        print('binary_digits(14827) returned the correct list of digits')
        score1 += 1
    try: 
        assert(_globals['binary_digits'](14827) == [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1])
    except:
        if _globals['binary_digits'](14827) == [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]:
            print('However, digits are in reverse order\n')
        else:
            print('')
        score1 = 0
    else:
        print('The digits are in the correct order\n')
    score += score1        
    print('Test 3: edge cases\n')
    try: 
        assert(_globals['binary_digits'](1) == [1])
    except:
        print('binary_digits(1) did not return the correct list of digits')
    else:
        print('binary_digits(1) returned the correct list of digits')
        score2 += 1
    try: 
        assert(_globals['binary_digits'](0) == [0])
    except:
        print('binary_digits(0) did not return the correct list of digits\n')
        score2 = 0
    else:
        print('binary_digits(0) returned the correct list of digits\n')
    score += score2
    if score > 1:
        print(f"{score} marks out of {number_of_tests}")
        return score
    elif score == 1:
        print(f"1 mark out of {number_of_tests}")
        return score
    else: 
        raise AssertionError('Test failed!!')   
        
def question3e(_globals):
    score0, score1, score2, score3 = 0, 0, 0, 0
    score = 0
    number_of_tests = 4
    print('Test 1: typical case\n')
    try: 
        assert(_globals['binary_digits_float'](12.8191,10)[0] == [1, 1, 0, 0])
    except:
        print('binary_digits_float(12.8191,10) did not return the correct list of digits for the integer part')
    else:
        print('binary_digits_float(12.8191,10) returned the correct list of digits for the integer part')
        score0 += 1
    try: 
        assert(_globals['binary_digits_float'](12.8191,10)[1] == [1, 1, 0, 1, 0, 0, 0, 1, 1, 0])
    except:
        print('binary_digits_float(12.8191,10) did not return the correct list of digits for the fractional part\n')
        score0 = 0
    else:
        print('binary_digits_float(12.8191,10) returned the correct list of digits for the fractional part\n')
    score += score0
    print('Tests 2: fractional part begins with zeros\n')
    try: 
        assert(_globals['binary_digits_float'](12.2191,10)[1][-8::] == [1, 1, 1, 0, 0, 0, 0, 0])
    except:
        print('binary_digits_float(12.2191,10) did not return the correct list of digits for the fractional part\n')
    else:
        print('binary_digits_float(12.2191,10) returned the correct list of digits for the fractional part,')
        score1 += 1
    try: 
        assert(_globals['binary_digits_float'](12.2191,10)[1] == [0, 0, 1, 1, 1, 0, 0, 0, 0, 0])
    except:
        if _globals['binary_digits_float'](12.2191,10)[1][-8::] == [1, 1, 1, 0, 0, 0, 0, 0]:
            print('except that the two leading zeros are missing; an easy mistake to make! Can you fix it?\n')
        else:
            print('')
        score1 = 0
    else:
        print('including the two leading zeros\n')
    score += score1
    print('Test 3: integer part is zero\n')
    try: 
        assert(_globals['binary_digits_float'](0.8191,10)[0] == [0])
    except:
        print('binary_digits_float(0.8191,10) did not return the correct list of digits for the integer part')
    else:
        print('binary_digits_float(0.8191,10) returned the correct list of digits for the integer part')
        score2 += 1
    try: 
        assert(_globals['binary_digits_float'](0.8191,10)[1] == [1, 1, 0, 1, 0, 0, 0, 1, 1, 0])
    except:
        print('binary_digits_float(0.8191,10) did not return the correct list of digits for the fractional part\n')
        score2 = 0
    else:
        print('binary_digits_float(0.8191,10) returned the correct list of digits for the fractional part\n')
    score += score2
    print('Test 4: fractional part is zero\n')
    try: 
        assert(_globals['binary_digits_float'](12.0,10)[0] == [1, 1, 0, 0])
    except:
        print('binary_digits_float(12.0,10) did not return the correct list of digits for the integer part')
    else:
        print('binary_digits_float(12.0,10) returned the correct list of digits for the integer part')
        score3 += 1
    try: 
        assert(_globals['binary_digits_float'](12.0,10)[1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    except:
        print('binary_digits_float(12.0,10) did not return the correct list of digits for the fractional part\n')
        score3 = 0
    else:
        print('binary_digits_float(12.0,10) returned the correct list of digits for the fractional part\n')
    score += score3
    if score > 1:
        print(f"{score} marks out of {number_of_tests}")
        return score
    elif score == 1:
        print(f"1 mark out of {number_of_tests}")
        return score
    else: 
        raise AssertionError('Test failed!!')   

def question4(_globals): 
    score0, score1, score2, score3, score4 = 0, 0, 0, 0, 0   
    print('Test 1: n composite, non-square')
    try:
        assert(_globals['my_primes'](98) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    except:
        print('my_primes(98) returned an incorrect value\nTest 1 failed!\n')
        pass
    else:
        print('my_primes(98) returned the correct value\nTest 1 passed!\n')
        score0 += 1   
    print('Test 2: n prime')
    try:
        assert(_globals['my_primes'](97) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    except:
        print('my_primes(97) returned an incorrect value\nTest 2 failed!\n')
        pass
    else:
        print('my_primes(97) returned the correct value\nTest 2 passed!\n')
        score1 += 1   
    print('Test 3: n the square of a composite number')
    try:
        assert(_globals['my_primes'](100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    except:
        print('my_primes(100) returned an incorrect value\nTest 3 failed!\n')
        pass
    else:
        print('my_primes(100) returned the correct value\nTest 3 passed!\n')
        score2 += 1  
    print('Test 4: n the square of a prime')
    try:
        assert(_globals['my_primes'](121) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])
    except:
        print('my_primes(121) returned an incorrect value\nTest 4 failed!\n')
        pass
    else:
        print('my_primes(121) returned the correct value\nTest 4 passed!\n')
        score3 += 1         
    print('Test 5: edge case')
    try:
        assert(_globals['my_primes'](2) == [2])
    except:
        print('my_primes(2) returned an incorrect value\nTest 5 failed!\n')
        pass
    else:
        print('my_primes(2) returned the correct value\nTest 5 passed!\n')
        score4 += 1         
    score = score0 + score1 + score2 + score3 + score4
    if score > 1:
        print(f"{score} marks out of 5")
        return score
    elif score == 1:
        print("1 mark out of 5")
        return score
    else: 
        raise AssertionError('Test failed!!')
        
# def bonus_q1(_globals):
#     A = [[1, 2, 3], [2, 1, 3]]
#     try:
#         assert(_globals['symCheck'](A) == 'not symmetric')
#         print('Test case passed!!!')
#     except:
#         print('Test case failed for {}'.format(A))



def bonus_q2(_globals):
    a = [3, 4]
    b = [24, 48]
    score = 0
    numTests = 2
    try:
        assert(_globals['setDiff'](a, b) == 2)
        score += 1
        print('Test case passed!!!')
    except:
        print('Test case failed for {}'.format(a, b))
    a = [2, 6]
    b = [24, 36]
    try:
        assert(_globals['setDiff'](a, b) == 2)
        score += 1
        print('Test case passed!!!')
    except:
        print('Test case failed for {}'.format(a, b))

    if score == numTests:
        print(f"All tests passed! {numTests} of {numTests} marks awarded!")
        return score
    elif score > 1:
        print(f'Some tests passed, {score} of {numTests} marks awarded!')
        return score
    else:
        raise AssertionError('Tests failed!!')
             
              