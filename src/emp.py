class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment_salary(self, amount):
        self.salary += amount
        return self.salary

    def decrement_salary(self, amount):
        if amount > self.salary:
            raise ValueError("Salary cannot be negative")
        self.salary -= amount
        return self.salary

    def yearly_salary(self):
        return self.salary * 12

    def change_name(self, new_name):
        self.name = new_name