# Test Cases Report

**Project Title:** Employee Record Management System  
**Course:** MCA Semester I  
**Subject:** Python Programming & Relational Database  
**Module:** File I/O & Console Applications  

---

## Overview

This document records the formal test execution for the **Employee Record Management System**. All tests were executed against the console application using realistic inputs to verify functionality, data integrity, input validation, and exception handling.

---

## Summary of Test Results

| Total Tests | Passed | Failed | Success Rate |
| :---: | :---: | :---: | :---: |
| 16 | 16 | 0 | 100% |

---

## Detailed Test Cases

### Test Case 1: Program Starts
- **Test ID:** TC-01
- **Objective:** Verify that the program launches cleanly and displays the main menu.
- **Input:** Run `python employee_management.py`
- **Expected Output:** Main menu displayed with options 1 to 6.
- **Actual Output:** Main menu displayed with options 1 to 6 without errors.
- **Status:** PASS

---

### Test Case 2: CSV File is Created
- **Test ID:** TC-02
- **Objective:** Verify that `employees.csv` is automatically created with the header row if the file does not exist.
- **Input:** Remove `employees.csv` (if present) and start the application.
- **Expected Output:** File `employees.csv` created containing header: `employee_id,name,age,department,email,salary`.
- **Actual Output:** File `employees.csv` created with the exact header columns.
- **Status:** PASS

---

### Test Case 3: Add Employee (Valid Data)
- **Test ID:** TC-03
- **Objective:** Verify adding a new employee with valid details.
- **Input:**
  - Choice: `1`
  - Employee ID: `104`
  - Name: `Neha Verma`
  - Age: `25`
  - Department: `Finance`
  - Email: `neha.v@company.com`
  - Salary: `36000`
- **Expected Output:** `"Employee added successfully."` and record appended to CSV.
- **Actual Output:** `"Employee added successfully."`
- **Status:** PASS

---

### Test Case 4: Add Duplicate Employee ID
- **Test ID:** TC-04
- **Objective:** Verify that adding an employee with an existing ID is rejected.
- **Input:**
  - Choice: `1`
  - Employee ID: `101`
- **Expected Output:** `"Employee ID already exists."`
- **Actual Output:** `"Employee ID already exists."` (Record not duplicated).
- **Status:** PASS

---

### Test Case 5: View Employees
- **Test ID:** TC-05
- **Objective:** Verify that all employee records are fetched and formatted cleanly in a table.
- **Input:** Choice: `2`
- **Expected Output:** Formatted table showing ID, Name, Age, Department, Email, and Salary for all stored employees.
- **Actual Output:** Tabular display showing existing employee records correctly.
- **Status:** PASS

---

### Test Case 6: Search Existing Employee
- **Test ID:** TC-06
- **Objective:** Verify searching for an employee using a valid existing ID.
- **Input:**
  - Choice: `3`
  - Employee ID: `101`
- **Expected Output:** `"Employee Found"` followed by details of Employee 101.
- **Actual Output:**
  ```text
  Employee Found
  ------------------------------
  Employee ID : 101
  Name        : Rohan
  Age         : 22
  Department  : IT
  Email       : rohan@gmail.com
  Salary      : 30000.0
  ------------------------------
  ```
- **Status:** PASS

---

### Test Case 7: Search Non-Existing Employee
- **Test ID:** TC-07
- **Objective:** Verify that searching for an unknown employee ID is handled properly.
- **Input:**
  - Choice: `3`
  - Employee ID: `999`
- **Expected Output:** `"Employee not found."`
- **Actual Output:** `"Employee not found."`
- **Status:** PASS

---

### Test Case 8: Update Employee (Valid Data)
- **Test ID:** TC-08
- **Objective:** Verify updating an existing employee's details while keeping ID unchanged.
- **Input:**
  - Choice: `4`
  - Employee ID: `102`
  - New Name: `Amit Kumar`
  - New Age: `24`
  - New Department: `HR Operations`
  - New Email: `amit.k@gmail.com`
  - New Salary: `31000`
- **Expected Output:** `"Employee updated successfully."` and updated details reflected in CSV.
- **Actual Output:** `"Employee updated successfully."`
- **Status:** PASS

---

### Test Case 9: Update Non-Existing Employee
- **Test ID:** TC-09
- **Objective:** Verify that attempting to update a non-existing employee displays a friendly error.
- **Input:**
  - Choice: `4`
  - Employee ID: `999`
- **Expected Output:** `"Employee not found."`
- **Actual Output:** `"Employee not found."`
- **Status:** PASS

---

### Test Case 10: Delete Employee (Confirm Yes)
- **Test ID:** TC-10
- **Objective:** Verify that confirming deletion removes the employee record from the CSV file.
- **Input:**
  - Choice: `5`
  - Employee ID: `104`
  - Confirmation: `y`
- **Expected Output:** `"Employee deleted successfully."`
- **Actual Output:** `"Employee deleted successfully."` (Record removed from CSV).
- **Status:** PASS

---

### Test Case 11: Cancel Delete Operation
- **Test ID:** TC-11
- **Objective:** Verify that declining confirmation preserves the record.
- **Input:**
  - Choice: `5`
  - Employee ID: `101`
  - Confirmation: `n`
- **Expected Output:** `"Delete cancelled."` (Record remains in CSV).
- **Actual Output:** `"Delete cancelled."`
- **Status:** PASS

---

### Test Case 12: Input Validation - Invalid Age
- **Test ID:** TC-12
- **Objective:** Verify rejection of ages outside the 18–65 range or non-integer input.
- **Input:**
  - Choice: `1`
  - Employee ID: `105`
  - Name: `Rahul`
  - Age: `72`
- **Expected Output:** `"Invalid age. Age must be between 18 and 65."`
- **Actual Output:** `"Invalid age. Age must be between 18 and 65."`
- **Status:** PASS

---

### Test Case 13: Input Validation - Invalid Salary
- **Test ID:** TC-13
- **Objective:** Verify that negative salary amounts and non-numeric salary values are rejected.
- **Input:**
  - Choice: `1`
  - Employee ID: `105`
  - Name: `Rahul`
  - Age: `25`
  - Department: `Sales`
  - Email: `rahul@gmail.com`
  - Salary: `-4000`
- **Expected Output:** `"Salary cannot be negative."`
- **Actual Output:** `"Salary cannot be negative."`
- **Status:** PASS

---

### Test Case 14: Invalid Menu Choice
- **Test ID:** TC-14
- **Objective:** Verify that choosing an invalid menu option is handled gracefully.
- **Input:** Choice: `9`
- **Expected Output:** `"Invalid choice. Please enter a valid option between 1 and 6."`
- **Actual Output:** `"Invalid choice. Please enter a valid option between 1 and 6."`
- **Status:** PASS

---

### Test Case 15: Exit Application
- **Test ID:** TC-15
- **Objective:** Verify that option 6 terminates the application cleanly.
- **Input:** Choice: `6`
- **Expected Output:** `"Thank you for using the system."` and process exits.
- **Actual Output:** `"Thank you for using the system."`
- **Status:** PASS

---

### Test Case 16: Restart Program and Confirm Saved Records
- **Test ID:** TC-16
- **Objective:** Verify persistence by exiting the application and restarting to check stored records.
- **Input:**
  1. Add record `104`, exit program (`choice = 6`).
  2. Start program again: `python employee_management.py`.
  3. Select choice `2` (View Employees).
- **Expected Output:** Previously added employee `104` is retrieved and displayed from `employees.csv`.
- **Actual Output:** All previously saved records persist across program restarts.
- **Status:** PASS

---

## Conclusion

All 16 test cases were executed and passed. The system functions reliably, enforces data integrity, handles edge cases gracefully, and ensures persistent file storage.
