#User age input
age = input("What's your current age?: ")

#Casting age into an int
age = int(age)

#Calculate how many days, weeks and months in 90 years
total_days = 365 * 90
total_weeks = 52 * 90
total_months = 12 * 90

#Calculate age in days, weeks and months
age_days = age * 365
age_weeks = age * 52
age_months = age * 12

#Calculate how many months, weeks and days the user has left
days_left = total_days - age_days
weeks_left = total_weeks - age_weeks
months_left = total_months - age_months

#Format message string
message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left."

#Return age
print(message)
