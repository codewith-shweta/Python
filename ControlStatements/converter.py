# pyhton weight converter
weight = int(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit =="K":
    weight = weight* 2.205
    unit = "Kgs"
elif unit =="L":
    weight = weight/2.205
    unit= "Lbs"
else:
    print("{unit} is not valid")

print(f"YOur weight is: {weight} {unit} ")
