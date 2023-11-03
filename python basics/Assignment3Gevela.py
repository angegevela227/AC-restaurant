
#Declare Variable
apple = 25.00
orange = 30.00
mango = 80.00
guava = 100.00
#Display
print("Available Fruits:/n Apple:25.00,orange = 30.00,mango = 80.00,guava = 100.00")
#Get Inputs from the user 
AppleGetInput = int(input("How many Apples?: "))
ApplePriceTL = apple * AppleGetInput

OrangeGetInput = int(input("How many Oranges?: "))
OrangePriceTL = orange* OrangeGetInput 

MangoGetInput = int(input("How many Mango?: "))
MangoPriceTL = mango * MangoGetInput 

GuavaGetInput = int(input("How many Guava?: "))
GuavaPriceTL =  guava* GuavaGetInput
#Get Input for Payment
payment = int(input("Enter Your Payment: "))
#Total Price Computation
TotalPrice = ApplePriceTL + OrangePriceTL +  MangoPriceTL + GuavaPriceTL 
#Total Change 
Change = TotalPrice - payment

print("The total price is: ",str(TotalPrice))
print("Your Charge is: ",str(Change))