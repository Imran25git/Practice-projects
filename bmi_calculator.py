# bmi = weight/height^2

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(pow(height,2))
round_bmi = round(bmi,2)
print("Your body mass index is: ",round_bmi)

if (bmi < 18.5):
  print("You are underweight")
  print("You need to gain weight")
elif (bmi >= 18.5 and bmi < 24.9):
  print("You have normal weight")
  print("You are good")
elif (bmi >= 25 and bmi < 29):
  print("You are overweight")
  print("You need to lose weight")
elif (bmi >= 30):
  print("You are obese")
  print("You need to lose weight quickly")
else:
  print("Invalid input!!! Make sur you give inputs according to condition or need... If correct then issue in bmi calculator")
