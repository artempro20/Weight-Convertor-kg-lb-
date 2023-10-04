
print("This is a weight converter \n")

response = input("Do you want to convert kg-->lb (KL) or lb-->kg (LK) \n").upper()

if response == "KL": 
    weight_kg = float(input("Enter your weight in kilograms: "))
    weight_lb = weight_kg * 2.20462
    print("Your weight is {:.1f} lb".format(weight_lb))
elif response == "LK":
    weight_lb = float(input("Enter your weight in pounds: "))
    weight_kg = weight_lb / 2.20462
    print("Your weight is {:.1f} kg".format(weight_kg))
else: print("Error: Invalid Choice!")