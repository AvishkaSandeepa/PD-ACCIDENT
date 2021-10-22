import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Crash-Statistics-Victoria.csv", usecols=[5,6,7,8,9,13,17,28])
df["NEWC"] = ""
print(df)