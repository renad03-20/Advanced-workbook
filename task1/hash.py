from sys import exit

#insertion
def add_student(id):
    if id in intrested_in_football:
        print(f'student {id} is alreadt in the list')
    else:
        intrested_in_football[id]= True
        print(f'student {id} has been added')

#deletion
def delete_student(id):
    if id in intrested_in_football:
        del intrested_in_football[id]
        print(f'student {id} is removed')
    else:
        print(f'student {id} is not in the list')
        

#seartion
def search_student(id):
    if id in intrested_in_football:
        print(f'student {id} is in the list')
    else:
        print(f'student {id} is not in the list')

def display_all():
    if not intrested_in_football:
        print('no student are cerrently in the list ')
    else:
        print('student that are curently in the group:')
        for id in intrested_in_football.keys():
            print(f'- {id}')


intrested_in_football = {
    # id , is intrested in foolball
    111: True,
    112: True,
    113: True,
    114: True,
    115: True,
}

while True:
    print('-----------*OPTIONS*-----------')
    print('1- review all students')
    print('2- add a student')
    print('3- delete a student')
    print('4- search for a student')
    print('5- exit')

    choice = input('Enter your choice: ')

    if choice.isdigit() and 1 <= int(choice) <= 5:
        if choice == '1':
            display_all()
        elif choice == '2':
            student_id = int(input('Enter student ID: '))
            add_student(student_id)
        elif choice == '3':
            student_id = int(input('Enter student ID: '))
            delete_student(student_id)
        elif choice == '4':
            student_id = int(input('Enter student ID: '))
            search_student(student_id)
        elif choice == '5':
            print('bey!')
            exit()
        else:
            print('invalid choice, please try again.')
    else:
        print('please enter a valid number!')
    