from typing import List

def partition(arr: List[int], low: int, high: int) -> int:
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr: List[int], low: int, high: int) -> None:
	if len(arr) == 1:
		return
	if low < high:

		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr: List[int] = [6,5,4,1,8,7,3,4]
n: int = len(arr)
quickSort(arr, 0, n-1)
print(arr)
