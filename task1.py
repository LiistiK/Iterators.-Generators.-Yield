nested_list1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class task1:
    def __init__(self, lst):
        self.lst = sum(lst, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]


for item in task1(nested_list1):
    print(item)
flat_list = [item for item in task1(nested_list1)]
print(flat_list)