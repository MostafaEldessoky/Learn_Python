import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# data_list = data["temp"].to_list()
# print(sum(data_list) / len(data_list))
# print(int(data[data.day == "Monday"]["temp"]) * 9 / 5 + 32)


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
x1 = len(data[data["Primary Fur Color"] == "Gray"])
x2 = len(data[data["Primary Fur Color"] == "Black"])
x3 = len(data[data["Primary Fur Color"] == "Cinnamon"])
dic = {"Primary Fur Color": ["Gray", "Black", "Cinnamon"],
       "Number": [x1, x2, x3]
       }
dic = pd.DataFrame(dic)
dic.to_csv("dic.csv")
