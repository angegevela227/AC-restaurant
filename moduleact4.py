import productdiction3
#choices of the users on what type of discount they want
userchoice = input("What type of discount do you want to avail? ")

#discount choices
snrdisc = productdiction3.total * .30 
loyaldisc = productdiction3.total *  .40
#price that user paying to the product they choose
total1 = productdiction3.total - snrdisc
total2 = productdiction3.total - loyaldisc
#conditional if users pick in one of the discount choices
if userchoice.lower() == "senior":#typesenioriftheuserisabove60
    print("the discount price is ", snrdisc)
    print("the total price ",total1)
elif userchoice.lower() == "loyalty":#typelyaltyiftheuserisloyalcustomerandhadloyaltycard
    print("the discount price is ", loyaldisc)
    print("the total price ",total2)
else:
    print("Invalid discount type. Please enter 'senior' or 'loyalty'.")