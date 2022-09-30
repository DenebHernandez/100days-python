#User input
bill_amount = float(input("What was the total bill?: $"))
tip_percentage = int(input("What percentage tip would you like to give?: "))
people_amount = int(input("How many people to split the bill?: "))

#Calculations
tip_percentage = 1 + (tip_percentage / 100)
total_bill = bill_amount * tip_percentage
total_bill = total_bill / people_amount
total_bill = round(total_bill, 2)

#Formatted bill
formatted_bill = "{:.2f}".format(total_bill)
#Message
message = f"Each person should pay: ${formatted_bill}"

print(message)