import pandas as pd
#list variable in a list form
#Operating Revenue

room_accomodations ={
    2020 :120000,
    2021 :135000,
    2022 :155000
}
party_packages ={
    2020 :300000,
    2021 :400000,
    2022 :450000
}
food_beverages = {
    2020 :80000,
    2021 :88000,
    2022 :90000
}

OR =({"2020":room_accomodations,"2021":party_packages,"2022":food_beverages})
ind =("Room Accomodations","Party Packages","Food & Beverages")
totalrevenue = 0
for x in OR.values():
    for val in x:
        totalrevenue+=val



#Operating Expenses
WS ={
    2020 :27000,
    2021 :27000,
    2022 :27000
}
SM ={
    2020 :12000,
    2021 :12000,
    2022 :12000
}
PM = {
    2020 :30000,
    2021 :25000,
    2022 :32000
}
OE =({"2020":WS,"2021":SM,"2022":PM})
FIN =("Web Systems","Sales Marketing","Property Maintenance")

totalexpenses = 0
for y in OE.values():
    for value in y:
        totalexpenses+=value

TGOP = totalrevenue - totalexpenses
Tax = TGOP*0.15
coldata = pd.DataFrame(OE,index= FIN)
coldata = pd.DataFrame(OR,index= ind)
#input the filename from the user
fname=input("Enter you desired filename: ")
f =open(f"{fname}.txt","a")
f.write(f"{coldata}\n\nTotalExpenses{totalexpenses}")
f.write(f"{coldata}\n\nTotalExpenses{totalrevenue}")
f.write(f"{coldata}\n\nTotalTGOP{totalrevenue}")
print("File saved!")


