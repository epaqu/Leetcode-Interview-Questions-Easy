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
        asList = []
        while head:
            asList.append(head.val)
            head = head.next
        if asList[::-1] == asList:
            return True
        else:
            return False
