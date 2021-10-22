import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Crash-Statistics-Victoria.csv",usecols=[4,5,6,7,8,12,16,27])

s_date = input("Enter starting date in format of yyyy-mm-dd : ")
e_date = input("Enter Ending date in format of yyyy-mm-dd : ")

s_time = input("Enter starting time in format hh.mm.ss : ")
e_time = input("Enter ending time in format hh.mm.ss : ")

k = df['DATE'][0]

df['DATE'] = pd.to_datetime(df['ACCIDENT_DATE'])

filt = (df['DATE'] >= pd.to_datetime(s_date)) & (df['DATE'] < pd.to_datetime(e_date))
df = df.loc[filt]
filt = (df['ACCIDENT_TIME'] >=s_time) & (df['ACCIDENT_TIME'] < e_time)
df.loc[filt]

#pd.to_timedelta(10.00, unit="h")

new_df = df.drop(columns='ACCIDENT_DATE' , axis=1)
new_df.to_html('C:\\Users\\Avishka Sandeepa\\OneDrive - University of Moratuwa\\GitHub\\PD-ACCIDENT\\my.html')

no_of_injured_person = df['INJ_OR_FATAL']

fig, axes = plt.subplots(1,1, figsize = (30,25))
plt.plot(no_of_injured_person)
plt.show()