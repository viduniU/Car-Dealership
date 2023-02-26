# defining variables
users = ["admin", "owner", "technician"]
passwords = ["123", "123$", "abc#"]

print("Welcome to Kim's Cars")
remain_in_sys = 1
while remain_in_sys == 1:
    login = input("If you wish to login as a Guest; Press 'Y'\n If you already have an account press 'N' : ")
    if login == "N".lower():
        print("These are the available user names\nadmin\nowner\ntechnician")
        user1 = input("Enter user name : ")
        check = 1
        check1 = 1
        import sys

        while user1 not in users:
            check = check + 1
            print("Invalid User Name!\nPlease try again.")
            user1 = input("Enter User Name : ")
            if check > 2:
                print("Sorry! Please try later. ")
                sys.exit()

        password1 = input("Enter your Password : ")
        while password1 not in passwords:
            check1 = check1 + 1
            print("Invalid password!\nTry again.")
            password1 = input("Enter your password again : ")
            if check1 > 2:
                print("Sorry! Please try later. ")
                sys.exit()

        if password1 == "123":
            import Admin
            print(Admin)
        elif password1 == "123$":
            import Owner
            print(Owner)
        elif password1 == "abc#":
            import Technician
            print(Technician)
        else:
            print("invalid password")

    elif login == "y".lower():

        import Guest
        print(Guest)
    else:
        print("Invalid Input!")

    remain_in_sys = int(input("Do you want to return to the main menu, Enter 1 if so else enter 0 : "))
