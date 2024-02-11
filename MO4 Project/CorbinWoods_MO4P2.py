#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 9/22/22
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#prints welcome message then a space
print("Corbin Woods's Tip Calculator") 
print()

#asks user for the cost of the meal
meal_cost = float(input("Cost of meal:"))
print()

# tip percentages
tip_percent = [15, 30, 5]

#for loop which calculates the tip percentages and amounts, then displays the results.
for element in tip_percent:
    tip_percent = element / 100
    tip_amount = tip_percent * meal_cost
    total_amount = tip_amount + meal_cost
    print(str(element) + "%")
    print("Tip amount: " + str(tip_amount))
    print("Total amount:" + str(total_amount))
    print()
