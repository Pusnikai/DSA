"""
INFR-2080U Assignment 1
Prashanth B.Nallathamby 100784991
"""
import time

#Data Structure
#Data Structure to store the information of each Products
def Initial_product_data():
    products = []
    filename = "product_data.txt"
    with open(filename, 'r') as file:
        for line in file:
            productFile = line.strip().split(', ')
            products.append((int(productFile[0]), productFile[1], float(productFile[2]), productFile[3]))
    return products

#Function to display all the available products
def Show_Products(products):
    strProd = ""
    for product in products:
        strProd += "ID:" + str(product[0]) + " Name:" + product[1] + " Price:" + str(product[2]) + " Category:" + product[3] + "\n"
    return strProd

#Functions that search for the products based on ID or Name
def Search_Product(idORname, products):
    for i, product in enumerate(products):
        if isinstance(idORname, int) and product[0] == idORname:
            return i 
        elif isinstance(idORname, str) and product[1] == idORname:
            return f"ID:{product[0]} Name:{product[1]} Price:{product[2]} Category:{product[3]}\n"
    return None

#Function that insert new product into the array of products
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

#Function that updates the choosen product's attribute
def Update_Product(products, id, name, price, category):
    Location = int(Search_Product(id,products))
    products[Location] = (id,name,price,category)
    print("Products Updated\n")
    return products

#Function that removes a chosen product from the list
def Delete_Product(id, products):
    Location = int(Search_Product(id,products))
    products.pop(Location)
    print("Product Deleted\n")
    return products

#Sorting Algorithm (Bubble sort)
#Sorts based on ascending or descending
def Sort_Product(products, Order):
    start = time.time() #Start time of sorting
    for i in range(len(products)):
        for  j in range(0, len(products)-i-1):
            if Order == "Ascending":
                if  products[j][2] > products[j+1][2]:
                    products[j], products[j+1] = products[j+1], products[j]
            if Order == "Descending":
                if products[j][2] < products[j+1][2]:
                    products[j], products[j+1] = products[j+1], products[j]
    end = time.time() #End time of Sorting
    print("Sorting Time (seconds): ",end-start) #Print the time taken to sort for time complexity
    return products  

#Main Function that uses while loop for user interaction
def main():
    products = Initial_product_data()
    while True:
        
        action = input("\nInsert,Update,Delete,Search,Sort,Show or End?")
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
        elif action == "Delete":
            id = int(input("Enter the Product ID you Want to delete: "))
            products = Delete_Product(id, products)
        elif action == "Search":
            name = input("Enter the product name you are looking for: ")
            Search_Product(name, products)
        elif action == "Sort":
            order = input(f"Choose an order (Ascending/Descending): ")
            products = Sort_Product(products, order)
        elif action == "Show":
            print(Show_Products(products))
        else:
            print("Invalid Action! Please try again.\n")          
            
main()
    