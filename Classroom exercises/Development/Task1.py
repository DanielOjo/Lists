#DanielOgunlana (40730)
#Lists Development Exercise Task 1 
#05/01/15

def random_number():
    import random 
    random_num = random.randint(1,11)
    return random_num
 
def countrys():
    country_list = ["England","US","France","Spain","Belgium","Japan","China","Italy","Germany","Canada"]
    return country_list
def capitals():
    capital_list =  ["London","WashingtonDC", "Madrid", "Paris","Brussels","Tokyo","Hongkong","Rome","Berlin","Ottawa"]
    return capital_list

def process_country(country_list,random_num):
    country = country_list[random_num]
    return country
def process_capital(capital_list,random_num):
    capital = capital_list[random_num]
    return capital

def ask_user(country,capital):
    user_answer = input("Name the capital of {0}: ".format(country))
    if user_answer == capital:
        print("That is correct")
    else:
        print("That is wrong")

def main_program():
    random_num = random_number()
    country_list = countrys()
    capital_list = capitals()
    country = process_country(country_list,random_num)
    capital = process_capital(capital_list,random_num)
    ask_user(country,capital)

#main program
main_program()
