def add_to_cart(current_user):
    add = input("Enter Product Id : ")
    Quantity = int(input("Enter Quantity : "))
    product_exist = False
    purchase_successful = False
    with open("products.txt", "r") as f:
        data = f.readlines()
    updated_products = []
    for i in data:
        parts = i.strip().split(" --> ")
        product_id = parts[0]
        product_name = parts[1]
        product_price = parts[2]
        product_stock = int(parts[3])
        if add == product_id:
            product_exist = True
            cart_product_id = product_id
            cart_product_name = product_name
            cart_product_price = product_price
            if Quantity <= product_stock:
                new_stock = product_stock - Quantity
                updated_line = (
                    f"{product_id} --> "
                    f"{product_name} --> "
                    f"{product_price} --> "
                    f"{new_stock}\n"
                )
                updated_products.append(updated_line)
                purchase_successful = True
            else:
                print("Insufficient Stock")
                updated_products.append(i)
        else:
            updated_products.append(i)
    if purchase_successful:
        with open("products.txt", "w") as f:
            f.writelines(updated_products)
        with open(f"{current_user}_user.txt", "a") as f:
            f.write(
                f"{cart_product_id} --> "
                f"{cart_product_name} --> "
                f"{cart_product_price} --> "
                f"{Quantity}\n"
            )
        print("Product Added Successfully...")
    elif not product_exist:
        print("Product Not Found")
def viewcart(current_user):
    try:
        with open(f"{current_user}_user.txt","r") as f:
            data = f.readlines()
            print("..................................")
            print("These Are The Items In Your Cart")
            print("..................................")
            for i in data:
                parts = i.strip().split(" --> ")
                part_id = parts[0]
                part_name = parts[1]
                part_price = parts[2]
                part_quantity = parts[3]
                print("ID :",part_id)
                print("Name :",part_name)
                print("Price :",part_price)
                print("Quantity :",part_quantity)
                print("..................................")
            print("Cart Finished")
    except FileNotFoundError:
        print("File Not Found")
def totalbill(current_user):
    total_bill = 0
    with open(f"{current_user}_user.txt","r")as f:
        data = f.readlines()
        for i in data:
            parts = i.strip().split(" --> ")
            parts_price = int(parts[2])
            parts_Quantity = int(parts[3])
            bill = (parts_price*parts_Quantity)
            total_bill += bill
        print("Your Total Bill Was :",total_bill)
def removeproduct(current_user):
    newlist = []
    try:
        with open(f"{current_user}_user.txt","r")as f:
            data = f.readlines()
            print("..................................")
            print("Which Product Do You Want To Remove")
            print("...................................")
            for i in data:
                print(i)
            choice = input("Enter Product Id :" )
            with open(f"{current_user}_user.txt","r") as f:
                data = f.readlines()
                for i in data:
                    parts = i.strip().split(" --> ")
                    parts_id = parts[0]
                    parts_name = parts[1]
                    parts_price = parts[2]
                    parts_Quantity = int(parts[3])
                    if choice == parts_id:
                        products_list =[]
                        with open("products.txt","r") as f:
                            data = f.readlines()
                            for i in data:
                                parts = i.strip().split(" --> ")
                                parts_id = parts[0]
                                parts_name = parts[1]
                                parts_price = parts[2]
                                parts_stock = (int(parts[3]))
                                if choice == parts_id:
                                    return_stock = parts_Quantity + parts_stock
                                    products_list.append(f"{parts_id} --> {parts_name} --> {parts_price} --> {return_stock}\n")
                                else:
                                    products_list.append(f"{parts_id} --> {parts_name} --> {parts_price} --> {parts_stock}\n")
                        with open("products.txt" , "w") as f:
                            f.writelines(products_list)
                            continue
                    else:
                        newlist.append(f"{parts_id} --> {parts_name} --> {parts_price} --> {parts_Quantity}\n")
            with open(f"{current_user}_user.txt","w") as f:
                f.writelines(newlist)
    except FileNotFoundError:
        print("File Not Found")

        
                     
                     
             

