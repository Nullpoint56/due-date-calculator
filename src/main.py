from datetime import datetime, timedelta


def calculate_due_date(start_datetime: datetime, duration_hours: float) -> datetime:
    WORK_START_HOUR = 9
    WORK_END_HOUR = 17

    # Ensure the start datetime is within working hours
    if start_datetime.weekday() >= 5 or start_datetime.hour < WORK_START_HOUR or start_datetime.hour >= WORK_END_HOUR:
        raise ValueError("start_datetime must be within working hours (Monday to Friday, 9:00-17:00)")

    remaining_hours = duration_hours
    current_datetime = start_datetime

    while remaining_hours > 0:
        # Calculate time left in current workday
        workday_end = current_datetime.replace(hour=WORK_END_HOUR, minute=0, second=0)
        time_available_today = (workday_end - current_datetime).total_seconds() / 3600

        if remaining_hours <= time_available_today:
            # Task finishes within the current workday
            return current_datetime + timedelta(hours=remaining_hours)
        else:
            # Task exceeds current workday, move to next workday
            remaining_hours -= time_available_today
            next_workday = current_datetime + timedelta(days=1)
            while next_workday.weekday() >= 5:  # Skip weekends
                next_workday += timedelta(days=1)
            current_datetime = next_workday.replace(hour=WORK_START_HOUR, minute=0, second=0)

    return current_datetime
