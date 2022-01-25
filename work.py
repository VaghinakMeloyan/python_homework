# Task_1

class Country:
    def __init__(self, name, continent, *args, **kwargs):
        self.name = name
        self.continent = continent
        super().__init__(*args, **kwargs)
    def present(self):
        return f"{self.name} and {self.continent}"

class Brand(Country):
    def __init__(self, brande_name, business_start_date, *args, **kwargs):
        self.brand_name = brande_name
        self.business_start_date = business_start_date
        super().__init__(*args, **kwargs)
    def present(self):
        return F"{self.brand_name} and {self.business_start_date}"


class Season(Country):
    def __init__(self, season_name, average_temperatur, *args, **kwargs):
        self.season_name = season_name
        self.average_temperatur = average_temperatur
        super().__init__(*args, **kwargs)
    def present(self):
        return f"{self.season_name} and {self.average_temperatur}"

class Product(Season, Brand):
    def __init__(self, pruduct_name, product_type, product_price, product_quantity, *args, **kwargs):
        self.product_name = pruduct_name
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity
        super().__init__(*args, **kwargs)

    def present(self):
        return f"presentetion of product will be {self.product_name, self.product_type, self.product_quantity}"

    def discount(self):
        return F"discount price with 20% will be {self.product_price - self.product_price * 20 / 100}"

    def increase(self):
        while True:
            self.product_quantity += 1
            print(self.product_quantity)

    def decrease(self):
        while self.product_quantity > 1:
            self.product_quantity -= 1
            print(self.product_quantity)


object_1 = Product("boots", "sport", 5000, 399, "Summer", 20, "Adidas", 2000, "Armenia", "Asia")

print(Product.__mro__)

print(object_1.present())
print(object_1.discount())
# print(object_1.increase())
print(object_1.decrease())