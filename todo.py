from datetime import datetime


class Todo:
    def __init__(self, idx, name, status, owner, created_at, finished_at=None):
        self.idx = idx
        self.owner = owner
        self.created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        self.status = status
        self.name = name
        self.finished_at = None if finished_at == "None" or finished_at is None else datetime.strptime(finished_at,
                                                                                                       "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Todo {self.idx}. {self.name.capitalize()}, start: {self.created_at:'%m-%d %H:%M'}, stop: {'not today' if self.finished_at is None else self.finished_at}"
