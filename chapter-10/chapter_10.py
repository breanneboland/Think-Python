# Exercise 10-1
def nested_sum(lst):
    total = 0
    for item in lst:
        total += sum(item)
    print(total)

# nested_sum([[1, 2, 3], [4, 5, 6]])
# nested_sum([[0, 1, 2]])

# Exercise 10-2
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(list_strs):
    new_list = []
    for item in list_strs:
        new_list.append(capitalize_all(item))
    print(new_list)

# capitalize_nested([["pig", "chicken"], ["hoot"]])

# Exercise 10-3
def cumulative_sum(lst):
    new_summed_list = []
    temp_sum = 0
    for item in lst:
        temp_sum += item
        new_summed_list.append(temp_sum)
    print(new_summed_list)

# cumulative_sum([1, 2, 3])
# cumulative_sum([4, 1, 5])

# Exercise 10-4
def middle(lst):
    last_index = len(lst) -1
    new_list = []
    new_list.append(lst[0])
    new_list.append(lst[last_index])

    print(new_list)

# middle(["hi", "there", "oh", "cool"])
# middle([1, 2, 3, 4, 5, 6])

# Exercise 10-5
def chop(lst):
    last_index = len(lst) - 1
    lst.pop(0)
    lst.pop()
    return(None)

# chop([1, 2, 3, 4])
# chop(["apple", "chicken", "purple", "shelf"])

# Exercise 10-6
def is_sorted(lst):
    last_item = lst[0]
    lst_last_index = len(lst) - 1
    for index, item in enumerate(lst):
        if item >= last_item and index < lst_last_index:
            pass
            last_item = item
        elif item > last_item and index == lst_last_index:
            print(True)
        else:
            print(False)

is_sorted([1, 2, 3])
is_sorted(["a", "c", "b"])
