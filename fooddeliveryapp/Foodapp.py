
import json
import datetime

def register_user(user_json, name, password, age, phn):
    user = {
        "id": 1,
        "name": name,
        "password": password,
        "age": age,
        "phone number": phn,
        "order history": {}
        # {"22-04-2022":["Vegan Burger (1 Piece)"],"22-04-2022":["Tandoori Chicken (4 pieces)"]}
    }
    try:
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "User already Exists"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except json.JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return '''Registration succesfull,
              Welcome to Food Delivery App'''

def update_profile(user_json, user_id, name, age, phn):
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            content[i]["name"] = name
            content[i]["age"] = age
            content[i]["phone number"] = phn
            return "Update Succesful"
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

def user_order_history(user_json, user_id):
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            print("Order History")
            print("Date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    file.close()
    return False

def user_place_order(user_json, food_json, user_id, food_name, quantity):
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    file = open(user_json, "r+")
    content = json.load(file)
    file1 = open(food_json, "r+")
    content1 = json.load(file1)
    for i in range(len(content1)):
        if content1[i]["name"] == food_name:
            if content1[i]["no of plates"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["no of plates"]-=quantity
                        if date not in content[j]["order history"]:
                            content[j]["order history"][date] = [content1[i]["name"]]
                        else:
                            content[j]["order history"][date].append(content1[i]["name"])
            else:
                print("Pls Enter less quantity")
                break    
        else:
            print("Food Not Available")
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    
    file1.seek(0)
    file1.truncate()
    json.dump(data, file1, indent=4)
    file1.close()

def add_food(food_json, food_name, price, discount ,no_plates=1):
    food = {
        "id":1,
        "name": food_name,
        "no of plates": no_plates,
        "Price of Food": price,
        "Discount": discount
    }
    try:
        fp = open(food_json, "r+")
        content = json.load(fp)
        for i in range(len(content)):
            if content[i]["name"] == food_name:
                fp.close()
                return "Food Already Available"
        food["id"]=len(content)+1
        content.append(food)
    except json.JSONDecodeError:
        content = []
        content.append(food)
    fp.seek(0)
    fp.truncate()
    json.dump(content, fp, indent=4)
    fp.close()
    return "Success"

def update_food(food_json, food_id, price, discount, no_plates=1):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["price of food"] = price
            content[i]["Discount"] = discount
            content[i]["no of plates"] += no_plates
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

def remove_food(food_json, food_id):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "success"
    return "Pls Enter Valid ID"

def read_food(food_json):
    file = open(food_json)
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print("Id: ", content[i]["id"])
        print(f"---> Name: {content[i]['name']}")
        print(f"---> Number of Plates: {content[i]['no of plates']}")
        print(f"---> Price: {content[i]['Price of Food']}")
        print(f"---> Discount: {content[i]['Discount']}")   
    file.close()
    return True
    
val = input('''Welcome to food delivery App ,
               Do you want to order food y/n:''')
while val.lower() == "y":
    print("Menu: ")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1 = str(input("Kindly select one option from the above: "))
    if val1 == "1":
        print()
        name = input("Enter the name: ")
        password = input("Enter the password: ")
        age = int(input("Enter your Age"))
        phn = input("Enter the Phn number")
        register_user("user.json", name, password, age, phn)
        
    elif val1 == "2":
        print()
        while True:
            print("1) User")
            print("2) Admin")
            print("3) Exit")
            val2 = str(input("Kindly select one option from the above: "))
            if val2 == "1":
                print("   USER   ")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("user.json", "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == user:
                        if content[i]["password"] == password:
                            while True:
                                print()
                                print("1) View Menu")
                                print("2) Place New Order")
                                print("3) Show History of order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val4 = str(input("Kindly Enter your choice!! "))
                                if val4 == "1":
                                    read_food("food.json")
                                elif val4 == "2":
                                    user_id = input("Enter User Id: ")
                                    quantity = int(input("Enter the quantity of food: "))
                                    user_place_order("user.json", "food.json", user_id, quantity)
                                elif val4 == "3":
                                    user_id = input("Enter User Id: ")
                                    user_order_history("user.json", user_id)
                                elif val4 == "4":
                                    user_id =input("Enter the id: ")
                                    name = input("Enter the name: ")
                                    age = int(input("Enter your Age: "))
                                    phn = input("Enter the Phn number: ")
                                    update_profile("user.json", user_id, name, age, phn)
                                else:
                                    print("Thanks For Your Visit ")
                                    break
                        else:
                            print("Wrong Password!!")
                    else:
                        print("Wrong Username!!")                            
                
            elif val2 == "2":
                print("  Admin   ")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("admin.json", "r+")
                content = json.load(file)
                if content["name"] == user:
                    if content["password"] == password:
                        while True:
                            print()
                            print("1) Add New Food")
                            print("2) Edit Food")
                            print("3) View Food")
                            print("4) Remove Food") 
                            print("5) Exit")
                            val3 = str(input("Enter Your Choice Admin!!"))
                            if val3 == "1":
                                food_id = input("Enter Food ID: ")
                                food_name = input("Enter the Food to be added")
                                price = int(input("Enter the price of food: "))
                                discount = int(input("Enter the discount value"))
                                no_plates = int(input("Enter the Stock Value: "))
                                add_food("food.json", food_name, price, discount ,no_plates)
                            elif val3 == "2":
                                food_id = input("Enter Food ID: ")
                                price = int(input("Enter the price of food: "))
                                discount = int(input("Enter the discount value"))
                                no_plates = int(input("Enter the Stock Value: "))
                                update_food("food.json", food_id, price, discount , no_plates)
                            elif val3 == "3":
                                read_food("food.json")
                            elif val3 == "4":
                                food_id =input("Enter food need to be deleted : ")
                                remove_food("food.json", food_id)
                            else:
                                file.close()
                                print("See you again")
                                break
                    else:
                        print("Wrong Password!!")
                else:
                    print("Wrong Username!!")
            else:
                break
    else:
#--------------Exit--------------------#
        print("See you again !!")
        break