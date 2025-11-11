import Employee
class ShiftSupervisor(Employee.Employee):
    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self.salary = salary
        self.bonus = bonus
    
    def set_salary(self, salary):
        self.salary = salary
    def set_bonus(self, bonus):
        self.bonus = bonus
       
    def get_salary(self, salary):
        return self.salary 
    def get_bonus(self, bonus):
        return self.bonus
get_name = input("Please enter employee's name: ")
get_number = int(input("Please enter employee's number: "))
get_salary = int(input("Please enter your salary: "))
production = input("Was the production goal met this year? Type Y for yes:")
if production == 'n' or 'N':
    print("Total income is: $", (get_salary)) 
elif production == 'y' or 'Y': 
    totalIncome = get_salary + 3000
    print("Total income is: $", (totalIncome))