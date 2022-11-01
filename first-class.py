class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay =pay
        self.email = first_name+'.'+last_name+"@mail.com"

        def E_fullName(self):
            return(f"{self.first_name}{self.last_name}")
        

employee_1 = Employee('John','Doe',50000)
employee_2 = Employee('Mark','Anthony',77000)

# employee_1.first_name = "Mercy"
# employee_1.last_name = "Masika"
# employee_1.salary = 33338
# employee_1.email = "mercy.masica@email.com"

# employee_2.first_name = "John"
# employee_2.last_name = "Doe"
# employee_2.salary = 85858
# employee_2.email = "john.doe@email.com"

print(employee_1.email)
print(employee_2.email)