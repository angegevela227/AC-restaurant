products ={
    "notebook" : 50,
    "marker": 40,
    "ballpoint pen": 25,
    "bondpaper": 250,
    "staplerp": 150
}
user = "perry"
lgtpass = "oakley"
#loginfeature
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user == username and lgtpass == password:
        print("Login successful!")
        print("Please proceed to the next step!")
        break
    else:
        print("invalid input.try again!")

lst_products = []
#displaying the available products
for product, price in products.items():
    print(f"{product} - PHP {price:.2f}")
    print("============")

#user choosing their product they desire
while True:
    user_customer = input('Enter your desired product: ')
    if user_customer == 'f':
        print("This is your chosen products: ")
        break
    if user_customer not in products:
        print("invalid input,please try again")
        continue
    lst_products.append(user_customer)

#total cost of the product
total = 0
for product in lst_products:
    price = products[product]
    total += price
    print(f"{product}: PHP {price:.2f}")

print(f"Total cost: PHP {total:.2f}")