from typing import List

def insertion_sort(InputList: List[int]) -> None:
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
# you can add list of any numbers
list: List[int] = [6,5,3,1,8,7,2,4]
insertion_sort(list)
print(list)