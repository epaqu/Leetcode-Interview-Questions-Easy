# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, original):
        """
        :type original: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not original or not original.next:
            return original
        prev = original
        original = original.next
        prev.next = None
        while original and original.next:
            curr = original
            nxt = original.next
            curr.next = prev
            prev = original
            original = nxt
            #1->2->3->4->5->NULL
            #1<>2  3->4->5->NULL
            #1<>2<-3  4->5->NULL
            #1<>2<-3<-4  5->NULL
        original.next = prev
        return original
