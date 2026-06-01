### 1. Write a program to find the largest and smallest elements in a list.  

mylist = [2,4,6,8,10]
smallest = min(mylist)
largest = max(mylist)
print(f"smallest element in the list {mylist} is {smallest}")
print(f"largest element in the list {mylist} is {largest}")



### 2. Write a program to remove duplicate elements from a list.  


numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []

for num in numbers:
   if num not in unique_numbers:
      unique_numbers.append(num)

print(unique_numbers)

### 3. Write a program to reverse a list without using built-in reverse functions.  


lst = [10, 20, 30, 40, 50]
reversed_list = []

i = len(lst) - 1
while i >= 0:
    reversed_list.append(lst[i])
    i -= 1

print(reversed_list)

### 4. Write a program to count even and odd numbers in a list.  


lst = [1,2,3,4,5,6,7,8,9]
even_count = 0
odd_count = 0
for num in lst:
 if num % 2 == 0:
   even_count += 1
 else:
  odd_count += 1

print(f"Even number count = {even_count}")
print(f"Odd number count = {odd_count}")

### 5. Write a program to merge two lists and sort the final list.  


list_1 = [1,2,3,4]
list_2 = [5,6,7,8,9]

list_3 = list_1 + list_2
print(list_3)

### 6. Write a program to find the second largest element in a list.  


mylist = [15,20,34,5,34,89,99,100]

mylist.sort() # Using sort keyword sort the list
print(mylist[-2])  # -2 give the last two place element

### 7. Write a program to check whether an element exists in a tuple.  


tp = (1,9,10,20,30,40,50)
key = 500
idx = 0
for i in tp:
  if( i == key ):
    print(f"{key} number is present at index {idx}")
    break
  idx = idx + 1
else:
   print("key is not present in the tuple ")

### 8. Write a program to count the occurrence of an element in a tuple.  


tp = (1,20,10,20,30,40,50,20,)
val = 20
print(f"{val} occurrence of = {tp.count(val)} times ")

### 9. Write a program to sort a list of tuples based on tuple values.  


tuples_list = [(2, 5), (1, 3), (4, 1), (2, 1)]

# Sort by the first value, then by the second value
sorted_list = sorted(tuples_list)

print("Original list:", tuples_list)
print("Sorted list:", sorted_list)

### 10. Write a program to convert a tuple into a list and a list into a tuple.

mytuple = (1, 2, 3, 4)
mylist = list(mytuple)

print("Tuple into list:", mylist)

list_data = [10, 20, 30, 40]
tuple_data = tuple(list_data)

print("list into tuple ", tuple_data)