starting_list = ['a', 'b', 'c', 'd']


def chop(starting_list):
    del starting_list[0]
    del starting_list[-1]


def middle(starting_list):
    return starting_list[1:-1]


print(starting_list)
# chop(starting_list)
# print(starting_list)
print(middle(starting_list))
