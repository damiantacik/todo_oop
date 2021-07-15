from todo import Todo
from generate_data import GenerateData

for task in GenerateData.load_data():
    task_list = task[:-1].split(", ")
    t = Todo(*task_list)
    print(t)