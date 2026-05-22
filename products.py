def add_product():
    product_id = input("Enter Product Id : ")
    product_name = input("Enter Product Name : ")
    product_price = input("Enter Product Price : ")
    product_stock = int(input("Enter Product Stock : "))
    product_exist = False
    try:
        with open("products.txt","r")as f:
            data = f.readlines()
            for i in data:
                parts = i.strip().split(" --> ")
                parts_id = parts[0]
                if product_id == parts_id:
                    product_exist = True
                    break
        if product_exist:
            print("Product Id Already Exist....")
        else:
            with open("products.txt" , "a") as f:
                data = f.write(f"{product_id} --> {product_name} --> {product_price} --> {product_stock}\n")
                print("Product Added Sucessfully...")
    except FileNotFoundError:
        print("File Not Found")    
def viewproducts():
    with open("products.txt","r") as f:
        data = f.readlines()
        print(".....................")
        print("These Are The Products")
        for i in data:
            parts = i.strip().split(" --> ")
            print(".....................")
            print("ID :", parts[0])
            print("Name :", parts[1])
            print("Price :", parts[2])
            print("Stock :", parts[3])
def searchproducts():
    products =input("Search : ")
    product_found = False
    try:
        with open("products.txt","r") as f:
            data =f.readlines()
        for i in data:
            parts =i.strip().split(" --> ")
            if products.lower() == parts[1].lower():
                product_found = True
                break
        if product_found:
            print("Results :-")
            print(i)
        else:
            print("Product Not Found")
    except FileNotFoundError:
        print("File Not Found")
