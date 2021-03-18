from PurchaseEntities.Order import Item
from PurchaseEntities.Order import Order


item1 = Item(12345678, "Remote Control", 14.99, True)
item2 = Item(23456789, "Milk", 5.99, False)
item3 = Item(3456789, "Television", 799.99, True)

order1 = Order(1)

order1.add_item(item1)
order1.add_item(item2)
order1.add_item(item3)

print("The total amount of the order without tax is: ")
print(order1.total_item_price_notax())

print("The total amount of the order is: ")
print(order1.total_item_price_withtax())

print("Here is a receipt")
print(order1)





