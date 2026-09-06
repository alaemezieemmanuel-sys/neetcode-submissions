# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        current = head
        if current is None:
            return
        while current is not None:
            current = current.next
            sz +=1
        num = (sz-n) + 1
        y = 1
        current = head
        prev = None
        if y == num:
            head = current.next
            return head
        while y < num:
            prev = current
            current = current.next
            y+=1
        prev.next = current.next
        return head


    

