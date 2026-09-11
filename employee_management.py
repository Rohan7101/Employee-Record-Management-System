# ==========================================================
# MCA Semester I - Python Programming & Relational Database
# Assignment 1: Employee Record Management System
# ==========================================================

import csv
import os

# CSV File Name constant
FILE_NAME = "employees.csv"

# Field names for CSV storage
FIELDNAMES = ["employee_id", "name", "age", "department", "email", "salary"]


def create_file():
    """
    Creates the CSV file with appropriate headers if it does not already exist.
    """
    try:
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
    except (PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)


def check_employee_exists(employee_id):
    """
    Checks if an employee ID already exists in the CSV file.
    Returns True if found, False otherwise.
    """
    try:
        if not os.path.exists(FILE_NAME):
            return False

        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["employee_id"] == employee_id:
                    return True
        return False
    except (FileNotFoundError, PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)
        return False


def add_employee():
    """
    Prompts user for employee details, validates input,
    and appends the new record to the CSV file.
    """
    print("\n--- Add New Employee ---")

    # Validate Employee ID
    employee_id = input("Enter Employee ID: ").strip()
    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    if not employee_id.isdigit():
        print("Invalid input. Employee ID must be a numeric value.")
        return

    if check_employee_exists(employee_id):
        print("Employee ID already exists.")
        return

    # Validate Name
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    # Validate Age
    try:
        age = int(input("Enter Age: ").strip())
        if age < 18 or age > 65:
            print("Invalid age. Age must be between 18 and 65.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for age.")
        return

    # Validate Department
    department = input("Enter Department: ").strip()
    if not department:
        print("Department cannot be empty.")
        return

    # Validate Email
    email = input("Enter Email: ").strip()
    if not email or "@" not in email or "." not in email:
        print("Invalid email format. Please enter a valid email address.")
        return

    # Validate Salary
    try:
        salary = float(input("Enter Salary: ").strip())
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for salary.")
        return

    # Represent employee using a dictionary
    new_employee = {
        "employee_id": employee_id,
        "name": name,
        "age": str(age),
        "department": department,
        "email": email,
        "salary": str(salary)
    }

    # Write the employee record to CSV
    try:
        with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow(new_employee)
        print("\nEmployee added successfully.")
    except (PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)


def view_employees():
    """
    Reads all employee records from the CSV file and displays them in tabular format.
    """
    print("\n--- View Employees ---")

    try:
        if not os.path.exists(FILE_NAME):
            print("No employee records found.")
            return

        employees = []
        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)

        if not employees:
            print("No employee records found.")
            return

        # Display header and records in formatted table
        print("-" * 75)
        print(f"{'ID':<8}{'Name':<15}{'Age':<8}{'Department':<15}{'Email':<20}{'Salary':<10}")
        print("-" * 75)
        for emp in employees:
            print(f"{emp['employee_id']:<8}{emp['name']:<15}{emp['age']:<8}{emp['department']:<15}{emp['email']:<20}{emp['salary']:<10}")
        print("-" * 75)

    except (FileNotFoundError, PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)


def search_employee():
    """
    Searches for an employee record by Employee ID and displays their details.
    """
    print("\n--- Search Employee ---")

    employee_id = input("Enter Employee ID: ").strip()
    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    try:
        if not os.path.exists(FILE_NAME):
            print("Employee not found.")
            return

        found = False
        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["employee_id"] == employee_id:
                    print("\nEmployee Found")
                    print("-" * 30)
                    print(f"Employee ID : {row['employee_id']}")
                    print(f"Name        : {row['name']}")
                    print(f"Age         : {row['age']}")
                    print(f"Department  : {row['department']}")
                    print(f"Email       : {row['email']}")
                    print(f"Salary      : {row['salary']}")
                    print("-" * 30)
                    found = True
                    break

        if not found:
            print("Employee not found.")

    except (FileNotFoundError, PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)


def update_employee():
    """
    Updates details of an existing employee by Employee ID.
    Employee ID remains unchanged.
    """
    print("\n--- Update Employee ---")

    employee_id = input("Enter Employee ID to update: ").strip()
    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    try:
        if not os.path.exists(FILE_NAME):
            print("Employee not found.")
            return

        employees = []
        found = False

        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["employee_id"] == employee_id:
                    found = True
                    print(f"\nEmployee found with Name: {row['name']}, Department: {row['department']}")

                    # Prompt for updated values
                    new_name = input("Enter new Name: ").strip()
                    if not new_name:
                        print("Name cannot be empty. Update cancelled.")
                        return

                    try:
                        new_age = int(input("Enter new Age: ").strip())
                        if new_age < 18 or new_age > 65:
                            print("Invalid age. Age must be between 18 and 65. Update cancelled.")
                            return
                    except ValueError:
                        print("Invalid input. Please enter a number for age. Update cancelled.")
                        return

                    new_dept = input("Enter new Department: ").strip()
                    if not new_dept:
                        print("Department cannot be empty. Update cancelled.")
                        return

                    new_email = input("Enter new Email: ").strip()
                    if not new_email or "@" not in new_email or "." not in new_email:
                        print("Invalid email format. Update cancelled.")
                        return

                    try:
                        new_salary = float(input("Enter new Salary: ").strip())
                        if new_salary < 0:
                            print("Salary cannot be negative. Update cancelled.")
                            return
                    except ValueError:
                        print("Invalid input. Please enter a number for salary. Update cancelled.")
                        return

                    # Update the record dictionary
                    row["name"] = new_name
                    row["age"] = str(new_age)
                    row["department"] = new_dept
                    row["email"] = new_email
                    row["salary"] = str(new_salary)

                employees.append(row)

        if not found:
            print("Employee not found.")
            return

        # Write updated list of employees back to CSV
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(employees)

        print("\nEmployee updated successfully.")

    except (FileNotFoundError, PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)


def delete_employee():
    """
    Deletes an employee record by Employee ID after confirmation.
    """
    print("\n--- Delete Employee ---")

    employee_id = input("Enter Employee ID to delete: ").strip()
    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    try:
        if not os.path.exists(FILE_NAME):
            print("Employee not found.")
            return

        employees = []
        found = False

        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["employee_id"] == employee_id:
                    found = True
                else:
                    employees.append(row)

        if not found:
            print("Employee not found.")
            return

        confirm = input("Are you sure you want to delete this employee? (y/n): ").strip().lower()
        if confirm == "y":
            with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(employees)
            print("Employee deleted successfully.")
        else:
            print("Delete cancelled.")

    except (FileNotFoundError, PermissionError, IOError) as e:
        print("Error while accessing employee file:", e)


def show_menu():
    """
    Prints the main interactive menu for the user.
    """
    print("\n========================================")
    print("     EMPLOYEE RECORD MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    print("========================================")


def main():
    """
    Main function to run the Employee Record Management System loop.
    """
    # Ensure CSV file and header exist
    create_file()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

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
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please enter a valid option between 1 and 6.")


if __name__ == "__main__":
    main()
