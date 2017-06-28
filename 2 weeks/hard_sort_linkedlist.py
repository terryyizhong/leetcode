#Sort a linked list in O(n log n) time using constant space complexity.

# regular merge_sortcan do it in O(nlogn) but when use recursion, the depth will cost O(logn) space
# so we need to use bottom to up way to do merge_sort

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        step = 1          # each time, do merge_sort in step 1, 2, 4 ... n
        dummy = ListNode(0)
        dummy.next = head     # to get to head conviniently
        while step < length:
            tail = dummy      #each turn set the start of whole linked-list  
            curr = dummy.next #head at first
            while curr:     # O(n) times in this loop
                left = curr  #
                right = self.split_list(left, step) 
                curr = self.split_list(right, step)
                tail = self.merge_list(left, right, tail)     #input tail is the end of last turn sorted list 
            step <<= 1      # O(logn) times in this loop
        return dummy.next     #totally O(nlogn)
        
    def split_list(self, head, n):    #go forward step length
        for i in range(n - 1):
            if not head:
                break
            head = head.next
        if not head:
            return None
        second = head.next
        head.next = None
        return second
        
    def merge_list(self, l1, l2, head):   # merge two sorted list
        curr = head
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        while curr.next:
            curr = curr.next
        return curr
