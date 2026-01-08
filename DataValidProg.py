Name=input("Enter your Name:")
Age=int(input("Enter your Age:"))
email_id=input("Enter your email id:")
contact=input("Enter your contact number")
grad=float(input("Enter your percentage:"))

if Age>=18:
  if grad>=60:
    if len(contact)==10:
      print("Intern Eligible")
    else:
      print("Contact Number must be exactly 10 digit")
  else:
    print("Percentage should be more than 60%")
else:
  print("Age should be more than 18")
