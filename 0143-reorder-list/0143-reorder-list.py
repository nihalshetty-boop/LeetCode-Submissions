# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        prev = slow.next = None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp

        fir, sec = head, prev
        while sec:
            t1, t2 = fir.next, sec.next
            fir.next = sec
            sec.next = t1
            fir, sec = t1, t2
