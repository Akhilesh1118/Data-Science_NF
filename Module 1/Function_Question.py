# 1. Create a Function to Check Whether Two Strings are Anagrams 
# Problem 
# Write a function that accepts two strings and returns True if both are anagrams, otherwise False. 

def are_anagrams(str1, str2):
    # Sort both strings and compare them
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True
    else:
        return False

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(are_anagrams(s1, s2))

# 2. Create a Function to Find Second Largest Number in a List 
# Problem 
# Write a function that accepts a list and returns the second largest number.

def second_largest(numbers):
    # Remove duplicate 
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    # Return second largest element
    return unique_numbers[-2]

print(second_largest([10, 20, 30, 40, 50]))

# 3. Create a Function to Count Vowels in a Sentence 
# Problem 
# Write a function that accepts a sentence and returns the count of each vowel.

def count_vowels(sentence):
    # Dictionary to store vowel counts
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Check each character
    for char in sentence.lower():
        if char in vowels:
            vowels[char] += 1

    return vowels

print(count_vowels("Hello World"))

# 4. Create a Function to Check Whether a Number is an Armstrong Number 
# Problem 
# Write a function that returns True if a number is an Armstrong number. 

def is_armstrong(num):
    # Convert number to string
    num_str = str(num)

    # Number of digits
    power = len(num_str)

    total = 0

    # Calculate sum of digits raised to power
    for digit in num_str:
        total += int(digit) ** power

    # Check Armstrong condition
    if total == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))
print(is_armstrong(number))

# 5. Create a Function to Find Common Elements Between Multiple Lists 
# Problem 
# Write a function that accepts three lists and returns common elements. 

def common_elements(list1, list2, list3):
    # Find common elements using sets
    return list(set(list1) & set(list2) & set(list3))

# Example
print(common_elements(
    [1, 2, 3, 4],
    [2, 3, 5, 6],
    [2, 3, 7, 8]
))