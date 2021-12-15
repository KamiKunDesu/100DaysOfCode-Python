# with open("weather_data.csv") as weather:
#     weather_days = weather.readlines()
#     print(weather_days)

# import csv

# with open("weather_data.csv") as weather:
#     weather_days = csv.reader(weather)
#     temperatures = []
#     for count, row in enumerate(weather_days):
#         if count == 0:
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

color_count = {
    "colour": ["Gray", "Cinnamon", "Black"],
    "amount": [0, 0, 0]
}

for color in data["Primary Fur Color"]:
    if color == "Gray":
        color_count["amount"][0] += 1
    elif color == "Cinnamon":
        color_count["amount"][1] += 1
    elif color == "Black":
        color_count["amount"][2] += 1

final_data = pd.DataFrame(color_count)

final_data.to_csv("Squirrel_Color.csv", index=False)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(numpy.mean(temp_list))

# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])



# celsius = data[data.day=="Monday"].temp
# fahrenheit = float(celsius*1.8 + 32)

# print(f"The temperature in farenheight is: {fahrenheit}")