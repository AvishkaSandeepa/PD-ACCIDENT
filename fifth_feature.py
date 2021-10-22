import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_prepocessing():
    # read the input .csv file for processing purposes..you can choose columns as you wish............................
    df = pd.read_csv("CrashStatisticsVictoria.csv", usecols=[4,5,6,7,8,11,15,26])

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

    return s_date, e_date, s_time, e_time, df


def plot_speed():
    # assign the variables using previous function................................
    s_date, e_date, s_time, e_time, df = data_prepocessing()

    # defining lists..............................................................
    lst = ['10 km/hr','20 km/hr','30 km/hr','40 km/hr','50 km/hr','60 km/hr','70 km/hr','80 km/hr','90 km/hr','100 km/hr',]
    

    # define a list to store selected average accidents...........................
    accidents = []


    #.............calculate the average accidents for given period................
    for i in lst:
        
        # check the number of accidents for given speed and add them to list
        new_df = df[df['SPEED_ZONE'].str.contains(i)]
        
        accidents.append(new_df.shape[0])

    #plot the bar chart..........................................................
    fig, axes = plt.subplots(1,1, figsize = (15,10))
    plt.bar(lst,accidents)
    plt.plot(lst, accidents, "r_")
    plt.xlabel("SPEEDS")
    plt.ylabel("NO OF ACCIDENTS")
    plt.title("Number of Accidents in each Speed zone")
    plt.show()


'''

you have to call this function and give the inputs in correct(asked) order


'''

plot_speed()