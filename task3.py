nested_list1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def task3(my_list):
    for lists in my_list:
        for item in lists:
            yield item

for item in task3(nested_list1):
    print(item)