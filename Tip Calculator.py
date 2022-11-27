bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
split = float(input("How many people to spilt the bill?"))
tip_per = tip / 100

total_tip_amount = bill * tip_per
total_bill = bill + total_tip_amount
bill_split = total_bill / split

print(f"Each person should pay ${round(bill_split, 2)}")