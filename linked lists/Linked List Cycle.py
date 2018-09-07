# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        runner = head
        walker = head
        while walker and runner:
            walker = walker.next
            runner = runner.next
            if not runner:
                return False
            runner = runner.next
            if walker == runner:
                return True
        return False
    
