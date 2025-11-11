import employee
import pickle
LOOK_UP = 1
ADD = 2 
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employee'

def main():
    emp = load_employee()
    choice=0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(emp) 
        elif choice == ADD:
            add(emp) 
        elif choice == CHANGE:
            change(emp) 
        elif choice == DELETE:
            delete(emp)
    save_employee(emp)
def load_employee():
    try:
        input_file = open(FILENAME, 'wb')
        employee = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee = {}
    return employee
def get_menu_choice():
    print()
    print("1.  Look up an employee")
    print("2.  Add a new employee")
    print("3.  Change an existing employee")
    print("4.  Delete an employee")
    print("5.  Quit the program")
    print()
    choice = int(input("Enter your choice: "))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))
    return choice
def look_up(emp):
    idNum = input("Enter your ID number: ")
    print(emp.get(idNum, 'Employee not found.'))
def add(emp):
    name = input("Enter a name: ")
    idNum = input("Enter ID number: ")
    dept = input("Enter the department: ")
    jobTitle = input("Enter the job title: ")
    entry = employee.Employee(name, idNum, dept, jobTitle)
    if idNum not in emp:
        emp[idNum] = entry
        print("Employee has been added.")
    else:
        print("Employee already exists")
def change(emp):
    idNum = input("Enter ID number: ")
    if idNum in emp:
        name = input("Enter the new name: ")
        dept = input("Enter the new department: ")
        jobTitle = input("Enter the new job title: ")
        entry = employee.Employee(name, idNum, dept, jobTitle)
        emp[idNum] = entry
        print("Employee updated")
    else:
        print("Employee not found")
def delete(emp):
    idNum = input("Enter an ID number: ")
    if idNum in emp:
        del emp[idNum]
        print("Employee deleted")
    else:
        print("That name is not found")
def save_employee(emp):
    output_file = open(FILENAME, 'wb')
    pickle.dump(emp, output_file)
    output_file.close()
main()