# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
life_left = 90 - age_int
life_left_days = life_left * 365
life_left_weeks = life_left * 52
life_left_months = life_left * 12

print(
  f"You have {life_left_days} days, {life_left_weeks} weeks, and {life_left_months} months left."
)
