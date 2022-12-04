year = int(input("Which year do you want to check? "))

leap_year = year % 4
if leap_year == 0:
    print("Leap year")
else:
    print("Not leap year")  