# Employee Record Management System

This is a simple console-based Python project for managing employee records.

This project is created for **Programming with Python & Relational Databases, Assignment 1**.

## Description

The Employee Record Management System allows the user to:

* Add employee records
* View employee records
* Search for an employee
* Update employee details
* Delete an employee
* Save records in a CSV file

The employee data is stored in `employees.csv`, so the records are available even after closing the program.

## Features

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit

The program also checks user input and handles common errors.

## Technologies Used

* Python 3
* CSV
* File Handling
* Python Standard Library

## Python Concepts Used

The project uses the following Python concepts:

* Variables and Data Types
* `if`, `elif`, and `else`
* `for` and `while` loops
* Functions
* Lists and Dictionaries
* `try` and `except`
* File Handling
* CSV File Handling
* Menu-driven programming

## Employee Details

Each employee record contains:

* Employee ID
* Name
* Age
* Department
* Email
* Salary

Example:

```text
101, Rohan, 22, IT, rohan@gmail.com, 30000
```

## Project Structure

```text
Employee-Record-Management-System/
│
├── employee_management.py
├── employees.csv
├── README.md
├── Assignment_Report.md
├── .gitignore
│
└── screenshots/
    ├── main_menu.png
    ├── add_employee.png
    ├── view_employees.png
    ├── search_employee.png
    ├── update_employee.png
    ├── delete_employee.png
    └── error_handling.png
```

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Open the Project Folder

Open Command Prompt or PowerShell and go to the project folder.

```bash
cd Employee-Record-Management-System
```

### Step 3: Run the Program

```bash
python employee_management.py
```

The main menu will appear.

## Main Menu

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

Enter your choice:
```

## CSV File

The employee records are stored in:

```text
employees.csv
```

The file is created automatically if it does not already exist.

## Screenshots

Screenshots of the program are available in the `screenshots` folder.

They include:

* Main Menu
* Add Employee
* View Employees
* Search Employee
* Update Employee
* Delete Employee
* Error Handling

## GitHub Repository

GitHub Repository:(https://github.com/Rohan7101/Employee-Record-Management-System)

## Author

**Name:** Rohan Gurunath Gaikar

**Course:** MCA Semester I

**Subject:** Programming with Python & Relational Databases
