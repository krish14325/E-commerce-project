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
