import csv

remain_in_sys = 1
while remain_in_sys == 1:
    while True:
        print("Entering Service Details")
        car_id = input("Car ID : ")
        owners_name = input("Owner's Name : ")
        contact = int(input("Contact No : "))
        date = input("Date (DD/MM/YYYY) : ")
        time = (input("Time (am/pm) : "))
        price = int(input("Price : "))

        list2 = [car_id, owners_name, contact, date, time, price]
        print("%s\n", list2)

        option = input("Do you wish to Enter another service detail, press 'y'\n otherwise press 'n' : ")
        if option == "n".lower():
            break
    data_to_append = list2

    file = open("Service Details.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow(data_to_append)
    file.close()
    
    remain_in_sys = int(input("Do you want to return to the main menu, Enter 1 if so else enter 0 : "))
