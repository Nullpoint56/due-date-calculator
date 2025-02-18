# 📌 Due Date Calculation - TDD Development Plan

## 🔹 Introduction
This document follows the **Test-Driven Development (TDD)** approach to implementing a **Due Date Calculator** for an issue tracking system.

### **🔹 TDD Workflow:**
1️⃣ **Define the required functions based on the problem statement.**  
2️⃣ **Write unit tests first to specify expected behavior.**  
3️⃣ **Implement each function iteratively, ensuring tests pass before proceeding.**  
4️⃣ **Refactor code while keeping all tests green.**

The following sections describe the necessary functions and corresponding unit test cases before implementation.

---
# 🛠 Function Design Breakdown (Before Implementation)

## 1. Checking Working Days
📌 **Function:** `is_working_day(date)`

- **Purpose:** Checks if a given date is a valid working day.
- **Input:** A `datetime` object.
- **Output:** `True` if the date is a working day, otherwise `False`.

---

## 2. Getting the Next Working Day
📌 **Function:** `get_next_working_day(date)`

- **Purpose:** Moves the date forward to the next valid working day if it's on a weekend or holiday.
- **Input:** A `datetime` object.
- **Output:** The next working day's `datetime` at **9:00 AM**.

---

## 3. Calculating Remaining Work Hours in a Day
📌 **Function:** `get_remaining_work_hours_in_day(date)`

- **Purpose:** Determines the number of working hours left in the day from a given time.
- **Input:** A `datetime` object.
- **Output:** Number of hours remaining in the workday (`integer`).

---

## 4. Adding Working Hours to a Date
📌 **Function:** `add_working_hours(start_date, hours)`

- **Purpose:** Adds a given number of working hours, skipping weekends and holidays.
- **Input:** A `datetime` object (`start_date`) and an `integer` (`hours`).
- **Output:** A `datetime` object representing the **calculated due date**.

---

## 5. Main Function: Calculating Due Date
📌 **Function:** `calculate_due_date(submit_date, turnaround_time)`

- **Purpose:** Calls the helper functions to compute the due date.
- **Input:** `submit_date` (a valid working hour) and `turnaround_time` (in working hours).
- **Output:** The calculated `datetime` object.

---
# ✅ Test-Driven Development: Unit Test Plan

## 🔹 1. Testing `is_working_day(date)`

### ✅ Test Cases:
| **Test Scenario**        | **Input Date**       | **Expected Output** |
|--------------------------|----------------------|---------------------|
| Monday is a working day  | 2022-09-05 (Monday)  | `True`              |
| Wednesday is a working day | 2022-09-07 (Wednesday) | `True`              |
| Saturday is not a working day | 2022-09-10 (Saturday) | `False`             |
| Sunday is not a working day | 2022-09-11 (Sunday) | `False`             |
| Holiday is not a working day | 2022-12-26 (Holiday) | `False`             |

---

## 🔹 2. Testing `get_next_working_day(date)`

### ✅ Test Cases:
| **Test Scenario**  | **Input Date** | **Expected Output** |
|--------------------|---------------|---------------------|
| Next working day after Friday | 2022-09-09 (Friday) | 2022-09-12 (Monday at 9:00 AM) |
| Next working day after Sunday | 2022-09-11 (Sunday) | 2022-09-12 (Monday at 9:00 AM) |
| Next working day after holiday | 2022-12-26 (Monday, Holiday) | 2022-12-27 (Tuesday at 9:00 AM) |

---

## 🔹 3. Testing `get_remaining_work_hours_in_day(date)`

### ✅ Test Cases:
| **Test Scenario**  | **Input Time** | **Expected Output** |
|--------------------|---------------|---------------------|
| 10 AM - Time left in workday | 2022-09-05 10:00 AM | `7 hours` |
| 4 PM - Time left in workday | 2022-09-05 16:00 PM | `1 hour` |
| 5 PM (End of workday) | 2022-09-05 17:00 PM | `0 hours` |

---

## 🔹 4. Testing `add_working_hours(start_date, hours)`

### ✅ Test Cases:
| **Test Scenario**  | **Input Start Date & Time** | **Turnaround Hours** | **Expected Output** |
|--------------------|---------------------------|----------------------|---------------------|
| Within same workday | 2022-09-05 10:00 AM | `3 hours` | 2022-09-05 13:00 PM |
| Spanning multiple days | 2022-09-05 14:00 PM | `6 hours` | 2022-09-06 12:00 PM |
| Spanning weekend | 2022-09-09 14:00 PM (Friday) | `6 hours` | 2022-09-12 12:00 PM (Monday) |
| Spanning holiday | 2022-12-23 14:00 PM (Friday) | `6 hours` | 2022-12-27 12:00 PM (Tuesday) |

---

## 🔹 5. Testing `calculate_due_date(submit_date, turnaround_time)`

### ✅ Test Cases:
| **Test Scenario**  | **Submit Date & Time** | **Turnaround Hours** | **Expected Due Date** |
|--------------------|----------------------|----------------------|----------------------|
| Spanning to next day | 2022-09-05 14:12 PM (Monday) | `6 hours` | 2022-09-06 12:12 PM |
| Skipping weekend | 2022-09-09 15:00 PM (Friday) | `5 hours` | 2022-09-12 11:00 AM (Monday) |
| Submission on weekend (invalid) | 2022-09-10 10:00 AM (Saturday) | `4 hours` | **Raise ValueError** |
| Zero turnaround time | 2022-09-05 14:00 PM (Monday) | `0 hours` | 2022-09-05 14:00 PM (Same as submit date) |

---
# 📌 Next Steps (Following TDD)
1️⃣ **Write unit tests for `is_working_day(date)` and ensure it fails.**  
2️⃣ **Implement `is_working_day(date)` to pass the test.**  
3️⃣ **Refactor `is_working_day(date)` to improve efficiency and maintainability.**  
4️⃣ **Repeat for `get_next_working_day()`, `get_remaining_work_hours_in_day()`, etc.**  
5️⃣ **Combine the helper functions into `calculate_due_date()`.**  
6️⃣ **Perform integration testing with all test cases.**
