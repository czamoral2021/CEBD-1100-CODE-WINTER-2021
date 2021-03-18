class Item:

    def __init__(self, sku, name, price=0.00, taxable=False):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def __str__(self):
        tax_text = " "

        if self.taxable:
            tax_text = "(taxable)"
        else:
            tax_text = "(non-taxable)"

        return str(self.sku) + "    " + self.name + "    " + str(self.price)