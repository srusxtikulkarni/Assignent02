emp_name=input("Enter employee name:")
emp_id=input("Enter employee id:")
salary=float(input("Enter Salary:"))
HRA=20/100*salary
DA=10/100*salary
PF=12/100*salary
net_sal=salary+HRA+DA-PF
print("Net Salary:",net_sal)
print("HRA=",HRA)
print("DA=",DA)
print("PF=",PF)
