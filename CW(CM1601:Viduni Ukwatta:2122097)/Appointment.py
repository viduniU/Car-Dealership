import pandas
import pandas as pd
import csv
while True:
    print("Entering Appointment Details")
    car_id = input("Car Id : ")
    date = input("Date : ")
    time = input("Time : ")
    contact = input("Contact No : ")
    list1 = [car_id, date, time, contact]
    print("%s\n", list1)

    option = input("Do you wish to Enter another Appointment, press 'y'\n otherwise press 'n' : ")
    if option == "n".lower():
        break
data_to_append = list1

file = open("Appointment.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow(data_to_append)
file.close()

file1 = pd.read_csv("Appointment.csv")
pandas.set_option('display.max_columns', 4)
print(file1)

