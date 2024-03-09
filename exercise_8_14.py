# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Arbitrary parameters in Functions, including keyword ones.
# -----------------------------------------------------------------------------
# Exercise 8-14:
# 3a. Write a function that stores information about a car in a dictionary.
# 3a.1. The function should always receive a manufacturer and a model name.
# 3a.2.  It should then accept an arbitrary number of keyword arguments.
# 3a.3. Call the function with the required information
# 3a.2a. and two other name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 3a. 4.: Print the dictionary that’s returned to make sure all the information was stored correctly.

# -----------------------------------------------------------------------------
from icecream import ic

# -----------------------------------------------------------------------------
print("\n\nExercises 8-14:\n-------------------------------------------------")


def car_info(manufacturer, model, **car_details):  # 3a. & 3a.2.
    car_details["manufacturer"] = manufacturer  # 3a.1.
    car_details["model"] = model
    return car_details


car_1 = car_info("hyundai", "civic", color="teal", wifi=True)  # 3a.3. & 3a.2a

for key, value in car_1.items():  # 3a. 4
    # Changing True of Wifi argument to 'Yes'
    if value == True:
        value = "Yes"
        print(f"{key.title()}: {value}\n")
    else:
        print(f"{key.title()}: {value.title()}\n")
