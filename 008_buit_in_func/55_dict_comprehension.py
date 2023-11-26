import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# iterableであれ何でも良いので、listをもとにdictすることも可能
students_score = {name: random.randint(1, 100) for name in names}
print(students_score)

print("*****")
passed_students = {name: score for (name, score) in students_score.items() if score > 75}
print(passed_students)

print("*****")
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)
