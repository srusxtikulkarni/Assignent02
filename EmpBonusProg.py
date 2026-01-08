Emp_name=input("Enter name")
sal=float(input("Enter your salary:"))
rating=int(input("Performance Rating(1-5)"))
if rating==5:
  bonus=sal*20/100
if rating==4:
  bonus=sal*15/100
if rating==3:
  bonus=sal*10/100
if rating<3:
  bonus=0
print("Employee Name:",Emp_name)
print("Performance Rating:",rating)
print("Bonus Amount:",bonus)
print("Final Salary",sal+bonus)
