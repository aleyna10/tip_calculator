#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip_percent=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip=bill*tip_percent/100
totalBill=bill+tip
each_person="{:.2f}".format(round(totalBill/people,2))
print(f"Each person should pay: ${each_person}")
