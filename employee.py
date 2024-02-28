from dataclasses import dataclass

@dataclass
class Employee:
    name: str =""
    age: int =0
    department: str = ""
    salary: float =0.0

employees = []

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    
    new_employee = Employee(name, age, department, salary)
    employees.append(new_employee)
    print("Employee added successfully.\n")

def display_employees():
    print("Employee Details:")
    for employee in employees:
        print(f"Name: {employee.name}, Age: {employee.age}, Department: {employee.department}, Salary: {employee.salary}")
    

def update_employee_salary():
    name = input("Enter full employee name to update salary: ")
    for employee in employees:
        if employee.name == name:
            new_salary = float(input("Enter new salary: "))
            employee.salary = new_salary
            print("Salary updated successfully.\n")
            return
    print("Employee not found.\n")

def remove_employee():
    name = input("Enter full employee name to remove: ")
    for employee in employees:
        if employee.name == name:
            employees.remove(employee)
            print("Employee removed successfully.\n")
            return
    print("Employee not found.\n")


while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee Salary")
    print("4. Remove Employee")
    print("5. Exit")
    
    choice = input("Enter your number for your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        update_employee_salary()
    elif choice == "4":
        remove_employee()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
        
#Ahmed Alkayyal       
# employee management system utilizing dataclasses. Users can add, display, update salaries, and remove employees. 
# To add an employee, input their details which are stored as an Employee object in a list. 
# Displaying employees shows their name, age, department, and salary. 
# Updating an employee's salary requires entering the employee's name and the new salary. 
# Removing an employee involves entering the employee's name for deletion. The program offers a menu-driven interface for these operations. 
# Users can navigate through options to manage employee data effectively. 
# This system provides essential functionalities for handling employee information efficiently in a structured and user-friendly manner.