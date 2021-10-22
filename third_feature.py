import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def data_show():
    # read the input .csv file for processing purposes..you can choose columns as you wish............................
    df = pd.read_csv("CrashStatisticsVictoria.csv", usecols=[4,5,6,7,8,11,15,26])

    # take the input form user for filterout the given period.....................

    # ask for the date period with asking format..................................
    s_date = input("Enter starting date in format of yyyy-mm-dd : ")
    e_date = input("Enter Ending date in format of yyyy-mm-dd : ")
    # ask for the time period with asking format..................................
    s_time = input("Enter starting time in format hh.mm.ss : ")
    e_time = input("Enter ending time in format hh.mm.ss : ")

    # ask for the keyword for filter the data....................................
    k_word = input("Enter the keyword for the Accident(with correct format) : ")
    # convert the .csv time to timestamp format for easy access...................
    df['DATE'] = pd.to_datetime(df['ACCIDENT_DATE'])


    # filter out the selected range of dates......................................
    '''
    this takes upto end date. does not take end date.
    If you want to consider end date too.. simply change the '<' symbol with '<="
    '''
    filt = (df['DATE'] >= pd.to_datetime(s_date)) & (df['DATE'] < pd.to_datetime(e_date))
    # update the dataframe according to filtered dates............................
    df = df.loc[filt] 

    # filter out the selected range of time......................................
    filt = (df['ACCIDENT_TIME'] >=s_time) & (df['ACCIDENT_TIME'] < e_time)
    # update the dataframe according to filtered dates............................
    df = df.loc[filt]


    # remove the duplicate column................................................
    new_df = df.drop(columns='ACCIDENT_DATE' , axis=1)


    # keyword search.............................................................
    new_df = new_df[new_df['ACCIDENT_TYPE'].str.contains(k_word)]
   

    # view the resultant data table from this html page..........................
    new_df.to_html(
        'C:\\Users\\Avishka Sandeepa\\OneDrive - University of Moratuwa\\GitHub\\PD-ACCIDENT\\results_for_keyword.html')

'''
you have to call this function and give the inputs in correct(asked) order
then go to the same directory where your .py files located and open the html page to display the resultant chart.
**** makesure to change the directory of your html file with your own directory ****
'''

data_show()