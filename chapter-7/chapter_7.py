# Exercise 7-1
def print_n(s, n):
    if n <= 0:
        return
    while n > 0:
        print(s)
        n = n -1

# print_n("hello kittens", 5)

# Exercise 7-4
def eval_o_matic():
    submission = ""
    while submission != "done":
        submission = input("> ")
        print(eval(submission))

eval_o_matic()