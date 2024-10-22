print("welcome to tip calculator")
bill=float(input("what is your bill "))
tip=int(input("how much tip would you like to give?10,12 or 15? "))
people=int(input("how many people to split bill? "))
tip_as_percent=tip/100
total_tip_amount=tip_as_percent*bill
total_bill=bill + total_tip_amount
bill_per_person=round(total_bill/people,2) 
print("each person should pay",bill_per_person)