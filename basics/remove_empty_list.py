# Given a list containing multiple sublists, the task is to remove all empty sublists from it.
#  Removing empty lists means keeping only the sublists that have at least one element.

# For example:

# a = [[1, 2], [], [3, 4], [], [5]]
# Resulting list = [[1, 2], [3, 4], [5]]

def remove_list(arr):
    for i in arr:
        if i==[]:
            arr.remove(i)
    return arr

a = [[1, 2], [], [3, 4], [], [5]]
print(remove_list(a))


