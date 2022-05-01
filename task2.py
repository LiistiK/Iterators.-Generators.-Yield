nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

class FlatIteratorList:
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.iter_queue = []
        self.current_iter = iter(self.my_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iter)
            except StopIteration:
                if not self.iter_queue:
                    raise StopIteration
                else:
                    self.current_iter = self.iter_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iter_queue.append(self.current_iter)
                self.current_iter = iter(self.current_element)
            else:
                return self.current_element

for item in FlatIteratorList(nested_list2):
    print(item)

flat_list2 = [item for item in task2(nested_list2)]
print(flat_list2)