def register():
    username = input("ENTER USERNAME : ").strip()
    password = input("ENTER PASSWORD : ").strip()
    user_exist = False
    with open ("users.txt" , "r") as f:
        data = f.readlines()
        for i in data:
            parts = i.strip().split(" ----> ")
            if len(parts) != 2:
                continue
            stored = parts[0]
            storedpass = parts[1]
            if username == stored and password == storedpass:
                user_exist = True
                break
    if user_exist:
        print("USER ALREADY EXIST")
    else:
        with open("users.txt","a") as f:
            f.write(f"{username} ----> {password}\n")
            print("USER REGISTERED SUCESSFULLY")
def login():
    Username = input("Enter Username : ").strip()
    Password = input("Enter Password : ").strip()
    user_exist = False
    try:
        with open("users.txt" , "r") as f:
            data = f.readlines()
            for i in data:
                parts = i.strip().split(" ----> ")
                if len(parts) != 2:
                    continue
                stored = parts[0]
                storedpass = parts[1]
                if Username == stored and Password == storedpass:
                    user_exist = True
                    break
    except FileNotFoundError:
        print("File Not Found")
    if user_exist:
        print("USER LOGIN SUCESSFULLY")
        return Username
    else:
        print("INVALID INFORMATION")
        return None


            