# CHALLENGE: Create a csv that's called squirrel_count that has a small table which just contains fur color and how many of each fur color there is
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = {
    "Fur Color": [],
    "Count": []
}

primary_fur = data["Primary Fur Color"]
color_list = []
for color in primary_fur:
    if color not in data_dict["Fur Color"]:
        data_dict["Fur Color"].append(color)
        index = data_dict["Fur Color"].index(color)
        data_dict["Count"].append(1)
    else:
        index = data_dict["Fur Color"].index(color)
        data_dict["Count"][index] += 1
        
print(data_dict)
