# #import csv
# # with open('weather_data.csv') as csvfile:
# #     data = csv.reader(csvfile)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(row[1])
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #data_dict  = data.to_dict()
# temp_list = data["temp"].to_list()
# # print(temp_list)
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# # print(data[data.day == "Monday"])
# # print(data["temp"].max())
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(data[data.temp == data.temp.max()])
#
#
# #Create a data frame from scratch
# data_dict = {
#     "students ":["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("Squirrel_Data.csv")

cinnamon_squirrels_cinnamon  = len(data[data["Primary Fur Color"] == "Cinnamon"])
cinnamon_squirrels_black  = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_gray  = len(data[data["Primary Fur Color"] == "Gray"])

print(cinnamon_squirrels_cinnamon)
print(cinnamon_squirrels_black)
print(cinnamon_squirrels_gray)


data_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count":[cinnamon_squirrels_gray,cinnamon_squirrels_cinnamon,cinnamon_squirrels_black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("ColorCount.csv")