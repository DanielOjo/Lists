#Shopping List
#Daniel Ogunlana
#09/12/2014

<<<<<<< HEAD
shopping_list = [0]
=======
shopping_list = [""]
>>>>>>> branch 'master' of https://github.com/DanielOjo/Lists.git
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

for index in range(len(shopping_list)):
    print("item {0} is {1}".format(index, shopping_list[index]))
