"""

"""

def binarysearch(target, arr):

	l=0
	r = len(arr) -1

	while l <= r:
		mid = l + (r-l)//2
		if arr[mid] == target:
			return mid

		if arr[mid] < target:
			l = mid + 1

		else:
			r = mid - 1
	return -1


def main():
    arr = [2, 4, 5, 8, 10]
    print(binarysearch(8, arr))


if __name__ == '__main__':
    main()