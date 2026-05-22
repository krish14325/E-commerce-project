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
    foundlist=[]
    product_found = False
    try:
        with open("products.txt","r") as f:
            data =f.readlines()
        for i in data:
            parts =i.strip().split(" --> ")
            if products.lower() in parts[1].lower():
                product_found = True
                if product_found == True:
                    foundlist.append(i)
                else:
                    pass
        if len(foundlist) !=0:
            for i in foundlist:
                new_parts = i.strip().split(" --> ")
                print("ID","-->",new_parts[0])
                print("Name","-->",new_parts[1])
                print("Price","-->",new_parts[2])
                print("Stock","-->",new_parts[3])
        else:
            print("No Product Found")
    except FileNotFoundError:
        print("File Not Found")
def updateproduct():
    products_id = input("Enter Product Id : ")
    new_updates = []
    product = False
    with open("products.txt","r") as f:
        data = f.readlines()
        for i in data:
            parts = i.strip().split(" --> ")
            if products_id == parts[0]:
                product = True
                print("......................")
                print(i)
                print("......................")
                new_id = input("Enter New Id :")
                new_name = input("Enter New Name :")
                new_price = input("Enter New Price :")
                new_stock = input("Enter New Stock :")
                new_updates.append(f"{new_id} --> {new_name} --> {new_price} --> {new_stock}\n")
            else:
                new_updates.append(i)
    if product:
        with open("products.txt","w") as f:
            data = f.writelines(new_updates)
        print("Product Updated Sucessfully")
    else:
        print("Product Not Found")
            

        
        
        
    
