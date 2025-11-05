# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        ctr = 0
        while node:
            ctr += 1
            node = node.next

        if ctr == n:
            return head.next
        
        prev = head
        for i in range(ctr - n - 1):
            prev = prev.next
        
        if prev and prev.next:
            prev.next = prev.next.next
        
        return head
        
            


