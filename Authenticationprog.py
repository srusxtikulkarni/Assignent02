course=input("Enter your Course")
isstudent=input("Are you student?(yes/no)")
isreg=input("Registering early?(yes/no)")
if course=='PythonProgramming':
  course='PythonProgramming'
  fees=5000
elif course=='DataAnalytics':
  course='DataAnalytics'
  fees=8000
elif course=='AI&ML':
  course='AI&ML'
  fees=12000
else:
  print("Invalid Input")
if isstudent=='yes':
  disc=fees*10/100
elif isreg=='yes':
  disc=fees*5/100
else:
  disc=0
print("\nCourse Choosen:",course)
print("Original Fees:",fees)
print("Total Discount:",disc)
print("Final Payable Amount:",fees-disc)
