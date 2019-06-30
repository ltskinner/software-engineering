
from datetime import datetime, timedelta


class WorkDay(object):
    def __init__(self, start_day, off_days):
        self.start_day = start_day
        self.current_day = start_day
        self.off_days = self.convert_string_day_to_int(off_days)

    def get_current_day(self):
        return self.current_day

    def next_work_day(self):
        while True:
            self.current_day = self.increment_day(self.current_day)
            day_of_week = self.current_day.weekday()
            if day_of_week not in self.off_days:
                break

        return self.current_day

    def increment_day(self, day):
        return day + timedelta(days=1)

    @staticmethod
    def convert_string_day_to_int(string_days):
        day_map = {
            'MONDAY': 0,
            'TUESDAY': 1,
            'WEDNESDAY': 2,
            'THURSDAY': 3,
            'FRIDAY': 4,
            'SATURDAY': 5,
            'SUNDAY': 6
        }
        int_days = [day_map[day.upper()] for day in string_days]
        return int_days

if __name__ == "__main__":

    start_day = datetime.today()
    off_days = ["Monday", "Wednesday", "Friday"]
    day_maker = WorkDay(start_day, off_days)

    for _ in range(15):
        day = day_maker.next_work_day()
        print(day.strftime("%Y-%m-%d"))
