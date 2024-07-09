def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


def bubble_sort(lst):
    for cycle in range(len(lst)):
        for i in range(len(lst) - 1 - cycle):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


class SortPrinter:
    def __init__(self):
        self.lst = []
        self.method = None

    def insert(self, data):
        self.lst.append(data)

    def selection(self, method):
        self.method = method

    def run(self):
        self.method(self.lst)

    def show(self):
        print(self.lst)


a = SortPrinter()
a.insert(2)
a.insert(3)
a.insert(1)
a.insert(6)
a.insert(4)
a.insert(9)
a.selection(bubble_sort)
a.run()
a.show()
a.insert(0)
a.selection(selection_sort)
a.run()
a.show()
