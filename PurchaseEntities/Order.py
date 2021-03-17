import datetime
from PurchaseEntities.Item import Item

class Order:

    def __init__(self, order_number):

        self.order_number = order_number
        self.order_date = datetime.datetime.now()

        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, sku):

        for i in self.items:
            if i.sku == sku:
                pass
                # delete the item here.

    def total_item_price_notax(self):

        total_price = 0.0

        for i in self.items:
            total_price = total_price + i.price

        return total_price
    #
    # def total_item_price_withtax(self):








