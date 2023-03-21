def reverseList(head: ListNode):

	if not head:
		return None

	newHead = head
	if head.next:
		newHead = self.reverseList(head.next)
		head.next.next = head ## reverse the link

	head.next = None
	return newHead

	## -> 4 -> 5 -> 6 