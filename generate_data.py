import datetime
import random


class GenerateData:

    def __init__(self):
        self.names = ["do homework", "train", "clean"]
        self.statuses = [True, False]
        self.owners = ["Damian", "Mateusz", "Marcin"]

    def generate_data(self, amount):
        with open("data.txt", "w") as file:
            lines = []
            for no in range(1, amount + 1):

                created_at = datetime.datetime(2021, random.randint(1, 12), random.randint(1, 28),
                                               random.randint(0, 23), random.randint(0, 59))
                status = random.choice(self.statuses)
                if status:
                    finished_at = created_at + datetime.timedelta(days=float(random.randint(2, 15)),
                                                                  seconds=float(random.randint(1000, 10000)))
                else:
                    finished_at = None

                line = f"{no}, {random.choice(self.names)}, {status}, {random.choice(self.owners)}, {created_at}, {finished_at}\n"
                lines.append(line)
            file.writelines(lines)

    @staticmethod
    def load_data():
        with open("data.txt", "r") as file:
            return file.readlines()