import pandas
import pandas as pd
import csv
while True:
    print("Entering Car Details")
    brand = input("Brand : ")
    model = input("Model : ")
    year = int(input("Year : "))
    name = input("Owner's Name : ")
    number = int(input("Contact No : "))
    mileage = int(input("Mileage : "))
    price = float(input("Price : LKR "))
    selling_price = float(input("Selling Price : LKR "))
    list1 = [brand, model, year, name, number, mileage, price, selling_price]
    print("%s\n", list1)

    option = input("Do you wish to Enter another car detail, press 'y'\n otherwise press 'n' : ")
    if option == "n".lower():
        break
data_to_append = list1

file = open("Kim's Cars .csv", "a", newline="")
writer = csv.writer(file)
writer.writerow(data_to_append)

file.close()

file = pd.read_csv("Kim's Cars .csv")
pandas.set_option('display.max_columns', 8)
print(file)
