#  Design and Create an online store for Products(name, price).
# Track total products being created
#  Create a static method to calculate discount on each product based on a % parameter.

class Products:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.count += 1

    def get_info(self):  # instance method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price , discount):
        print(f"discountd price = {price - (discount * price / 100) }")

P1 = Products("Phone", 10_000)
P2 = Products("laptop", 50_000 )
P3 = Products("Pen", 10)


Products.get_count()
P1.calc_discount(P1.price, 12)