import drill
user = input("Enter your chosen discount: ")
#discountchoices
student = drill.total * .20
teacher = drill.total * .15
senior = drill.total * .25
loyalty = drill.total * .30
none = drill.total 

if user.lower() == "student":
    drill.total -= student
elif user.lower() == "teacher":
    drill.total -= teacher
elif user.lower() == "senior":
    drill.total -= senior
elif user.lower() == "loyal":
    drill.total -= loyalty
elif user.lower() == "none":
    print("The user does not have any discounts to apply.")
else:
    print("Invalid input. Please try again.")

# display new total price after discount
print(f"The total price after discount: Php {drill.total:.2f}")