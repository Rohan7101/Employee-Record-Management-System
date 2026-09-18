# MCA Semester I – Assignment 1

# Employee Record Management System

---

## 1. Cover Page

**PROJECT REPORT**

**Project Title:** Employee Record Management System

**Course:** Master of Computer Applications (MCA)
**Semester:** I
**Subject:** Python Programming & Relational Database
**Assignment:** Assignment 1 – Console Record-Management Application

---

## 2. Student Details

* **Student Name:** Rohan Gurunath Gaikar
* **Roll Number:** 40
* **Course:** MCA
* **Semester:** I
* **Subject:** Programming with Python & Relational Databases
* **College:** ITM Skill University 
* **Academic Year:** 2026-2027

---

## 3. Project Title

**Employee Record Management System**

This is a console-based Python application used to store and manage employee records using a CSV file.

---

## 4. Introduction

Employee information needs to be stored properly so that it can be viewed and changed when required. In this project, I have created a simple Employee Record Management System using Python.

The application runs in the console and allows the user to add, view, search, update, and delete employee records.

The records are stored in a CSV file named `employees.csv`. Because the data is stored in a file, the records are available even after the program is closed.

This project helped me understand basic Python programming concepts such as variables, data types, conditions, loops, functions, exception handling, and file handling.

---

## 5. Problem Statement

Managing employee information manually can become difficult when the number of records increases.

The purpose of this project is to create a simple program that can manage employee records through a menu-driven console application.

The program should allow the user to:

* Add a new employee
* View employee records
* Search for an employee
* Update an employee record
* Delete an employee record

The records should also be saved permanently using a CSV file.

---

## 6. Objectives

The main objectives of this project are:

1. To create a menu-driven Python application.
2. To learn how to use functions in Python.
3. To use variables and different data types.
4. To use `if`, `elif`, and `else` statements.
5. To use loops for repeated operations.
6. To understand exception handling.
7. To learn how to read and write CSV files.
8. To create a simple application for managing employee records.
9. To make sure that records are not lost when the program is closed.

---

## 7. Scope of the Project

The project includes:

* Adding employee records
* Viewing all employee records
* Searching for an employee using Employee ID
* Updating employee information
* Deleting employee records
* Saving records in a CSV file
* Checking user input
* Handling common errors

The project does not include:

* Login system
* Online database
* Web application
* Mobile application
* Multiple users working at the same time
* Advanced employee management features

---

## 8. Technologies Used

The following technologies and tools are used:

* **Programming Language:** Python 3
* **File Format:** CSV
* **Python Module:** `csv`
* **File Handling:** Python File I/O
* **Interface:** Console / Command Line

No external Python packages are required.

---

## 9. Python Concepts Used

### 9.1 Variables and Data Types

Different variables are used to store employee information.

Examples:

* Employee ID – String
* Name – String
* Age – Integer
* Department – String
* Email – String
* Salary – Float

Other variables such as `choice` and `found` are also used in the program.

### 9.2 Conditional Statements

`if`, `elif`, and `else` are used for making decisions.

For example, the program checks the user's menu choice and performs the selected operation.

### 9.3 Loops

A `while` loop is used to keep the main menu running until the user selects the Exit option.

A `for` loop is used to go through employee records when reading or searching the CSV file.

### 9.4 Functions

Different functions are created for different operations.

For example:

* `add_employee()`
* `view_employees()`
* `search_employee()`
* `update_employee()`
* `delete_employee()`

This makes the program easier to read and manage.

### 9.5 Lists and Dictionaries

Dictionaries are used to represent employee records.

For example:

```python
employee = {
    "employee_id": "101",
    "name": "Rohan",
    "age": "22",
    "department": "IT",
    "email": "rohan@gmail.com",
    "salary": "30000"
}
```

A list can be used to store multiple employee records when updating or deleting records.

### 9.6 Exception Handling

`try` and `except` are used to handle errors.

For example, if the user enters text instead of a number for age, the program displays an error message instead of stopping.

### 9.7 File I/O

The program uses file handling to save and retrieve employee information.

The CSV file is opened using `open()` and the `csv` module is used to read and write records.

---

## 10. Features of the Application

### Add Employee

The user can enter a new employee's details and save them to the CSV file.

### View Employees

The user can view all the employee records stored in the file.

### Search Employee

The user can search for an employee using the Employee ID.

### Update Employee

The user can update the details of an existing employee.

### Delete Employee

The user can delete an employee after confirming the deletion.

### Input Validation

The program checks values such as age and salary before saving them.

### Exception Handling

The program handles invalid input and common file-related errors.

### CSV Storage

Employee records are stored in `employees.csv`, so the information remains available after the program is closed.

---

## 11. System Working

When the program starts, it first checks whether the `employees.csv` file exists.

If the file does not exist, the program creates it with the required column names.

After that, the main menu is displayed.

The user can select one of the following options:

```text
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
```

The selected operation is performed and then the main menu is shown again.

The program continues until the user selects the Exit option.

---

## 12. Menu Structure

```text
========================================
     EMPLOYEE RECORD MANAGEMENT SYSTEM
========================================
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
========================================
Enter your choice:
```

---

## 13. Employee Record Format

The CSV file contains the following columns:

```text
employee_id,name,age,department,email,salary
```

Example:

```text
101,Rohan,22,IT,rohan@gmail.com,30000
102,Amit,23,HR,amit@gmail.com,28000
103,Priya,22,Finance,priya@gmail.com,32000
```

---

## 14. File Handling

The project uses the Python `csv` module for storing employee records.

### Reading Records

The program reads records from `employees.csv` when displaying or searching for employees.

### Adding Records

When a new employee is added, the record is written to the CSV file.

### Updating Records

For an update, the existing records are read into a list. The required employee record is changed and the records are written back to the CSV file.

### Deleting Records

For deletion, the records are read and the selected employee is removed. The remaining records are then written back to the file.

The file is opened using `with open()` so that it is properly closed after the operation.

---

## 15. Exception Handling

Exception handling is used to prevent common errors from stopping the program.

For example, if the user enters an invalid value for age:

```python
try:
    age = int(input("Enter Age: "))
except ValueError:
    print("Please enter a valid number.")
```

File-related errors are also handled where required.

This makes the program easier to use and prevents unexpected termination for common input errors.

---

## 16. Functions Used

| Function            | Purpose                                   |
| ------------------- | ----------------------------------------- |
| `create_file()`     | Creates the CSV file if it does not exist |
| `add_employee()`    | Adds a new employee                       |
| `view_employees()`  | Displays all employee records             |
| `search_employee()` | Searches for an employee                  |
| `update_employee()` | Updates an employee record                |
| `delete_employee()` | Deletes an employee record                |
| `show_menu()`       | Displays the main menu                    |
| `main()`            | Controls the main program                 |

The exact function names may be adjusted according to the final source code.

---

## 17. Basic Algorithm

### Add Employee

1. Select **Add Employee** from the menu.
2. Enter Employee ID.
3. Check whether the ID already exists.
4. Enter employee name.
5. Enter age.
6. Enter department.
7. Enter email.
8. Enter salary.
9. Validate the entered information.
10. Save the employee record in the CSV file.
11. Display a success message.

### Search Employee

1. Select **Search Employee**.
2. Enter Employee ID.
3. Read employee records from the CSV file.
4. Compare the entered ID with each record.
5. Display the employee details if found.
6. Display "Employee not found" if there is no matching record.

### Update Employee

1. Select **Update Employee**.
2. Enter Employee ID.
3. Read the employee records.
4. Find the matching employee.
5. Enter the new information.
6. Update the record.
7. Save the updated records to the CSV file.

### Delete Employee

1. Select **Delete Employee**.
2. Enter Employee ID.
3. Find the employee.
4. Ask for confirmation.
5. Remove the record if confirmed.
6. Save the remaining records.

---

## 18. Sample Input and Output

### Adding an Employee

```text
Enter your choice: 1

Enter Employee ID: 104
Enter Name: Neha
Enter Age: 25
Enter Department: Finance
Enter Email: neha@gmail.com
Enter Salary: 36000

Employee added successfully.
```

### Viewing Employees

```text
Enter your choice: 2

ID     Name       Age    Department    Email              Salary
----------------------------------------------------------------
101    Rohan      22     IT            rohan@gmail.com    30000
102    Amit       23     HR            amit@gmail.com     28000
103    Priya      22     Finance       priya@gmail.com    32000
104    Neha       25     Finance       neha@gmail.com     36000
```

### Searching an Employee

```text
Enter your choice: 3

Enter Employee ID: 101

Employee Found

Employee ID : 101
Name        : Rohan
Age         : 22
Department  : IT
Email       : rohan@gmail.com
Salary      : 30000
```

### Invalid Input

```text
Enter Age: abc

Invalid input. Please enter a valid number.
```

---

## 19. Testing

The application should be tested before submission.

The following test cases can be performed:

| No. | Test                     | Expected Result                 |
| --- | ------------------------ | ------------------------------- |
| 1   | Start program            | Main menu appears               |
| 2   | Add employee             | Employee is saved               |
| 3   | Add duplicate ID         | Duplicate is rejected           |
| 4   | View employees           | Records are displayed           |
| 5   | Search existing employee | Employee details are displayed  |
| 6   | Search wrong ID          | Employee not found message      |
| 7   | Update employee          | Record is updated               |
| 8   | Delete employee          | Record is deleted               |
| 9   | Cancel delete            | Record remains                  |
| 10  | Enter invalid age        | Error message displayed         |
| 11  | Enter invalid salary     | Error message displayed         |
| 12  | Enter wrong menu choice  | Invalid choice message          |
| 13  | Restart program          | Previously saved records remain |
| 14  | Exit program             | Program closes normally         |

**Testing Result:**
The final result should be filled in after actually testing the application.

---

## 20. Advantages

* Simple and easy to use.
* Easy to understand for a beginner.
* No external packages are required.
* Employee records are saved permanently.
* CSV files can also be opened using spreadsheet software.
* Basic errors are handled using exception handling.
* The program is divided into separate functions.

---

## 21. Limitations

The application also has some limitations:

* It works only through the console.
* It does not have a login system.
* It uses a CSV file instead of a database.
* It is mainly suitable for a small number of employee records.
* It does not support multiple users at the same time.

---

## 22. Future Enhancements

The project can be improved in the future by:

* Adding a graphical user interface.
* Adding a login system.
* Adding more employee information.
* Adding sorting and filtering.
* Using a relational database such as MySQL.
* Creating reports from employee records.

---

## 23. Conclusion

The Employee Record Management System is a simple Python console application developed for MCA Semester I Assignment 1.

The project demonstrates the main Python concepts required in the assignment, including variables, data types, conditional statements, loops, functions, exception handling, data structures, and File I/O.

Employee records are stored in a CSV file, which allows the data to remain available after the program is closed.

Through this project, I was able to understand how basic Python concepts can be combined to create a working record-management application.

---

## 24. GitHub Repository

**GitHub Repository:** (https://github.com/Rohan7101/Employee-Record-Management-System)

The repository contains:

* Python source code
* CSV data file
* README file
* Assignment report
* Test cases
* Screenshots

---

## 25. References

1. Python Documentation – Python 3
   https://docs.python.org/3/

2. Python `csv` module documentation
   https://docs.python.org/3/library/csv.html

3. Class notes and study material provided for Python Programming.

