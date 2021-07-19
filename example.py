# l = [1, 34, 332, 4]
#
# text = list('Ala ma Kota')
#
# result = sorted(text, reverse=True)  #  funkcja sortuje liste i zwraca nowa liste i nie dotyka oryginalu - create new sorted list
# l.sort()            # metoda modyfikuje oryginana liste
# print(result)


data = [
    {"name": "andrzej", "age": 10, "hobby": "sport"},
    {"name": "Mati", "age": 16, "hobby": "sport"},
    {"name": "Damian", "age": 56, "hobby": "sport"},
    {"name": "Damian", "age": 45, "hobby": "it"}
]

result = sorted(data, key=lambda x: (x["name"][-2].upper(), x["age"]))
print(result)
