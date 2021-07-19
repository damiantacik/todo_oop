from datetime import datetime


class Todo:
    def __init__(self, idx, name, status, owner, created_at, finished_at=None):
        self.idx = int(idx)
        self.owner = owner
        self.created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        self.status = True if status == "True" or status is True else False
        self.name = name
        self.finished_at = None if finished_at == "None" or finished_at is None else datetime.strptime(finished_at,
                                                                                                       "%Y-%m-%d %H:%M:%S")

    def __str__(self):  # reprezentacja tekstowa obiektu (bardzej dla uzytkownikow)
        return f"{type(self).__name__} {self.idx}. {self.name.capitalize()}, start: {self.created_at:'%m-%d %H:%M'}, stop: {'not today' if self.finished_at is None else self.finished_at}"

    def __repr__(self):  # reprezentacja obiektu (bardziej dla programistow)
        return f"{type(self).__name__}(idx='{self.idx}', name='{self.name}', status='{self.status}', owner='{self.owner}', created_at='{self.created_at}', finished_at='{self.finished_at}')"


# slef.__class__.__name__ = type(self).__name__
class TodoWeekend(Todo):
    pass
