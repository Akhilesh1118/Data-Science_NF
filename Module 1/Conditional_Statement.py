## 1.  Write a program to check whether a year is a leap year or not.


year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

### 2. Write a program to find the largest among three numbers using nested conditional statements.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "A is the largest number")

elif b > a:
    if b > c:
        print(b, "B is the largest number")

else:
      print(c, "C is the largest number")


### 3. Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character.

ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")
elif ch >= 'A' and ch <= 'Z':
    print("Uppercase letter")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase letter")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")


### 4. Write a program to calculate electricity bill using different unit slabs.


units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 15

print("Electricity bill =", bill)

### 5. Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene.


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

### 6. Write a program to create a simple calculator using if-elif-else.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = input("Enter your choice: ( + , - , * , /) ")

if choice == "+":
    print("Result =", a + b)
elif choice == "-":
    print("Result =", a - b)
elif choice == "*":
    print("Result =", a * b)
elif choice == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result =", a / b)
else:
    print("Invalid choice")

### 7. Write a program to calculate income tax according to salary ranges.


salary = float(input("Enter your salary: "))
print("Salary:", salary)

if salary < 30000:
    tax_rate =  salary * 0.05
    print("Applicable Tax Rate 5 % =", tax_rate)
elif salary <= 70000:
    tax_rate = salary * 0.15
    print("Applicable Tax Rate 15 % =", tax_rate)
else:
    tax_rate = salary * 0.25
    print("Applicable Tax Rate 25 % =", tax_rate)

total = salary - tax_rate
print("Final amount after tax remove =" , total)


### 8. Write a program to check login authentication using username and password conditions.


username = input("enter username : ")
password = input("enter password : ")

if (username == "akhilesh" and password == "password"):
    print("Login Successfully ")
elif (username != "admin"):
    print("Wrong username")
else:
    if ( password != "pass" ):
        print("Invaild credintional ")

#### 9. Write a program to determine whether a point lies in First quadrant, Second quadrant, Third quadrant, Fourth quadrant, On axis, or At origin.

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point is at origin")
elif x == 0 or y == 0:
    print("Point is on axis")
elif x > 0 and y > 0:
    print("Point lies in First quadrant")
elif x < 0 and y > 0:
    print("Point lies in Second quadrant")
elif x < 0 and y < 0:
    print("Point lies in Third quadrant")
else:
    print("Point lies in Fourth quadrant")

### 10. Write a program to assign grades based on marks and display distinction for high scores.

math = int(input("Enter marks math: "))
phy= int(input("Enter marks phy: "))
chem = int(input("Enter marks chem: "))
physical = int(input("Enter marks physical: "))
english = int(input("Enter marks: english: "))

percentage = (math + phy + chem + physical + english)/5
print("Total percentage =", percentage)
69
if percentage >= 90 or percentage > 100:
    print("Grade A ")
elif percentage >= 60 or percentage > 90:
    print("Grade: B")
elif percentage >= 40 or percentage > 60:
    print("Grade: C")
else:
    print("FAIL ")