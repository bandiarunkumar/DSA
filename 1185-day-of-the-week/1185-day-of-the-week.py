class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(year):
            return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

        week = [
            "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"
        ]

        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        days = 0

        # Count days for previous years
        for y in range(1971, year):
            days += 366 if is_leap(y) else 365

        # Count days for previous months
        for m in range(month - 1):
            days += days_in_month[m]

        # Leap year adjustment
        if month > 2 and is_leap(year):
            days += 1

        # Days in current month
        days += day - 1

        # Jan 1, 1971 was Friday (index 5)
        return week[(days + 5) % 7]