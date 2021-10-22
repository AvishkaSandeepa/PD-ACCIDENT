import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def analysis_of_alcoholic_effect():
    df = pd.read_csv("CrashStatisticsVictoria.csv", usecols=[4,5,6,7,8,11,15,26])
    #alchoholic search
    df = df[df['ALCOHOLTIME'].str.contains(r'Y(?!$)')]

    val = int(input("Enter the analysing method..| trends over time --> type 0 | for accident types involving alchohol --> type 1 : "))

    ##################################################################################
    if val == 1:
            
        # for accident types involving alchohol
        c = df["ACCIDENT_TYPE"].value_counts().plot(kind='barh')
        plt.show()
        
    ##################################################################################

    elif val == 0:

        # defining lists..............................................................
        lst = ['00.00.00', '01.00.00', '02.00.00', '03.00.00', '04.00.00', '05.00.00', '06.00.00', '07.00.00', '08.00.00', '09.00.00', '10.00.00', '11.00.00', '12.00.00', '13.00.00', '14.00.00', '15.00.00', '16.00.00', '17.00.00', '18.00.00', '19.00.00', '20.00.00', '21.00.00', '22.00.00', '23.00.00', '24.00.00']
        lstNew = ['00-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24']
        # defining selection range indexes............................................
        

        # define a list to store selected average accidents...........................
        accidents = []


        #.............calculate the average accidents for given period................
        for i in range(0, len(lst)-1):
            timeperiod = (df['ACCIDENT_TIME'] >=lst[i]) & (df['ACCIDENT_TIME'] < lst[i+1])
            dk = df.loc[timeperiod]
            
            
            accidents.append(dk.shape[0])

        # plot the bar chart..........................................................
        fig, axes = plt.subplots(1,1, figsize = (15,10))
        plt.bar(lstNew,accidents)
        plt.plot(lstNew, accidents, "r_")
        plt.xlabel("HOURS")
        plt.ylabel("AVERAGE ACCIDENTS DUE TO ALCHOHOL")
        plt.title("Number of Accidents in each hour of the day due to alchohol")
        plt.show()

    ##################################################################################

    else:
        print("Invalid input. Please check the user manual")
analysis_of_alcoholic_effect()

'''
you must enter the correct value (0 or 1). according to your need
'''