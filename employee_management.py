import csv
import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "employees.csv")
FIELDNAMES = ["employee_id", "name", "age", "department", "email", "salary"]


def load_employees():
    employees = []
    if not os.path.exists(FILE_NAME):
        return employees
    try:
        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except OSError as e:
        print(f"Error reading file: {e}")
    return employees


def save_employees(employees):
    try:
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(employees)
        return True
    except OSError as e:
        print(f"Error saving to file: {e}")
        return False


def add_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID: ").strip()
    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    for emp in employees:
        if emp["employee_id"] == emp_id:
            print("Employee ID already exists.")
            return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: ").strip())
        if age <= 0:
            print("Age must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Age must be an integer.")
        return

    department = input("Enter Department: ").strip()
    if not department:
        print("Department cannot be empty.")
        return

    email = input("Enter Email: ").strip()
    if not email or "@" not in email:
        print("Invalid email address.")
        return

    try:
        salary = float(input("Enter Salary: ").strip())
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Salary must be a number.")
        return

    new_emp = {
        "employee_id": emp_id,
        "name": name,
        "age": str(age),
        "department": department,
        "email": email,
        "salary": str(salary)
    }

    employees.append(new_emp)
    if save_employees(employees):
        print("Employee added successfully.")


def view_employees():
    employees = load_employees()
    if not employees:
        print("No employee records found.")
        return

    print("\n" + "=" * 85)
    print(f"{'ID':<10} {'Name':<15} {'Age':<6} {'Department':<15} {'Email':<25} {'Salary':<10}")
    print("-" * 85)
    for emp in employees:
        print(f"{emp['employee_id']:<10} {emp['name']:<15} {emp['age']:<6} {emp['department']:<15} {emp['email']:<25} {emp['salary']:<10}")
    print("=" * 85)


def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    employees = load_employees()

    for emp in employees:
        if emp["employee_id"] == emp_id:
            print("\nEmployee Found:")
            print(f"ID         : {emp['employee_id']}")
            print(f"Name       : {emp['name']}")
            print(f"Age        : {emp['age']}")
            print(f"Department : {emp['department']}")
            print(f"Email      : {emp['email']}")
            print(f"Salary     : {emp['salary']}")
            return

    print("Employee not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ").strip()
    employees = load_employees()

    for emp in employees:
        if emp["employee_id"] == emp_id:
            print(f"\nUpdating details for {emp['name']} (leave blank to keep current):")

            name = input(f"New Name [{emp['name']}]: ").strip()
            if name:
                emp["name"] = name

            age_input = input(f"New Age [{emp['age']}]: ").strip()
            if age_input:
                try:
                    age = int(age_input)
                    if age <= 0:
                        print("Age must be greater than 0.")
                        return
                    emp["age"] = str(age)
                except ValueError:
                    print("Invalid input. Age must be an integer.")
                    return

            dept = input(f"New Department [{emp['department']}]: ").strip()
            if dept:
                emp["department"] = dept

            email = input(f"New Email [{emp['email']}]: ").strip()
            if email:
                if "@" not in email:
                    print("Invalid email address.")
                    return
                emp["email"] = email

            salary_input = input(f"New Salary [{emp['salary']}]: ").strip()
            if salary_input:
                try:
                    salary = float(salary_input)
                    if salary < 0:
                        print("Salary cannot be negative.")
                        return
                    emp["salary"] = str(salary)
                except ValueError:
                    print("Invalid input. Salary must be a number.")
                    return

            if save_employees(employees):
                print("Employee updated successfully.")
            return

    print("Employee not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()
    employees = load_employees()

    for i, emp in enumerate(employees):
        if emp["employee_id"] == emp_id:
            employees.pop(i)
            if save_employees(employees):
                print("Employee deleted successfully.")
            return

    print("Employee not found.")


def main():
    while True:
        print("\n--- Employee Record Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

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
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
