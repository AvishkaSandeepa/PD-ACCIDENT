import pandas as pd
df = pd.read_csv("Crash-Statistics-Victoria.csv",usecols=[4,5,6,7,8])

df = df.sort_values(by="ACCIDENT_DATE")
print(df['ACCIDENT_DATE'])