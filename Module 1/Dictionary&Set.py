# Q1. Write a program to create a dictionary from two lists: one of keys and one of values.

keys = ['id', 'name', 'age']
values = [101, 'Akhilesh', 22]

mydict = dict(zip(keys, values))

print(mydict)

# Q2. Merge two dictionaries into one

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

print(dict1)

# Q3. Write a program to sort a dictionary by its values.

mydict = {'a': 50, 'b': 20, 'c': 10}

sorted_dict = dict(sorted(mydict.items(), key=lambda x: x[1]))

print(sorted_dict)

# Q4. Give two sets. check if one set is a subset of another.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))

# Q5. Write a program to check wheather two lists have at least one common element using sets.

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

common = set(list1).intersection(set(list2))

if common:
    print("Common element exists")
else:
    print("No common element")