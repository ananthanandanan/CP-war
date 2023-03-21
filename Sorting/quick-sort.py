""" 

This follows a divide and conquer approach
Choose a pivot element from the array. The pivot element can be any element in the array, but it's common to choose the first or last element.
Partition the array into two sub-arrays: one sub-array containing elements smaller than the pivot, and another sub-array containing elements greater than or equal to the pivot.
Recursively sort each sub-array by repeating steps 1 and 2.
Combine the sorted sub-arrays to obtain the final sorted array.


worst case : O(n^2)
Average Time complexity: O(n log n)


"""

def quicksort(arr):
	if len(arr)<=1:
		return arr

	pivot = arr[0]
	left = []
	right = []

	for i in range(1, len(arr)):
		if arr[i] < pivot:
			left.append(arr[i])
		else:
			right.append(arr[i])

	return quicksort(left) + [pivot] + quicksort(right)
 

def main():
	arr = [7, 2, 1, 6, 8, 5, 3, 4]
	print(quicksort(arr))


if __name__ == '__main__':
	main()
