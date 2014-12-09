#Daniel Ogunlana
#List's R&R
#07/12/14

first_student = str(input("Please enter the name of the first student: "))
second_student = str(input("Please enter the name of the second student: "))
third_student = str(input("Please enter the name of the third student: "))
fourth_student = str(input("Please enter the name of the fourth student: "))
fifth_student = str(input("Please enter the name of the fifth student: "))
sixth_student = str(input("Please enter the name of the sixth student: "))
seventh_student = str(input("Please enter the name of the seventh student: "))
eighth_student = str(input("Please enter the name of the eighth student: "))

students_list = [first_student, second_student, third_student, fourth_student, fifth_student, sixth_student, seventh_student, eighth_student]

for each in students_list:
    print(each)

place_to_change = int(input("Please select a student to edit: "))
student_name_change = str(input("Please enter their new student name: "))
students_list.pop(place_to_change)
students_list.insert(place_to_change,student_name_change)
for count in students_list:
    print(count)
