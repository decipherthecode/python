height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height_in = float(height)
weight_in = float(weight)
Bmi_height = height_in**2
Bmi = int(weight_in / Bmi_height)
print(Bmi)
