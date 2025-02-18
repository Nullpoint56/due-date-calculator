from datetime import datetime, timedelta

class WorkSchedule:
    def __init__(self, work_start_hour: int = 9, work_end_hour: int = 17, workdays: tuple = (0, 1, 2, 3, 4)):
        """Initialize with configurable work hours and workdays."""
        self.work_start_hour = work_start_hour
        self.work_end_hour = work_end_hour
        self.workdays = frozenset(workdays)  # Use frozenset for better performance and immutability

    def get_next_workday(self, date: datetime) -> datetime:
        """Returns the next valid workday starting at work_start_hour."""
        days_to_add = 1
        while (date + timedelta(days=days_to_add)).weekday() not in self.workdays:
            days_to_add += 1
        next_day = date + timedelta(days=days_to_add)
        return next_day.replace(hour=self.work_start_hour, minute=0, second=0)

    def is_within_working_hours(self, date: datetime) -> bool:
        """Checks if the given datetime falls within configured working hours and workdays."""
        return date.weekday() in self.workdays and self.work_start_hour <= date.hour < self.work_end_hour

    def calculate_due_date(self, start_datetime: datetime, duration_hours: float) -> datetime:
        """Calculates the due datetime for a task, considering only working hours."""
        if not self.is_within_working_hours(start_datetime):
            raise ValueError(
                f"start_datetime must be within working hours ({self.work_start_hour}:00-{self.work_end_hour}:00)")

        remaining_hours = duration_hours
        current_datetime = start_datetime

        while remaining_hours > 0:
            # Calculate time left in current workday
            workday_end = current_datetime.replace(hour=self.work_end_hour, minute=0, second=0)
            time_available_today = (workday_end - current_datetime).total_seconds() / 3600  # More accurate calculation

            if remaining_hours <= time_available_today:
                return current_datetime + timedelta(hours=remaining_hours)
            else:
                remaining_hours -= time_available_today
                current_datetime = self.get_next_workday(current_datetime)

        return current_datetime
