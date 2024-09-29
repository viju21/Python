# Author: VS
# Script_name: Analyze_WeatherData_WithNumpy.py
# Description: This script will calculate various statistical metrics to analyze the weather patterns for that month.



#Importing the Libraries and creating the dataset
import numpy as np

#temperatures
temperatures = np.linspace(start = 25.0, stop = 40,num = 100 )+ np.random.normal(scale= 0.2, size= 100, loc= 0)

#print few values
print(temperatures[:10])

#Calculate the Mean, median, standard deviation, maximum, minimum temperatures
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
std_temp = np.std(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

#print those values
print(f"Mean Temperatures:{mean_temp:2f}c")
print(f"Median Temperatures:{median_temp:2f}c")
print(f"Standard Deviation Temperatures:{std_temp:2f}c")
print(f"Maximum Temperatures:{max_temp:2f}c")
print(f"Minimum Temperature:{min_temp:2f}c")

#Day-to-day temperature difference
diff_temp = np.diff(temperatures)

#Avg Fluctation of temperatures
avg_fluctuation = np.mean(np.abs(diff_temp))

print(f"Avg_Fluctuation:{avg_fluctuation:2f}c")

