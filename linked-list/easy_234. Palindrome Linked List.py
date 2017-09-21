'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # reversed the first half linked-list first, and find the mid point
        slow, fast = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next  # all the right hand side is value before assignment, left side will change after assignment
        if fast:
            slow = slow.next  #odd or even case differ here
        while rev and slow:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True
