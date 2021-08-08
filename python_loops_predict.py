#     x = 10
#     if x > 50:
#     	print("bigger than 50")
#     else:
#     	print("smaller than 50")
# class EmptyClass:
#     pass

# for val in my_string:
#     pass
# # Boolean Values
# is_hungry = True
# has_freckles = False

# # Numbers 
# age = 35 # storing an int
# weight = 160.57 # storing a float

# # Strings
# name = "Joe Blue"
# # Composite Types
# # Tuples
# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# # Lists
# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# # Dictionaries
# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists
# new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}   
# # 
# # Common Functions
# print(type(2.63))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>     

# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))	# output: 11

# # Type Casting or Explicit Type Conversion
# print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61

#1
# for i in range(1, 10, 1):
#     print(i)
#  Predicted 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Actual
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#2
# for t in range(1, 10, 3):
#     print(t)
# Predicted 
# 1
# 4
# 7
# Actual
# 1
# 4
# 7

#3
# for y in range(5):
#     if y < 5:
#         print(y)
#     elif y == 3:
#         print("y is 3")
# Predicted
# 3
# "y is 3"
# Actual
# 0
# 1
# 2
# 3
# 4

#4
# for j in range(20, 1, -3):
#     print(j)
# Predicted
# 20
# 17
# 14
# 11
# 8
# 5
# 2
# Actual
# 20
# 17
# 14
# 11
# 8
# 5
# 2

#5
# cities = ["London", "Paris", "Tokyo"]
# for city in cities:
#     print(city)
# Predictive
# London
# Paris
# Tokyo
# Actual
# London
# Paris
# Tokyo

#6
# numbers = [7, 13, 8, 42]
# for x in range(0, len(numbers)):
#     print(x)
#     print(numbers[x])
# if numbers[len(numbers) - 1] == 42:
#     print("The answer to life, the universe, and everything.")
# Predicted
# 0
# 7
# 1
# 13
# 2
# 8
# 3
# 42
# The answer to life, the universe, and everything.

# Actual 
# 0
# 7
# 1
# 13
# 2
# 8
# 3
# 42
# The answer to life, the universe, and everything.

#7
# for num in range(10):
#     if num % 2 == 0:
#         print("Hello")
#     elif num % 4 == 0:
#         print("World")
#     else:
#         print(num)
# Predicted
# Hello
#  1
# Hello
# 3
# Hello
# 5
# Hello
# 7
# Hello
# 9

# Actual
# Hello
#  1
# Hello
# 3
# Hello
# 5
# Hello
# 7
# Hello
# 9

#8
# for num in range(10):
#     if num % 4 == 0:
#         print("Hello")
#     elif num % 2 == 0:
#         print("World")
#     else:
#         print(num)

# Predicted
# Hello
# 1
# World
# 3
# Hello
# 5
# World
# 7
# Hello
# 9

# Acutal
# Hello
# 1
# World
# 3
# Hello
# 5
# World
# 7
# Hello
# 9

#9
# pet_info = {
#     "name": "Fido", 
#     "age": 4, 
#     "trick": "rolls over"
# }
# for key in pet_info:
#     print(key)
#     print(pet_info[key])

# Predicted
# 
# Actual

#10
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)





# python python_loops_predict.py
