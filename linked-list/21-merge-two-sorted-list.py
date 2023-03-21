"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

def mergeLinkedList(l1, l2):
	dummy = ListNode()
	tail = dummy

	while l1 and l2:
		if l1.val < l2.val:
			tail.next = l1
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next
		tail = tail.next
	if l1:
		tail.next = l1
	elif l2:
		tail.next = l2

	return dummy.next