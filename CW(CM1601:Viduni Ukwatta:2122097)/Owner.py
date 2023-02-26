import pandas
import pandas as pd
remain_in_sys = 1
while remain_in_sys == 1:
    option = input("New Cars-->1\nSold Cars-->2\nService Details-->3\nView Report-->4\nSelect option : ")
    if option == "1":
        file2 = pd.read_csv("Kim's Cars .csv")
        pandas.set_option('display.max_column', 8)

        print(file2)

    elif option == "2":
        file3 = pd.read_csv("Sold Car Details .csv")
        pandas.set_option('display.max_column', 7)

        print(file3)

    elif option == "3":
        file4 = pd.read_csv("Service Details.csv")
        pandas.set_option('display.max_column', 6)

        print(file4)

    elif option == "4":
        question = input("If you want view profit report, press-->1\nIf you want to view Income graph press-->2\n "
                         "Please enter your option : ")
        if question == "1":
            import report
            print(report)
        elif question == "2":
            import income
            print(income)
        else:
            print("Invalid Option!")

    else:
        print("Invalid option")
    remain_in_sys = int(input("Do you want to return to the main menu, Enter 1 if so else enter 0 : "))
