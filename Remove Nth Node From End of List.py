# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, original, n):
        """
        :type original: ListNode
        :type n: int
        :rtype: ListNode
        """
        asList = []
        head = original
        while original:
            asList.append(original)
            original = original.next
        if n < len(asList):
            asList[-1-n].next = asList[-n].next
        else:
            return head.next
        return head
