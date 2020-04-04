"""
    You are the manager of a supermarket.
    You have a list of items together with their prices that consumers bought on a particular day.
    Your task is to print each item_name and net_price in order of its first occurrence.
    Take Input from user.
  Hint:
    item_name = Name of the item.
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Sample input:
    Banana Fries 12
    Potato Chips 30
    Apple Juice 10
    Candy 5
    Apple Juice 10
    Candy 5
    Candy 5
    Candy 5
    Potato Chips 30
  Sample output:
    Banana Fries 12
    Potato Chips 60
    Apple Juice 20
    Candy 20
"""
print("\nFollowing are the items available in the store:")
print("\nBanana Fries, Apple Juice, Candy, Potato Chips\n")

OrderedDict = {}

while True:
    entry = input("Enter item name, followed by a space and net price: ")
    if not entry:
        break
    list1 = entry.split()
    net_price = int(list1[-1])
    item_name = " ".join(list1[:-1])
    if item_name in OrderedDict:
        OrderedDict[item_name] += net_price
    else:
        OrderedDict[item_name] = net_price
print("\n", OrderedDict)
