# with open("weather_data.csv") as data:
#     list=data.readlines()
#     print(list)

# import csv
# with open("weather_data.csv") as data:
#     list_data=csv.reader(data)
#     temperature=[]
#     for row in list_data:
#         if row[1]!='temp':
#             temp=row[1]
#             temperature.append(int(temp))
#     print(temperature)

import pandas
import pandas as pandas

# data=pandas.read_csv("weather_data.csv")
# # print(data)
# temp_list=data['temp'].to_list()
# total=0
# for temp in temp_list:
#     total+=temp
# avg_temp=total/len(temp_list)
# print(round(avg_temp))
# max_temp=data['temp'].max()
# print(max_temp)

# max_temp_row=data[data.temp==data.temp.max()]
# # print(max_temp_row)
# monday=data[data.day=='Monday']
# print(monday)
# name=[
#         ['Name','Tenzin','dolma','yeshi','tashi'],
#         [20,54,47,63,25]
#     ]
# name_list=pandas.DataFrame(name)
# print(name_list)
data=pandas.read_csv("squirrel_data.csv")
gray_squirrel=data[data["Primary Fur Color"]=='Gray']
gray_squirrel_count=len(gray_squirrel)
cinnamon_squirrel_count=len(data[data["Primary Fur Color"]=='Cinnamon'])
black_squirrel_count=len(data[data["Primary Fur Color"]=='Black'])

squirrel_count_dict={
   "Fur color":["Gray","Cinnamon",'Black'],
    "Count":[gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}
data_count_dict=pandas.DataFrame(squirrel_count_dict)
data_count_dict.to_csv("Squirrel Count.csv")