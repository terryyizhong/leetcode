'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow, fast = head.next, head.next.next
        while fast and fast.next:
            if slow != fast:
                slow, fast = slow.next, fast.next.next
            else:
                break
        if not fast or not fast.next:
            return None
        start = head
        while start != slow:
            start, slow = start.next, slow.next
        return start

# beautiful and concise solution:
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:     # can solve prob in this loop if there is a cycle, it break then means no loop
            slow, fast = slow.next, fast.next.next  # head == head 
            if slow == fast:
                start = head
                while start != slow:
                    start, slow = start.next, slow.next
                return start
