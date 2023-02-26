import pandas
import pandas as pd
import csv
while True:
    print("Entering Sold Car Details")
    car_id = input("Car ID : ")
    brand = input("Brand : ")
    model = input("Model : ")
    year = int(input("Year : "))
    name = input("Customer Name : ")
    number = int(input("Contact No : "))
    price = float(input("Price : LKR "))
    selling_price = float(input("Selling Price : LKR "))
    list1 = [car_id, brand, model, year, name, number, price, selling_price]
    print("%s\n", list1)

    option = input("Do you wish to Enter another car detail, press 'y'\n otherwise press 'n' : ")
    if option == "n".lower():
        break
data_to_append = list1

file = open("Sold Car Details .csv", "a", newline="")
writer = csv.writer(file)
writer.writerow(data_to_append)

file.close()
file1 = pd.read_csv("Sold Car Details .csv")
pandas.set_option('display.max_columns', 8)
print(file1)
