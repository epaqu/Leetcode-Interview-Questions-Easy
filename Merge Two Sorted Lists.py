# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1
        if l1.val < l2.val:
            current = head = l1
            n1 = l1.next
            n2 = l2
        else:
            current = head = l2
            n1 = l1
            n2 = l2.next

        while n1 and n2:
            if n1.val < n2.val:
                current.next = n1
                n1 = n1.next
                current = current.next
            else:
                current.next = n2
                n2 = n2.next
                current = current.next
        if n1 and not n2:
            current.next = n1
        elif not n1 and n2:
            current.next = n2
        return head
