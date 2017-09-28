# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd, even, head_2 = head, head.next, head.next
            while even and even.next:
                odd.next, even.next, odd, even = odd.next.next, even.next.next, odd.next.next, even.next.next
            odd.next = head_2
        return head
