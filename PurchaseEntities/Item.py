class Item:

    def __init__(self, sku, name, price=0.00, taxable=False):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable


