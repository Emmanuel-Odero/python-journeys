from abc import ABC, abstractmethod

class Product():
    name = ''
    quantities = 0
    cost = 0

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product : Product):
        pass
    @abstractmethod
    def get_all_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def edit_product(self, product_id):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass

class ProductManager(ProductAbstract):
    def create_product(self, product: Product):
        print("You created a product ")

    def get_all_product(self):
        print("Here are your products: ")

    def get_product_by_id(self, product_id):
        print("Your Products, id is: ", product_id)

    def edit_product_by_id(self, product_id):
        print("You have Edited the Product")

    def upload_product_image(self):
        print("Product Image Uploaded")

    def delete_product_by_id(self, product_id):
        print("Product Deleted")


first_product = Product()
first_product.name = "Iphone 13 Pro"
first_product.cost = 500
first_product.quantities = 1

product_manager = ProductManager()
product_manager.create_product(first_product)
product_manager.get_all_product()
product_manager.get_product_by_id(123)
product_manager.edit_product_by_id(1)
product_manager.upload_product_image()
product_manager.delete_product_by_id(1)