# Test Plan for `CalculateDueDate` Method

## Overview
The `CalculateDueDate` method determines the resolution date/time for an issue based on:
- **Input:** Submission date/time and turnaround time (in working hours).
- **Output:** The resolved date/time.
- **Working hours:** Monday to Friday, 9:00 AM - 5:00 PM.
- **Holidays:** Ignored.
- **Turnaround time:** Given in working hours (e.g., 16 hours = 2 working days).
- **Submission time:** Must be strictly between 9:00 AM and 5:00 PM.

---

## Test Cases

| **Test Case ID** | **Input Submit Date/Time**    | **Input Turnaround Time (Hours)** | **Expected Output (Resolved Date/Time)** | **Description**                                        |
|------------------|-------------------------------|-----------------------------------|------------------------------------------|--------------------------------------------------------|
| **TC01**         | 2025-02-17 10:00 AM (Monday)  | 2                                 | 2025-02-17 12:00 PM (Monday)             | Simple case within the same day.                       |
| **TC02**         | 2025-02-17 3:00 PM (Monday)   | 3                                 | 2025-02-18 10:00 AM (Tuesday)            | Crosses into the next working day.                     |
| **TC03**         | 2025-02-17 4:30 PM (Monday)   | 2                                 | 2025-02-18 10:30 AM (Tuesday)            | Starts late in the day and rolls over to the next day. |
| **TC04**         | 2025-02-17 11:00 AM (Monday)  | 8                                 | 2025-02-18 11:00 AM (Tuesday)            | Full working day (8 hours) crosses into the next day.  |
| **TC05**         | 2025-02-17 4:00 PM (Monday)   | 8                                 | 2025-02-19 10:00 AM (Wednesday)          | Ends two working days later.                           |
| **TC06**         | 2025-02-21 2:00 PM (Friday)   | 6                                 | 2025-02-24 12:00 PM (Monday)             | Crosses over the weekend.                              |
| **TC07**         | 2025-02-21 4:00 PM (Friday)   | 2                                 | 2025-02-24 10:00 AM (Monday)             | Rolls over to Monday morning.                          |
| **TC08**         | 2025-02-20 9:00 AM (Thursday) | 16                                | 2025-02-21 5:00 PM (Friday)              | Exactly two full working days.                         |
| **TC09**         | 2025-02-20 2:00 PM (Thursday) | 20                                | 2025-02-24 2:00 PM (Monday)              | Rolls over weekend with extra hours.                   |
| **TC10**         | 2025-02-17 10:00 AM (Monday)  | 40                                | 2025-02-21 10:00 AM (Friday)             | Full working week.                                     |
| **TC11**         | 2025-02-14 3:00 PM (Friday)   | 16                                | 2025-02-18 3:00 PM (Tuesday)             | Rolls over weekend into Tuesday.                       |
| **TC12**         | 2025-02-14 3:00 PM (Friday)   | 24                                | 2025-02-19 3:00 PM (Wednesday)           | Crosses over a full weekend and into midweek.          |
| **TC13**         | 2025-02-18 9:30 AM (Tuesday)  | 0                                 | 2025-02-18 9:30 AM (Tuesday)             | Zero-hour turnaround should return the same timestamp. |

---

## Edge Cases

| **Test Case ID** | **Input Submit Date/Time**  | **Input Turnaround Time (Hours)** | **Expected Output (Resolved Date/Time)** | **Description**                                          |
|------------------|-----------------------------|-----------------------------------|------------------------------------------|----------------------------------------------------------|
| **EC01**         | 2025-02-21 4:59 PM (Friday) | 1                                 | 2025-02-24 9:59 AM (Monday)              | Just before closing time, carries to Monday.             |
| **EC02**         | 2025-02-17 9:01 AM (Monday) | 1                                 | 2025-02-17 10:01 AM (Monday)             | Barely inside working hours.                             |
| **EC03**         | 2025-02-17 4:59 PM (Monday) | 1                                 | 2025-02-18 9:59 AM (Tuesday)             | Last possible moment before closing.                     |
| **EC04**         | 2025-02-21 5:00 PM (Friday) | 1                                 | **ValueError**                           | Should raise ValueError for submission at 5:00 PM sharp. |
| **EC05**         | 2025-02-21 8:59 AM (Friday) | 1                                 | **ValueError**                           | Should raise ValueError for submission before 9:00 AM.   |
