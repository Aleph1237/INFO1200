#Prints welcome message, then adds a space
print("Corbin Woods's Tip Calculator App")
print()

# asks user for cost of meal, the tip percentage, and the tip ammount
costOfMeal = float(input("What was the cost of your meal?\t"))
tipPercentage = float(input("What was the tip percentage?\t"))
print()

#calculates the tip ammount, then displays tip ammount rounded to two decimal places
tipAmount = costOfMeal * (tipPercentage / 100)
tipAmount = round(tipAmount,2)
print("Tip Ammount\t" + str(tipAmount))

# Calculates the total ammount of the meal, including the tip, then displays result.
totalAmount = tipAmount + costOfMeal
totalAmount = round(totalAmount,2)
print("Total Amount:\t" + str(totalAmount))

