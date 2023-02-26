# importing modules
from pandas import *

data = read_csv("income.csv")

# converting column data to list

profit = data['profit'].tolist()
service_charges = data['Service Charges'].tolist()
month = data['Month'].tolist()
income = []

income_for_list = 0
for x in range(0, len(profit)):
    income_for_list = int(service_charges[x]) + int(profit[x])
    income.append(income_for_list)

print("\n y-axis")
print("    ^")
for x in range(0, len(income)):
    temp = income[x]//50000
    print(month[x], "|", "@" * int(temp))

print("   ", "0", "-"*20, "> x-axis(@ = 50000)")
