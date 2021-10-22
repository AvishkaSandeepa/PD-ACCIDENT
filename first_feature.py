import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_show():
    # read the input .csv file for processing purposes............................
    df = pd.read_csv("Crash-Statistics-Victoria.csv",usecols=[5,6,7,8,9,13,17,28])

    # take the input form user for filterout the given period.....................

    # ask for the date period with asking format..................................
    s_date = input("Enter starting date in format of yyyy-mm-dd : ")
    e_date = input("Enter Ending date in format of yyyy-mm-dd : ")
    # ask for the time period with asking format..................................
    s_time = input("Enter starting time in format hh.mm.ss : ")
    e_time = input("Enter ending time in format hh.mm.ss : ")

    # convert the .csv time to timestamp format for easy access...................
    df['DATE'] = pd.to_datetime(df['ACCIDENT_DATE'])


    # filter out the selected range of dates......................................
    filt = (df['DATE'] >= pd.to_datetime(s_date)) & (df['DATE'] < pd.to_datetime(e_date))
    # update the dataframe according to filtered dates............................
    df = df.loc[filt] 

    # filter out the selected range of time......................................
    filt = (df['ACCIDENT_TIME'] >=s_time) & (df['ACCIDENT_TIME'] < e_time)
    # update the dataframe according to filtered dates............................
    df.loc[filt]

    # remove the duplicate column................................................
    new_df = df.drop(columns='ACCIDENT_DATE' , axis=1)
    

    # view the resultant data table from this html page..........................
    new_df.to_html('C:\\Users\\Avishka Sandeepa\\OneDrive - University of Moratuwa\\GitHub\\PD-ACCIDENT\\accident_results_over_period.html')



'''

you have to call this function and give the inputs in correct(asked) order
then go to the same directory where your .py files located and open the html page to display the resultant chart.

**** makesure to change the directory of your html file with your own directory ****

'''

data_show()