total_amount = int(input("Welcome to the tip calculator. What was the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
split = int(input("How many people to split the bill? "))
total_bill_split = total_amount * tip_percentage / 100
total_bill_add = total_amount + total_bill_split
each_person_pay = round(total_bill_add / split, 2)
print(f"Each person should pay: {each_person_pay}")12