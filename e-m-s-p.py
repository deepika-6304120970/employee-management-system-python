import json
import os

FILE_NAME = "employees.json"


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "Employee ID": self.emp_id,
            "Name": self.name,
            "Department": self.department,
            "Salary": self.salary
        }


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


employees = load_data()


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = Employee(emp_id, name, department, salary)
    employees.append(employee.to_dict())

    save_data(employees)
    print("Employee Added Successfully!")


def view_employees():
    if not employees:
        print("No Employees Found.")
        return

    for emp in employees:
        print("-" * 40)
        for key, value in emp.items():
            print(f"{key}: {value}")


def search_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["Employee ID"] == emp_id:
            print(emp)
            return

    print("Employee Not Found")


def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    for emp in employees:
        if emp["Employee ID"] == emp_id:
            emp["Name"] = input("New Name: ")
            emp["Department"] = input("New Department: ")
            emp["Salary"] = input("New Salary: ")
            save_data(employees)
            print("Employee Updated Successfully!")
            return

    print("Employee Not Found")


def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    for emp in employees:
        if emp["Employee ID"] == emp_id:
            employees.remove(emp)
            save_data(employees)
            print("Employee Deleted Successfully!")
            return

    print("Employee Not Found")


while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
