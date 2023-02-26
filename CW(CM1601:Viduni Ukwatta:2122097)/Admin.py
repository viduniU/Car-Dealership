import pandas
import pandas as pd
remain_in_sys = 1
while remain_in_sys == 1:
    print("Data Entering Options:\n *Sold Car Details\n *New Car Details\n*Check Requests")
    option = input("If you want to add new car details press y\nSold Car Details press n\nTo check requests press "
                   "1\nEnter your option : ")
    if option == "y".lower():
        import new_cars
        print(new_cars)
    elif option == "n".lower():
        import sold_cars
        print(sold_cars)
    elif option == "1":
        file1 = pd.read_csv("Request.csv")
        pandas.set_option('display.max_columns', 3)
        print(file1)
        q = input("Do you want to enter data (yes/no) : ")
        if q == "yes".lower():
            import Appointment
            print(Appointment)
        else:
            print("No appointments")

    else:
        print("Invalid Input!")
    remain_in_sys = int(input("Do you want to return to the main menu, Enter 1 if so else enter 0 : "))
