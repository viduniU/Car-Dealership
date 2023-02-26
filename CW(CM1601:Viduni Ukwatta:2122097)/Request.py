import pandas
import pandas as pd
import csv
while True:
    print("Entering Request Details")
    car_id = input("Car ID : ")
    description = input("Description : ")
    date = input("Date : ")
    list1 = [car_id, description, date]
    print("%s\n", list1)

    option = input("Do you wish to Enter another request, press 'y'\n otherwise press 'n' : ")
    if option == "n".lower():
        break
data_to_append = list1

file = open("Request.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow(data_to_append)
file.close()

file1 = pd.read_csv("Request.csv")
pandas.set_option('display.max_columns', 3)
print(file1)

