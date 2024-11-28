class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        return f"Employee Name:{self.name}, Employee ID:{self.id}"

class PermanentEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
    
class ContractEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name,id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

perm_emp = PermanentEmployee("John", "P101", 1000)
print(perm_emp.display())
print(f"Permanent Employee Salary: ${perm_emp.calculate_salary()}")
print()
contract_emp = ContractEmployee("Jessica", "C101", 50, 10)
print(contract_emp.display())
print(f"Contract Employee Salary: ${contract_emp.calculate_salary()}")