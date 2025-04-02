# Program to find the largest of three numbers

def find_largest_three():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    largest = max(num1, num2, num3)
    print(f"The largest number is: {largest}")

# Modify the program to accept five numbers
def find_largest_five():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))
    num5 = float(input("Enter the fifth number: "))
    
    largest = max(num1, num2, num3, num4, num5)
    print(f"The largest number is: {largest}")

# Call the function to find the largest of five numbers
find_largest_five()
