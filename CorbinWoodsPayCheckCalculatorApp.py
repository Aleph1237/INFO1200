# displays beginning message and adds a space.
print("Corbin Woods's Pay Check Calculator App")
print()

# User puts in hours worked and pay rate.
hoursWorked = float(input("How many hours did you work?\t"))
payRate = float(input("What is your pay rate?\t\t"))
print()

# calculates and presents the gross pay.
grossPay = hoursWorked * payRate
print("Gross Pay:\t" + str(round(grossPay, 2)))

# calculates and discloses how much was taken by the government, and at what rate.
taxRate = .18
print("Tax Rate:\t" + str(taxRate))
taxAmmount = grossPay * taxRate
print("Tax Ammount:\t" + str(round(taxAmmount, 2)))

# calculates and shows the take home pay
takeHomePay = grossPay - taxAmmount
takeHomePay = round(takeHomePay,2)
print("Take Home Pay:\t" + str(round(takeHomePay, 2)))

