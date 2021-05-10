import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
Read_list = df["reading score"].tolist()

mean = statistics.mean(Read_list)
median = statistics.median(Read_list)
mode = statistics.mode(Read_list)
print("Mean, Median and Mode of Reading Score is {},{} and {} respectively".format(mean,median,mode))

stdev = statistics.stdev(Read_list)
print("Standard deviation of Reading Score is {}".format(stdev))

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (2*stdev)

list_of_data_within_one_stdev = [result for result in Read_list if result>first_stdev_start and result<first_stdev_end]
list_of_data_within_two_stdev = [result for result in Read_list if result>second_stdev_start and result<second_stdev_end]
list_of_data_within_three_stdev = [result for result in Read_list if result>third_stdev_start and result<third_stdev_end]

print("{}% of data for Reading scores lies within one standard deviation".format(len(list_of_data_within_one_stdev)*100.0/len(Read_list)))
print("{}% of data for Reading scores lies within two standard deviation".format(len(list_of_data_within_two_stdev)*100.0/len(Read_list)))
print("{}% of data for Reading scores lies within three standard deviation".format(len(list_of_data_within_three_stdev)*100.0/len(Read_list)))

