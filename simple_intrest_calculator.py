# Simple Interest Calculator

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of intrest: "))
t = input("Which time period you want to select (year, month or week): ").lower()

if t == "year":
  t = int((input("Enter time in year after which you have to pay: ")))
elif t == "month":
  t = int((input("Enter time in month after which you have to pay: ")))/12
elif t == "week":
  t = int((input("Enter time in week after which you have to pay: ")))/52
else:
  print("Something went wrong try it again")
  exit()
# I = pxrxt/100

I = (p*r*t)/100
round_I = round(I,3)
print("The intrest calculated is: ",round_I)
