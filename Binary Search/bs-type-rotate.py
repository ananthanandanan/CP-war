"""
The array increases and then decreases
Find the maximux

2 3 4 6 9 12 11 8 6 4 1
T T T T T T  F F  F F F 

So in this situation we are looking for the last T

"""

def binarysearch(arr):
	l = 0
	r = len(arr) - 1
	ans = -1

	while l<=r:
		mid = l + (r-l)//2
		if (mid == 0) or (arr[mid] > arr[mid - 1]):
			ans = mid
			l= mid + 1 ## going to left to check if there are any more greater mid or desired value
		else:
			r = mid - 1
	return ans

def main():
    arr = [2,3,4, 6, 9, 12, 11, 8, 6, 4, 1]
    print(binarysearch(arr))


if __name__ == '__main__':
    main()