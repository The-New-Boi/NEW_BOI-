a = int(input("Enter your weight in kg :"))
b = int(input("Enter your height in cm :"))
BMI = a/((b**2)/100**2)
print("your BMI is",BMI)
if (BMI< 18.5):
  print("you are lower than normal BMI of a person or you r underweight")
elif (BMI>18.5 and BMI<24.9):
  print("you r alright")
else:
  print("you are above than normal BMI of a person or you r overweight")
