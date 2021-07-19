from datetime import datetime, date


def sorting(fn):
    def inner(*args, **kwargs):
        return sorted(fn(*args, **kwargs), key=lambda x: x.created_at)

    return inner


class Dashboard:

    def __init__(self, todos=None):
        self.todos = todos or []

    @staticmethod
    def _parse_date(input_date):
        if isinstance(input_date, datetime):
            return input_date

        try:
            return datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid date format: {input_date}")

    @sorting
    def filter_task_by_date(self, start_date=None, end_date=None):
        start = start_date or datetime.min  # falsy, truthy
        end = end_date or datetime.max

        return [todo for todo in self.todos if
                self._parse_date(start) < todo.created_at < self._parse_date(end)]

    def __str__(self):
        return f"{type(self).__name__}: {[repr(todo) for todo in self.todos]}"
