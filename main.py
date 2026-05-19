from users import register
from users import login
from products import viewproducts
from cart import add_to_cart
from cart import viewcart
from cart import totalbill
from cart import removeproduct
while True:
    print("1.Register\n2.Login\n3.Exit")
    choice =input("Enter Option : ")
    if choice == "1":
        register()
    elif choice == "2":
        current_user = login()
        if current_user:
            while True:
                print(",,,,,,,,,,,,,,,,,,,,,,")
                print(f"Hello {current_user}")
                print("........MENU.......")
                print("1.View Products\n2.Add To Cart\n3.Remove From Cart\n4.View Cart\n5.Total Bill\n6.Log Out")
                choice = input("Enter Option : ")
                if choice == "1":
                    viewproducts()
                elif choice == "2":
                    add_to_cart(current_user)
                elif choice == "3":
                    with open(f"{current_user}_user.txt" , "r") as f:
                        data = f.read()
                    if len(data) == 0:
                        print("No products Here To Remove")
                    else:
                        removeproduct(current_user)
                elif choice == "4":
                    viewcart(current_user)
                elif choice == "5":
                    totalbill(current_user)
                elif choice == "6":
                    print("Log Out Sucessfully")
                    break
    elif choice == "3":
        print("Exiting.....")
        break
    else:
        print("INVALID INPUT")  
