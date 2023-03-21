"""
Find first value >= X

x =4
2,3,5,6,8,10.12

Keep the answer as -1, what we do is when we find the first time it gets the value greater, we store it and hope that there
might another value greater, so we keep on searching. So when loop ends
we just return from function level.
"""



def binarysearch(target, arr):

	l=0
	r = len(arr) -1
	ans = -1

	while l <= r:
		mid = l + (r-l)//2
		if arr[mid] >= target:
			ans = mid
			r = mid - 1
		else:
			l = mid + 1

	return ans


def main():
    arr = [2, 4, 5, 8, 10]
    print(binarysearch(8, arr))


if __name__ == '__main__':
    main()