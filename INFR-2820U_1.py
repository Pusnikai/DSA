import time

class Product:
    def  __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

def main():
   
    products = []
    filename = "product_data.txt"
    with open(filename, 'r') as file:
        for line in file:
            productFile = line.strip().split(', ')
    