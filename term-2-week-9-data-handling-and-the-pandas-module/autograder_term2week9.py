import numpy.testing as npt
from time import time
import numpy as np
import pandas as pd
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
    try:
        assert(all(_globals['ser1'] == pd.Series(np.cos(np.linspace(0.0,2*np.pi,25)))))
    except:
        print("ser1 does not seem to be defined correctly")
    else:
        print("ser1 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        test_ser = pd.Series(np.cos(np.linspace(0.0,2*np.pi,25)))
        test_ser.index = np.linspace(0.0,2*np.pi,25)
        assert(all(_globals['ser1'] ==test_ser))
    except:
        print("ser1 does not seem to be defined correctly")
    else:
        print("ser1 is defined correctly")
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
        polyhedra = {'platonic': 5,'archimedean': 13,'catalan': 13,'johnson (simple)': 28,'johnson': 92,'kepler-poinsot': 4}
        assert(all(_globals['poly_ser'] == pd.Series(polyhedra)))
    except:
        print("poly_ser does not seem to be defined correctly")
    else:
        print("poly_ser is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1iia(_globals):
    number_of_tests = 1
    score = 0
    try:
        footballers_dict = {'Position':('goalkeeper','left back','centre half'), 'Name':('Aisha','Esme','Colin'), 'Age':(15,14,15)}
        assert(all(_globals['footballers_df'] == pd.DataFrame(footballers_dict)))
    except:
        print("footballers_df does not seem to be defined correctly")
    else:
        print("footballers_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1iib(_globals):
    number_of_tests = 1
    score = 0
    try:
        footballers_dict = {'Position':('goalkeeper','left back','centre half'), 'Name':('Aisha','Esme','Colin'), 'Age':(15,14,15)}
        footballers_df = pd.DataFrame(footballers_dict)
        footballers_df2 = footballers_df.set_index('Position')
        assert(all(_globals['footballers_df2'] == footballers_df2))
    except:
        print("footballers_df2 does not seem to be defined correctly")
    else:
        print("footballers_df2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question1iic(_globals):
    number_of_tests = 1
    score = 0
    try:
        footballers_dict = {'Position':('goalkeeper','left back','centre half'), 'Name':('Aisha','Esme','Colin'), 'Age':(15,14,15)}
        footballers_df = pd.DataFrame(footballers_dict)
        footballers_df2 = footballers_df.set_index('Position')
        footballers_df3 = footballers_df2.sort_values('Name')
        assert(all(_globals['footballers_df3'] == footballers_df3))
    except:
        print("footballers_df3 does not seem to be defined correctly")
    else:
        print("footballers_df3 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2a(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        assert(all(_globals['planet_df'] == planet_df))
    except:
        print("planet_df does not seem to be defined correctly")
    else:
        print("planet_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2b(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        planet_df2 = planet_df.sort_values('mass',ascending=False)
        assert(all(_globals['planet_df2'] == planet_df2))
    except:
        print("planet_df2 does not seem to be defined correctly")
    else:
        print("planet_df2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2c(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        escape_vel_ser = planet_df['escape_velocity']
        assert(all(_globals['escape_vel_ser'] == escape_vel_ser))
    except:
        print("escape_vel_ser does not seem to be defined correctly")
    else:
        print("escape_vel_ser is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2d(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        orbital_radius_list = [0.39, 0.72, 1.0, 1.5, 5.2, 9.5, 19.0, 30.0]
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        planet_df['orbital_radius'] = orbital_radius_list
        assert(all(_globals['planet_df'] == planet_df))
    except:
        print("planet_df does not seem to be defined correctly")
    else:
        print("planet_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2e(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        orbital_radius_list = [0.39, 0.72, 1.0, 1.5, 5.2, 9.5, 19.0, 30.0]
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        planet_df['orbital_radius'] = [1.5e08*x for x in orbital_radius_list]
        assert(all(_globals['planet_df'] == planet_df))
    except:
        print("planet_df does not seem to be defined correctly")
    else:
        print("planet_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2f(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(np.isclose(_globals['mass_rad_cov'],1.4745941249999998e+34))
    except:
        print("mass_rad_cov does not have the correct value")
    else:
        print("mass_rad_cov has the correct value")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')

def question2g(_globals):
    number_of_tests = 1
    score = 0
    try:
        assert(np.isclose(_globals['mass_rad_corr'],0.8666134506249494))
    except:
        print("mass_rad_corr does not have the correct value")
    else:
        print("mass_rad_corr has the correct value")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2h(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        orbital_radius_list = [0.39, 0.72, 1.0, 1.5, 5.2, 9.5, 19.0, 30.0]
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        planet_df['orbital_radius'] = [1.5e08*x for x in orbital_radius_list]
        planet_df_corr = planet_df.corr()
        assert(np.allclose(_globals['planet_df_corr'],planet_df_corr))
    except:
        print("planet_df_corr does not seem to be defined correctly")
    else:
        print("planet_df_corr is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question2j(_globals):
    number_of_tests = 1
    score = 0
    try:
        mercury_data = {'radius' : 2.4e6, 'mass' : 3.3e23, 'escape_velocity' : 4.3e3}
        venus_data = {'radius' : 6.1e6, 'mass' : 4.9e24, 'escape_velocity' : 1.0e4}
        earth_data = {'radius' : 6.3e6, 'mass' : 6.0e24, 'escape_velocity' : 1.1e4} 
        mars_data = {'radius' : 3.4e6, 'mass' : 6.4e23, 'escape_velocity' : 5.0e3}
        jupiter_data = {'radius' : 6.9e7, 'mass' : 1.9e27, 'escape_velocity' : 6.0e4}
        saturn_data = {'radius' : 5.7e7, 'mass' : 5.6e26, 'escape_velocity' : 3.6e4}
        uranus_data = {'radius' : 2.5e7, 'mass' : 8.7e25, 'escape_velocity' : 2.2e4}
        neptune_data = {'radius' : 2.5e7, 'mass' : 1.0e26, 'escape_velocity' : 2.4e4}
        planet_data = {'mercury': mercury_data, 'venus': venus_data, 'earth': earth_data,
                       'mars': mars_data, 'jupiter': jupiter_data, 'saturn': saturn_data,
                       'uranus': uranus_data, 'neptune': neptune_data}
        orbital_radius_list = [0.39, 0.72, 1.0, 1.5, 5.2, 9.5, 19.0, 30.0]
        planet_df = pd.DataFrame(planet_data).reindex(['escape_velocity','mass','radius']).transpose()
        planet_df['orbital_radius'] = [1.5e08*x for x in orbital_radius_list]
        planet_df_grouped = planet_df.groupby('radius')[['escape_velocity','mass']].mean()
        assert(np.allclose(_globals['planet_df_grouped'],planet_df_grouped))
    except:
        print("planet_df_grouped does not seem to be defined correctly")
    else:
        print("planet_df_grouped is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3ia(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df = pd.read_csv('historical_stock_market.csv')
        assert(all(_globals['stocks_df'] == stocks_df))
    except:
        print("stocks_df does not seem to be defined correctly")
    else:
        print("stocks_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3ib(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        assert(all(_globals['stocks_df2'] == stocks_df2))
    except:
        print("stocks_df2 does not seem to be defined correctly")
    else:
        print("stocks_df2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3ic(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        assert(all(_globals['stocks_df2'] == stocks_df2))
    except:
        print("stocks_df2 does not seem to be defined correctly")
    else:
        print("stocks_df2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3id(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_change = stocks_df2.pct_change().fillna(0)
        assert(all(_globals['stocks_change'] == stocks_change))
    except:
        print("stocks_change does not seem to be defined correctly")
    else:
        print("stocks_change is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3ie(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_rollingmeans = stocks_df2.rolling(3).mean()
        assert(all(_globals['stocks_rollingmeans'] == stocks_rollingmeans))
    except:
        print("stocks_rollingmeans does not seem to be defined correctly")
    else:
        print("stocks_rollingmeans is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3if(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_max = stocks_df2.cummax()
        assert(all(_globals['stocks_max'] == stocks_max))
    except:
        print("stocks_max does not seem to be defined correctly")
    else:
        print("stocks_max is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3ig(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_agg = stocks_df2.aggregate(['min','mean','max'])
        assert(all(_globals['stocks_agg'] == stocks_agg))
    except:
        print("stocks_agg does not seem to be defined correctly")
    else:
        print("stocks_agg is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iia(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_max = stocks_df2.cummax()
        stocks_max = stocks_max.rename(columns = lambda str: "Max "+str)
        assert(all(_globals['stocks_max'] == stocks_max))
    except:
        print("stocks_max does not seem to be defined correctly")
    else:
        print("stocks_max is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iib(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_max = stocks_df2.cummax()
        stocks_max = stocks_max.rename(columns = lambda str: "Max "+str)
        joined_df = pd.concat([stocks_df2,stocks_max],axis=1)
        assert(all(_globals['joined_df'] == joined_df))
    except:
        print("joined_df does not seem to be defined correctly")
    else:
        print("joined_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iic(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_df_monthly = stocks_df2.drop(stocks_df2.index[range(-4,0)]).resample('M').last()
        assert(all(_globals['stocks_df_monthly'] == stocks_df_monthly))
    except:
        print("stocks_df_monthly does not seem to be defined correctly")
    else:
        print("stocks_df_monthly is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iid(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_df_monthly2 = stocks_df2.drop(stocks_df2.index[range(-4,0)]).resample('M').apply(
            {'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Adj Close':'last', 'Volume':'sum'})
        assert(all(_globals['stocks_df_monthly2'] == stocks_df_monthly2))
    except:
        print("stocks_df_monthly2 does not seem to be defined correctly")
    else:
        print("stocks_df_monthly2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iie(_globals):
    number_of_tests = 1
    score = 0
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_fall = stocks_df2.query('Close<Open')
        assert(all(_globals['stocks_fall'] == stocks_fall))
    except:
        print("stocks_fall does not seem to be defined correctly")
    else:
        print("stocks_fall is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question3iif(_globals):
    number_of_tests = 1
    score = 0
    from copy import copy
    try:
        stocks_df2 = pd.read_csv('historical_stock_market.csv',index_col='Date')
        stocks_df2.index = pd.to_datetime(stocks_df2.index)
        stocks_df3 = copy(stocks_df2)
        stocks_df3['Rise/fall'] = stocks_df3['Close'] - stocks_df3['Open']
        assert(all(_globals['stocks_df3'] == stocks_df3))
    except:
        print("stocks_df3 does not seem to be defined correctly")
    else:
        print("stocks_df3 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4ia(_globals):
    number_of_tests = 1
    score = 0
    from copy import copy
    try:
        platonic_dict2 = {
            'name': ['tetrahedron', 
                     'cube', 
                     'octahedron', 
                     'dodecahedron', 
                     'icosahedron'], 
            'faces': [4, 6, 8, 12, 20],
            'vertices': [4, 8, 6, 20, 12],
            'edges': [6, 12, 12, 30, 30],
            'face shape': ['triangle',
                           'square',
                           'triangle',
                           'pentagon',
                           'triangle']
        }
        platonic_df = pd.DataFrame(platonic_dict2)
        platonic_pt0 = platonic_df.pivot_table(
            index = 'face shape',
            values = 'name',
            aggfunc = 'count'
        )
        assert(all(_globals['platonic_pt0'] == platonic_pt0))
    except:
        print("platonic_pt0 does not seem to be defined correctly")
    else:
        print("platonic_pt0 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4ib(_globals):
    number_of_tests = 1
    score = 0
    from copy import copy
    try:
        platonic_dict2 = {
            'name': ['tetrahedron', 
                     'cube', 
                     'octahedron', 
                     'dodecahedron', 
                     'icosahedron'], 
            'faces': [4, 6, 8, 12, 20],
            'vertices': [4, 8, 6, 20, 12],
            'edges': [6, 12, 12, 30, 30],
            'face shape': ['triangle',
                           'square',
                           'triangle',
                           'pentagon',
                           'triangle']
        }
        platonic_df = pd.DataFrame(platonic_dict2)
        platonic_pt1 = platonic_df.pivot_table(
            index = 'face shape',
            values = 'name',
            aggfunc = list
        )
        assert(all(_globals['platonic_pt1'] == platonic_pt1))
    except:
        print("platonic_pt1 does not seem to be defined correctly")
    else:
        print("platonic_pt1 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4ic(_globals):
    number_of_tests = 1
    score = 0
    from copy import copy
    try:
        platonic_dict2 = {
            'name': ['tetrahedron', 
                     'cube', 
                     'octahedron', 
                     'dodecahedron', 
                     'icosahedron'], 
            'faces': [4, 6, 8, 12, 20],
            'vertices': [4, 8, 6, 20, 12],
            'edges': [6, 12, 12, 30, 30],
            'face shape': ['triangle',
                           'square',
                           'triangle',
                           'pentagon',
                           'triangle']
        }
        platonic_df = pd.DataFrame(platonic_dict2)
        platonic_pt2 = platonic_df.pivot_table(
            index = 'face shape',
            values = 'faces',
            aggfunc = list
        )
        assert(all(_globals['platonic_pt2'] == platonic_pt2))
    except:
        print("platonic_pt2 does not seem to be defined correctly")
    else:
        print("platonic_pt2 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4iia(_globals):
    number_of_tests = 1
    score = 0
    try:
        trade_df = pd.read_csv('trade_data.csv')
        assert(all(_globals['trade_df'] == trade_df))
    except:
        print("trade_df does not seem to be defined correctly")
    else:
        print("trade_df is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4iib(_globals):
    number_of_tests = 1
    score = 0
    try:
        trade_df = pd.read_csv('trade_data.csv')
        trade_pt0 = trade_df.pivot_table(
            values = 'Value',
            index = 'Year',
            aggfunc = 'sum',
            columns = 'Measure'
        )
        assert(all(_globals['trade_pt0'] == trade_pt0))
    except:
        print("trade_pt0 does not seem to be defined correctly")
    else:
        print("trade_pt0 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')
        
def question4iic(_globals):
    number_of_tests = 1
    score = 0
    try:
        trade_df = pd.read_csv('trade_data.csv')
        trade_pt1 = trade_df.pivot_table(
            values = 'Value',
            index = 'Year',
            aggfunc = 'sum',
            columns = ['Commodity','Measure']
        )
        assert(all(_globals['trade_pt1'] == trade_pt1))
    except:
        print("trade_pt1 does not seem to be defined correctly")
    else:
        print("trade_pt1 is defined correctly")
        score += 1
    if score > 0:
        print('Test passed!')
        return score
    else: 
        raise AssertionError('Test failed overall!')