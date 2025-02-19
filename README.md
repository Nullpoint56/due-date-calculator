# Due Date Calculator

## Overview
The **Due Date Calculator** determines the resolution date and time for an issue based on a given submission date and turnaround time in working hours. It accounts for business hours and weekends, ensuring that deadlines are correctly calculated within the specified work schedule.

## Features
- **Configurable Working Hours**: Default working hours are **Monday to Friday, 9:00 AM - 5:00 PM**.
- **Excludes Weekends**: Automatically skips non-working days.
- **Handles Edge Cases**: Ensures tasks submitted near closing time or outside working hours are properly handled.
- **Robust Unit Testing**: Ensures accuracy with various test cases.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Nullpoint56/due-date-calculator.git
    ```

## Usage
The `WorkSchedule` class at [main.py](./src/main.py). provides a method to calculate the due date for a task based on a given submission time and required working hours.

### Example Usage
```python
from datetime import datetime
from src.main import WorkSchedule

schedule = WorkSchedule()
start_time = datetime(2025, 2, 17, 10, 0)  # Monday 10:00 AM
turnaround_time = 16  # 16 working hours (2 full workdays)
due_date = schedule.calculate_due_date(start_time, turnaround_time)
print(due_date)  # Expected output: 2025-02-19 10:00 AM
```

## Running Tests
Unit tests are provided in [unittests.py](./tests/unit_tests.py).
To run tests, use:
```sh
python -m unittest ./tests/unit_tests.py
```

## Coverage Report
To generate and view the coverage report:
```sh
coverage run -m unittest ./tests/unit_tests.py
coverage html
```
The HTML report can be found in the [htmlcov](./htmlcov) directory. Open [index.html](./htmlcov/index.html) in a browser to view detailed coverage results.

## Test Plan
A detailed [Test Plan](./docs/DueDateCalculator_test_Plan.md) outlines different test cases to verify the accuracy of the `CalculateDueDate` method.
