#Get numbers from users
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#display the mathematical operation
print("Select an Operation:")
print("1.Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")

#get user's choice
choice = input("Enter your choice (1-4): ")

#Perform Calculations
if choice == "1":
    result = num1 + num2
    print("Result = ", result)
elif choice == "2":
    result = num1 - num2
    print("Result = ", result)
elif choice == "3":
    result = num1 * num2
    print("Result = ", result)
elif choice == "4":
    result = num1 / num2
    print("Result = ", result)

else:
    print("Invalid choice!  Please select 1, 2, 3 or 4")
