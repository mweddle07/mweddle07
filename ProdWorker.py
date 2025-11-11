import Employee
class ProductionWorker(Employee.Employee):
    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self.shift = shift
        self.pay = pay
        
    def get_shift(self, shift):
        return self.shift
    def get_pay(self, pay):
        return self.pay
    
get_name = input("Please enter employee's name: ")
get_number = int(input("Please enter employee's number: "))
get_shift = int(input("Please enter shift number (Day shift = 1, Night shift = 2): "))
get_pay = float(input("Please enter the employee's hourly pay rate: "))
emp = ProductionWorker(get_name, get_number, get_shift, get_pay)
print('')
print("Employee's Name: ", get_name)
print("Employee's Number: ", get_number)
if get_shift == 1:
   print("Employee's Shift: Day shift")
if get_shift == 2:
    print("Employee's Shift: Night shift")
elif get_shift != 1 or 2:
    print("Error: Day shift = 1, Night shift = 2")
print("Employee's Hourly Pay Rate: ", get_pay)
emp = ProductionWorker(get_name, get_number, get_shift, get_pay)