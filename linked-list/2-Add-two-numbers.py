# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            val = 0
            val+=carry
            if l1:
                val +=l1.val
                l1 = l1.next
            if l2:
                val +=l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            newNode = ListNode()
            newNode.val += val

            tail.next = newNode
            tail = newNode

        return dummy.next

""" Logic and time complexity
1. Create a dummy node and a tail node
2. Create a carry variable and set it to 0
3. While l1 or l2 or carry is true
4. Create a val variable and set it to 0
5. Add carry to val
6. If l1 is true, add l1.val to val and set l1 to l1.next
7. If l2 is true, add l2.val to val and set l2 to l2.next
8. Set carry to val//10 and val to val%10
9. Create a new node and set its value to val
10. Set tail.next to the new node and set tail to the new node
11. Return dummy.next
Time complexity: O(max(m,n)) where m and n are the lengths of l1 and l2 respectively
"""