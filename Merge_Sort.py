from typing import List
def merge_sort(unsorted_list: List[int])-> List[int]:
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and divide the unsorted list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half: List[int],right_half: List[int]) -> List[int]:

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            del left_half[0]
        else:
            res.append(right_half[0])
            del right_half[0]
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
# You can add any list of numbers here
unsorted_list: List[int] = [6,5,3,1,8,7,2,4]

print(merge_sort(unsorted_list))

