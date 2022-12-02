from helper import load_input


def sort_by_cals():
    input = load_input("01").split("\n\n")
    cals = [sum(map(int, user.split("\n"))) for user in input]
    cals.sort()
    return cals


sorted_cals = sort_by_cals()


print("User with most cals:", sorted_cals[-1])
print("Top 3 users with most cals:", sum(sorted_cals[-3:]))
