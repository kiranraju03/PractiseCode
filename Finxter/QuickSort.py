"""
Sorting : Quick Sort
"""

def sortList(list_sort):
    if len(list_sort) < 2:
        return list_sort
    else:
        return sortList([x for x in list_sort[1:] if x < list_sort[0]]) + [list_sort[0]] + \
               sortList([x for x in list_sort[1:] if x >= list_sort[0]])

print(sortList([6,4,12,5,3]))