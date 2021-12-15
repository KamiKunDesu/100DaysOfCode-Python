sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Make a dictionary of the length of each word in the above sentence
# Write your code below:
result = {word:len(word) for word in sentence.split()}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Take the dictionary above and create a new dictionary of temperatures in fahrenheit
# Write your code 👇 below:
weather_f = {day:round((value*1.8)+32 ,2) for day, value in weather_c.items()}


print(weather_f)