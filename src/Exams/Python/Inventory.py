from src.Exams.Python.Product import Product


class Inventory:
    def __init__(self, product_list):
        self.__product_list = product_list

    @property
    def product_list(self):
        return self.__product_list

    def __repr__(self):
        return 'Product list: {}'.format(self.__product_list)

    def sum_of_products(self):
        return sum([product.quantity for product in self.__product_list])

    def get_by_id(self, id):
        for product in self.__product_list:
            if product.id == id:
                return product
        return None


# Testing functions
prod1 = Product(15, 1243, 40)
prod2 = Product(54, 4325, 5)
prod3 = Product(5, 3682, 56)
list = [prod1, prod2, prod3]
invent = Inventory(list)
print(invent)
print(invent.sum_of_products())
print(invent.get_by_id(4325))
invent.product_list[0].buy(10)
print(invent)
