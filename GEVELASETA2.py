import pandas as pd

# Operating Revenue
room_accommodations = {
    2020: 120000,
    2021: 135000,
    2022: 155000
}
party_packages = {
    2020: 300000,
    2021: 400000,
    2022: 450000
}
food_beverages = {
    2020: 80000,
    2021: 88000,
    2022: 90000
}

OR = {"Year": list(room_accommodations.keys()), "Room Accommodations": list(room_accommodations.values()),
      "Party Packages": list(party_packages.values()), "Food & Beverages": list(food_beverages.values())}

# Operating Expenses
WS = {
    2020: 27000,
    2021: 27000,
    2022: 27000
}
SM = {
    2020: 12000,
    2021: 12000,
    2022: 12000
}
PM = {
    2020: 30000,
    2021: 25000,
    2022: 32000
}
OE = {"Year": list(WS.keys()), "Web Systems": list(WS.values()),
      "Sales Marketing": list(SM.values()), "Property Maintenance": list(PM.values())}

totalrevenue = sum(val for x in OR.values() if x != "Year" for val in x)
totalexpenses = sum(value for y in OE.values() if y != "Year" for value in y)
TGOP = totalrevenue - totalexpenses

# Print the results
fname=input("Enter you desired filename: ")
with open(f"{fname}.txt", "w") as f:
    f.write("Operating Revenue:\n")
    f.write(pd.DataFrame(OR).to_string(index=False))
    f.write("\n\n")
    f.write("Operating Expenses:\n")
    f.write(pd.DataFrame(OE).to_string(index=False))
    f.write("\n\n")
    f.write(f"Total Revenue: {totalrevenue}\n")
    f.write(f"Total Expenses: {totalexpenses}\n")
    f.write(f"Total Gross Operating Profit (TGOP): {TGOP}\n")

print("Operating Revenue:")
print(pd.DataFrame(OR).to_string(index=False))
print()

print("Operating Expenses:")
print(pd.DataFrame(OE).to_string(index=False))
print()

print(f"Total Revenue: {totalrevenue}")
print(f"Total Expenses: {totalexpenses}")
print(f"Total Gross Operating Profit (TGOP): {TGOP}")
