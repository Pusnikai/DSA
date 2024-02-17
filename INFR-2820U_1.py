import time

def Initial_product_data():
    """Returns a dictionary containing the name and price of an item"""
    products = []
    filename = "product_data.txt"
    with open(filename, 'r') as file:
        for line in file:
            productFile = line.strip().split(', ')
            products.append((int(productFile[0]), productFile[1], float(productFile[2]), productFile[3]))
    return products

def Show_Products(products):
    strProd = ""
    for product in products:
        strProd += "ID:" + str(product[0]) + " Name:" + product[1] + " Price:" + str(product[2]) + " Category:" + product[3] + "\n"
    return strProd

def Search_Product(idORname, products):
    for i, product in enumerate(products):
        if isinstance(idORname, int) and product[0] == idORname:
            return i 
        elif isinstance(idORname, str) and product[1] == idORname:
            return f"ID:{product[0]} Name:{product[1]} Price:{product[2]} Category:{product[3]}\n"
    return None

def Insert_Product(products, id, name, price, category):
    Condition = True
    for product in products:
        if product[0] == id:
            print("Product ID Already Exists\n")
            Condition = False
            break
    if Condition:
        products.append( (id,name,price,category) )
        print("Product Succesfully  Added\n")
    return  products

def Update_Product(products, id, name, price, category):
    Location = int(Search_Product(id,products))
    products[Location] = (id,name,price,category)
    print(products[Location])
    return products
  
def main():
    #print(Show_Products(Initial_product_data()))  
    products = Initial_product_data()
    while True:
        print("Insert,Update,Delete,Search, or End?")
        action = input()
        if action == "End":
            break
        elif action == "Insert":
            id = int(input("Enter the product ID: "))
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            category = input("Enter the product category: ")
            products = Insert_Product(products, id, name, price, category)
        elif action == "Update":
            id = int(input("Enter the product ID you want to update: "))
            name = input("Enter the New Name: ")
            price = float(input("Enter the new Price: "))
            category = input("Enter the new Category: ")
            products = Update_Product(products, id, name, price, category)
        else:
            pass
    

main()
    