# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow.next
        prev = slow.next = None


        while start:
            tmp = start.next
            start.next = prev
            prev = start
            start = tmp

        begin, end = head, prev
        while end:
            tmp1, tmp2 = begin.next, end.next
            begin.next = end
            end.next = tmp1
            begin,end = tmp1, tmp2
        