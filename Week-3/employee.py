class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   
    def annual_salary(self):
        return self.salary * 12
emp = Employee("John", 5000)
print("Annual Salary:", emp.annual_salary())
