class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name}, type: {self.store_type}")

    def open_shop(self):
        print(f"Online shop {self.shop_name} opened!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discounts_products(self):
        print(f"Products with discount: {self.discount_products}")

store = Shop("TechStore", "Electronics")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()

store1 = Shop("BookWorld", "Books")
store2 = Shop("FashionHub", "Clothes")
store3 = Shop("HomeGoods", "Household goods")
store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print(store.number_of_units)
store.number_of_units = 10
print(store.number_of_units)

store.set_number_of_units(25)
print(store.number_of_units)
store.increment_number_of_units(5)
print(store.number_of_units)

store_discount = Discount("SuperDeals", "All Products")
store_discount.discount_products = ["Laptop", "Phone", "Headphones"]
store_discount.get_discounts_products()
