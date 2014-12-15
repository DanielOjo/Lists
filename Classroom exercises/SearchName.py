#SearchName.py

# Program to search for a name in a list

NamesList = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

ElementSought = input('Enter the name you are searching for : ')
NamesList.append(ElementSought)
ThisElement = 0

#If you enter a name that is not in the list of names them the This Element will look try to assign to a Element in the list that isnt there
Found = False
while not Found:
       if NamesList[ThisElement] == ElementSought:
          Found = True
       else:
          ThisElement = ThisElement + 1
          

if Found:
   print('{0} was in element {1} in the list'.format(ElementSought, ThisElement))
else:
   print('Not found')
