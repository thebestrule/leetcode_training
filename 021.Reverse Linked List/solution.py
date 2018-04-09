# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        i = 0
        while p.next:
            if i > 0:
                l = p.next
                l.next = p
            else:
                p.next = None
                i += 1
                continue

        head.next = l


