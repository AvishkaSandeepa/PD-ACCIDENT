import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_prepocessing():
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

    return s_date, e_date, s_time, e_time, df


def accident_avg():
    # assign the variables using previous function................................
    s_date, e_date, s_time, e_time, df = data_prepocessing()

    # defining lists..............................................................
    lst = ['00.00.00', '01.00.00', '02.00.00', '03.00.00', '04.00.00', '05.00.00', '06.00.00', '07.00.00', '08.00.00', '09.00.00', '10.00.00', '11.00.00', '12.00.00', '13.00.00', '14.00.00', '15.00.00', '16.00.00', '17.00.00', '18.00.00', '19.00.00', '20.00.00', '21.00.00', '22.00.00', '23.00.00', '24.00.00']
    lstNew = ['00,-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24']
    # defining selection range indexes............................................
    in1 = lst.index(s_time)
    in2 = lst.index(e_time)

    #...................Recreate the lists according to selection.................
    lstN = []
    if in2 < len(lst)-1:
        lstN = lstNew[in1:in2]

    elif in2 == len(lst)-1:
        lstN = lstNew[in1:]
    length = len(lst)

    # define a list to store selected average accidents...........................
    accidents = []

    #.........................define the date difference..........................
    t1 = pd.to_datetime(s_date)
    t2 = pd.to_datetime(e_date)
    # convert the data output to integer..........................................
    difference = int(pd.Timedelta(t2-t1).days)


    #.............calculate the average accidents for given period................
    for i in range(in1, in2):
        timeperiod = (df['ACCIDENT_TIME'] >=lst[i]) & (df['ACCIDENT_TIME'] < lst[i+1])
        dk = df.loc[timeperiod]
        timeperiod = (df['ACCIDENT_TIME'] >=lst[i]) & (df['ACCIDENT_TIME'] < lst[i+1])
        
        accidents.append(dk.shape[0]/difference)

    # plot the bar chart..........................................................
    fig, axes = plt.subplots(1,1, figsize = (15,10))
    plt.bar(lstN,accidents)
    plt.plot(lstN, accidents, "r_")
    plt.xlabel("HOURS")
    plt.ylabel("AVERAGE ACCIDENTS")
    plt.title("Number of Accidents in each hour of the day (on average)")
    plt.show()


accident_avg()