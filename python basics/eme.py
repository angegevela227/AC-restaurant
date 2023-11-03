year = int(input("Please enter a year: "))

a = year % 19
b = year // 100
c = year % 100
d = (19*a+24)%30
e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7


if (year >= 1900) and (year <= 2099):
    dateofeaster =22 + d + e
    if dateofeaster > 31:
        print("April {}".format(dateofeaster - 31))
    else:
            print("March {}".format(dateofeaster))
else:
           print("Error: Year is out of range: 1900 - 2099")



score = float(input("Enter a numeric score: "))

if score >=90:
    print("your grade is A")
elif score >=80 and score <=90:
    print("your grade is B")
elif score >=70 and score <=80:
    print("your grade is C")
elif score >=60 and score <=70:
    print("your grade is D")
else:
    print("your grade is F")



months = ['January','Feb','March','April','May','June','July','August','Sep','Oct','Nov','Dec']
for i in reversed(months):
    print("This month is part of the year is ",i)

#nums = (12, 10, 32, 3, 66, 17, 42, 99, 20)
#for i in range(nums):
#    print(nums[1],"-",nums[i]**2)


nums = (12, 10, 32, 3, 66, 17, 42, 99, 20)

for i in nums:
    print(i)
    print("the square of",i,"is", i**2)