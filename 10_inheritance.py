class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_name(self):
        return self.name

    def get_employee_id(self):
        return self.employee_id

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department


manager = Manager("John", "123456", 100000, "IT")
print(manager.get_name())
print(manager.get_employee_id())
print(manager.get_salary())
print(manager.get_department())
