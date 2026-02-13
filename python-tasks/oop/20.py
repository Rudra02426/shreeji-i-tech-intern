### Task 20: Employee Payroll
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def apply_bonus(self, bonus):
        self.salary += bonus

    def show_salary(self):
        print("Final Salary:", self.salary)


# user input
salary = int(input("Enter base salary: "))
bonus = int(input("Enter bonus amount: "))

# object creation
emp = Employee(salary)

# apply bonus
emp.apply_bonus(bonus)

# display salary
emp.show_salary()
