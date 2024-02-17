import time

class Product:
    def  __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
#test 1
def main():
    products = []
    filename = "product_data.txt"
    with open(filename, 'r') as file:
        for line in file:
            productFile = line.strip().split(', ')
            products.append(Product(int(productFile[0]), productFile[1], float(productFile[2]), productFile[3]))
    
    print(products)

main()
    