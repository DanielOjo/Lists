#DanielOgunlana (40730)
#Lists Development Exercise Task 1 
#05/01/15

import random

country_list = ["England","US","France","Spain","Belgium","Japan","China","Italy","Germany","Canada"]
capital_list = ["London","WashingtonDC","Paris","Brussels","Tokyo","Hongkong","Rome","Berlin","Ottawa"]

question = random.choice(country_list)
print(question)
correct_answer = capital_list(int(question) 

user_answer = input("Please type the capital city of this country: ")

answer = False
while not answer:
       if correct_answer == user_answer:
          Found = True
       else:
          print("Your answer was incorrect")

if answer:
    print("Your answer was correct")

