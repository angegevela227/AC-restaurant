#List of products in dictionary form
products = {
    "lemon" : 29.50,
    "meat"  : 168.48,
    "cup noodles" : 21.85
}


#Empty list to store chosen product of the user
chosen_products = {}

#Printing the available products and their prices
print("Available products:")
for product, price in products.items():
    print(f"{product}: {price:.2f} pesos")


while True:
    userchoice = input("My chosen Product are: ")#type'up'ifthechosenproductaresettled
    if userchoice == "up":
        break
    if userchoice in chosen_products:
        print("The product is already chosen. Choose another product")
    if userchoice not in products:
        print("Invalid product name. Please try again.")
        continue
    amount = int(input("Enter your the quantity of product: "))
    if amount <= 0:
        print("Quantity should be a positive integer. Please try again.")
        continue
    chosen_products[userchoice] = amount
#Displaying the users choice of product 
print("Chosen products:")
#Computing the price of chosen product of the users
total = 0
for product, amount in chosen_products.items():
    price = products[product]
    cost = price * amount
    total += cost
    print(f"{product}: {price:.2f} pesos x {amount} = {cost:.2f} pesos")

#Display the total cost
print(f"The exracted total is{total: .2f} pesos")