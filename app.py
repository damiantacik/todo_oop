from pprint import pprint

from todo import Todo, TodoWeekend
from generate_data import GenerateData
from dashboard import Dashboard

tasks = []
for task in GenerateData.load_data():
    task_list = task[:-1].split(", ")
    tasks.append(Todo(*task_list))  # * wszystkie parametry dzieki tej gwiazdce

# c = TodoWeekend(1, 'train', 'False', 'Marcin', '2021-07-26 17:49:00', 'None')
d = Dashboard(tasks)
# p = d.filter_task_by_date(end_date="2021-66-01 00:00:00")
p = d.filter_task_by_date()

pprint(p)
print(len(p))
# print(isinstance(c, (Todo, Dashboard)))

