"""
Bubble sort is a simple sorting algorithm that repeatedly steps through a list of elements, 
compares adjacent pairs of elements, and swaps them if they are in he wrong order.
The algorithm gets its name from the way that smaller elements "bubble" to the top of the list
 with each iteration. 

 Suppose we have an unsorted list of numbers: [5, 2, 9, 1, 5]. The first pass 
 through the list would compare the first two elements (5 and 2) and swap them, 
 resulting in [2, 5, 9, 1, 5]. The algorithm would then compare the second and 
 third elements (5 and 9) and leave them in place, resulting in [2, 5, 9, 1, 5]. The 
 next comparison would be between the third and fourth elements (9 and 1), 
 resulting in a swap and a new list of [2, 5, 1, 9, 5]. This process continues until 
 the list is sorted.

 O(n^2)

"""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def main():
	arr = [5, 2, 9, 1, 5]
	print(bubble_sort(arr))


if __name__ == '__main__':
	main()