import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Employee:
    def __init__(self, name, emp_id, department, position, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.position = position
        self.salary = salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

class Department:
    def __init__(self):
        # Dictionary to store the departments and their employees
        self.departments = {}

    def add_department(self, department_name):
        # Check if the department already exists
        self.departments[department_name] = []

    def assign_employee(self, employee, department_name):
        # Check if the department exists
        if department_name in self.departments:
            self.departments[department_name].append(employee)
            print(f"{employee.name} assigned to {department_name} department.")

        else:
            print(f"Department '{department_name}' does not exist.")

    def list_departments(self):
        print("Departments:")
        # Iterate through the departments and print their names
        for department in self.departments:
            print(department)

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = pd.DataFrame(columns=["Name", "Employee ID", "Department", "Position", "Salary"])
        self.department_manager = Department()

    def add_employee(self, name, department, position, salary):
        emp_id = self.generate_emp_id()
        new_employee = pd.DataFrame({"Name": [name], "Employee ID": [emp_id], "Department": [department], "Position": [position], "Salary": [salary]})
        self.employees = pd.concat([self.employees, new_employee], ignore_index=True)

    def generate_emp_id(self):
        return np.random.randint(1000, 10000)  # Generate a random 4-digit employee ID

    

    def display_employee_details(self, emp_id):
        employee = self.employees.loc[self.employees['Employee ID'] == emp_id]
        if not employee.empty:
            print(employee)
        else:
            print(f"Employee with ID {emp_id} not found.")

    def display_department_statistics(self):
        department_counts = self.employees['Department'].value_counts()
        department_counts.plot(kind='bar')
        plt.title('Employee Count by Department')
        plt.xlabel('Department')
        plt.ylabel('Employee Count')
        plt.show()

# Example usage:
employee_system = EmployeeManagementSystem()

# Adding employees
employee_system.add_employee("John Doe", "HR", "Manager", 60000)
employee_system.add_employee("Jane Smith", "IT", "Developer", 65000)
employee_system.add_employee("Mike Johnson", "Finance", "Analyst", 55000)
employee_system.add_employee(" Johnson", "Finance", "scientist", 75000)

# Displaying employee details
employee_system.display_employee_details(employee_system.employees.iloc[0]['Employee ID'])
employee_system.display_employee_details(employee_system.employees.iloc[1]['Employee ID'])
employee_system.display_employee_details(employee_system.employees.iloc[2]['Employee ID'])
employee_system.display_employee_details(employee_system.employees.iloc[3]['Employee ID'])


# Displaying department statistics
employee_system.display_department_statistics()
