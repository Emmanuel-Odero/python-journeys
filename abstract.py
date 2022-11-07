from  abc import  ABC, abstractmethod

class Payroll(self):
    @abstractmethod
    def print_payroll():
        pass

class Employee():
    id = 0
    first_name = ''
    last_name = ''
    role = ''
    is_active = True
    salary = 0
    email = ''
    phone_number = ''

class FullTimeEmployee(Employee):
    def print_payroll(self):
        self.salary = 10000

class HourlyEmployee(Employee):
    num_hours_worked = 0
    hourly_rate = 0
    def print_payroll(self):
        self.salary = self.num_hours_worked * self.hourly_rate