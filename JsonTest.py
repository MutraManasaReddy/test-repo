class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class ProductManeger:
    def __init__(self):
        self.products = []

    # Add a new product
    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added successfully!")

    # List all products
    def list_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("Product List:")
            for product in self.products:
                print(product)

    # Return a product by ID
    def return_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                print(f"Product found: {product}")
                return product
        print(f"Product with ID {product_id} not found.")
        return None

    # Update product details
    def update_product(self, product_id, name=None, price=None, quantity=None):
        product = self.return_product(product_id)
        if product:
            if name:
                product.name = name
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
            print(f"Product with ID {product_id} has been updated.")
        else:
            print(f"Product with ID {product_id} not found to update.")

    # Remove a product by ID
    def remove_product(self, product_id):
        product = self.return_product(product_id)
        if product:
            self.products.remove(product)
            print(f"Product with ID {product_id} has been removed.")
        else:
            print(f"Product with ID {product_id} not found to remove.")

    # Order products by a specific attribute 

    def order_products(self, attribute):
        if not self.products:
            print("No products to order.")
            return

        if attribute == 'price':
            self.products.sort(key=lambda x: x.price)
        elif attribute == 'name':
            self.products.sort(key=lambda x: x.name)
        elif attribute == 'quantity':
            self.products.sort(key=lambda x: x.quantity)
        else:
            print("Invalid attribute for ordering. Use 'price', 'name', or 'quantity'.")
            return

        print(f"Products ordered by {attribute}:")
        self.list_products()


if __name__ == "__main__":
    maneger = ProductManeger()

    # Adding products

    maneger.add_product(Product(1, "hairdryer", 500, 10))
    maneger.add_product(Product(2, "iPhone", 10000, 25))
    maneger.add_product(Product(3, "laptop", 10000, 35))

    # Listing all products

    maneger.list_products()

    # Returning a product by ID

    maneger.return_product(2)

    # Updating a product

    maneger.update_product(1, price=1200, quantity=8)

    # Removing a product

    maneger.remove_product(3)

    # Listing products after update and remove

    maneger.list_products()

    # Ordering products by price

    maneger.order_products('price')

    # Ordering products by name

    maneger.order_products('name')