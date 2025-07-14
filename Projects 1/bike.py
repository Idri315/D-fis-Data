# IMPORTS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load hourly data from the github repository of the book

hourly_data = pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Analysis-Workshop/master/Chapter01/Data/hourly_data.csv')

#print some generic statistics about the data

print(f"Shape of data: {hourly_data.shape}")
print(f"Number of missing value in the data: {hourly_data.isnull().sum().sum()}")
