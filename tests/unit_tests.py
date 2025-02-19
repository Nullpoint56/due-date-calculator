import unittest
from datetime import datetime
from src.main import WorkSchedule


class TestCalculateDueDate(unittest.TestCase):

    def setUp(self):
        """Initialize a standard work schedule for testing."""
        self.schedule = WorkSchedule()

    # Standard test cases
    def test_TC01(self):
        """TC01 - Simple case within the same day."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 10, 0), 2),
            datetime(2025, 2, 17, 12, 0)
        )

    def test_TC02(self):
        """TC02 - Crosses into the next working day."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 15, 0), 3),
            datetime(2025, 2, 18, 10, 0)
        )

    def test_TC03(self):
        """TC03 - Starts late in the day and rolls over to the next day."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 16, 30), 2),
            datetime(2025, 2, 18, 10, 30)
        )

    def test_TC04(self):
        """TC04 - Full working day crosses into the next day."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 11, 0), 8),
            datetime(2025, 2, 18, 11, 0)
        )

    def test_TC05(self):
        """TC05 - Ends two working days later."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 16, 0), 16),
            datetime(2025, 2, 19, 16, 0)
        )

    def test_TC06(self):
        """TC06 - Crosses over the weekend."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 21, 14, 0), 6),
            datetime(2025, 2, 24, 12, 0)
        )

    def test_TC07(self):
        """TC07 - Exactly two full working days."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 20, 9, 0), 16),
            datetime(2025, 2, 21, 17, 0)
        )

    def test_TC08(self):
        """TC08 - Rolls over weekend with extra hours."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 20, 14, 0), 24),
            datetime(2025, 2, 25, 14, 0)
        )

    def test_TC09(self):
        """TC09 - Full working week."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 10, 0), 32),
            datetime(2025, 2, 21, 10, 0)
        )

    # Edge cases
    def test_EC01(self):
        """EC01 - Just before closing time, carries to Monday."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 21, 16, 59), 1),
            datetime(2025, 2, 24, 9, 59)
        )

    def test_EC02(self):
        """EC02 - Barely inside working hours."""
        self.assertEqual(
            self.schedule.calculate_due_date(datetime(2025, 2, 17, 9, 1), 1),
            datetime(2025, 2, 17, 10, 1)
        )

    def test_EC03(self):
        """EC03 - Should raise ValueError for submission at 5:00 PM sharp."""
        with self.assertRaises(ValueError):
            self.schedule.calculate_due_date(datetime(2025, 2, 21, 17, 0), 1)

    def test_EC04(self):
        """EC04 - Should raise ValueError for submission before 9:00 AM."""
        with self.assertRaises(ValueError):
            self.schedule.calculate_due_date(datetime(2025, 2, 21, 8, 59), 1)

