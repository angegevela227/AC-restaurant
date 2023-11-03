
# A program that will convert meters to centimeter, kilometer, miles
# Ask the user to enter the value of meter
# Display the result 



meter = float(input("Enter the value of meter: "))
#value of metric length 
centimeter = 0.01
kilometers = 1000
miles = 1609
#convert meter to centimeter, kilometer, miles
centimeter = 0.01/meter
kilometers = 1000/meter
miles = 1609/meter

print("Length in centimeter: ", centimeter)
print("Length in kilometer: ", kilometers )
print("Length in meters: ", meter)