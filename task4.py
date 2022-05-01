nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

def task4(my_list):
    for item in my_list:
        if isinstance(item, list):
            for element in task4(item):
                yield element
        else:
            yield item

for item in task4(nested_list2):
    print(item)