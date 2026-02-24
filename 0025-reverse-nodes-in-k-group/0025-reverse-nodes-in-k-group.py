# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevgrp = ListNode(0, head)

        while True:
            kth = self.getKth(prevgrp, k)
            if not kth:
                break

            nextgrp = kth.next
            prev, curr = nextgrp, prevgrp.next

            while curr != nextgrp:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevgrp.next
            prevgrp.next = kth
            prevgrp = tmp    
    
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr