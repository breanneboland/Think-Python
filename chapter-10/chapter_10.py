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

capitalize_nested([["pig", "chicken"], ["hoot"]])
