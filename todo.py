from datetime import datetime


class Todo:
    def __init__(self, name, status, owner, finished_at=None):
        self.owner = owner
        self.created_at = datetime.now()
        self.status = status
        self.name = name
        self.finished_at = finished_at

    def __str__(self):
        return f"Todo {self.name}, created_at: {self.created_at}"
