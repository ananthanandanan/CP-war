"""
Merge sort works on divide and conquer method
Divide the unsorted array into two sub arrays of rougly equal size
Sort the sub arrays recurively by applying merge sort
finally merge two sorted sub arrays to produce final array

Time complexity: O(n log n)

"""

def merge_sort(arr):

	if len(arr)<=1:
		return arr

	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):

	result = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

	result += left[i:]
	result += right[j:]

	return result





def main():
	arr = [5, 2, 9, 1, 5]
	print(merge_sort(arr))


if __name__ == '__main__':
	main()