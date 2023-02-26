import pandas
import pandas as pd
remain_in_sys = 1
while remain_in_sys == 1:
    file1 = pd.read_csv("Kim's Cars .csv")
    file1 = file1.iloc[:, [0, 1, 2, 3, 4, 5, 7]]
    pandas.set_option('display.max_columns', 7)

    Question = input("Do you want to see our available cars? (yes/no) : ")
    if Question == "yes".lower():
        print(file1)
    elif Question == "no".lower():
        print("Thank you for visiting our page! Have a nice day")
    else:
        print("Invalid Input!")
    question2 = input("Do you want to request an appointment (yes/no): ")
    if question2 == "yes".lower():
        import Request
        print(Request)
    else:
        print("Have a nice day!")

        remain_in_sys = int(input("Do you want to return to the main menu, Enter 1 if so else enter 0 : "))
