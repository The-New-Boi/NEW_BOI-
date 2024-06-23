a = int(input("Enter your weight in kg :"))
b = int(input("Enter your height in cm :"))
BMI = a/((b**2)/100**2)
print("your BMI is",BMI)
if (BMI< 18.5):
  print("kuposhan ka shikaar")
elif (BMI>18.5 and BMI<24.9):
  print("sahi hai tu")
else:
  print("Duniya main gareebee teri vagah se hai")
