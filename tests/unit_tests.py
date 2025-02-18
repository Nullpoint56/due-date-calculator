import unittest
from datetime import datetime
from src.helper_methods import is_working_day


class TestIsWorkingDay(unittest.TestCase):
    def test_weekday(self):
        """Monday to Friday should return True."""
        self.assertTrue(is_working_day(datetime(2022, 9, 5)))  # Monday
        self.assertTrue(is_working_day(datetime(2022, 9, 7)))  # Wednesday

    def test_weekend(self):
        """Saturday and Sunday should return False."""
        self.assertFalse(is_working_day(datetime(2022, 9, 10)))  # Saturday
        self.assertFalse(is_working_day(datetime(2022, 9, 11)))  # Sunday

    def test_holiday(self):
        """A public holiday should return False."""
        self.assertFalse(is_working_day(datetime(2022, 12, 26)))  # Example holiday

    def test_non_holiday_weekday(self):
        """A normal working day that is not a holiday should return True."""
        self.assertTrue(is_working_day(datetime(2022, 9, 6)))  # Tuesday