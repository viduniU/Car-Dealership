# importing modules
from pandas import *

data = read_csv("Sold Car Details .csv")

# converting column data to list
price = data['Price'].tolist()
selling_price = data['Selling Price'].tolist()
month = data['Sold Month'].tolist()
profit = []

profit_for_list = 0
for x in range(0, len(price)):
    profit_for_list = int(selling_price[x]) - int(price[x])
    profit.append(profit_for_list)

print("\n y-axis")
print("    ^")
for x in range(0, len(profit)):
    temp = profit[x]//100000
    print(month[x], "|", "#" * int(temp))

print("   ", "0", "-"*20, "> x-axis(# = 100000)")
