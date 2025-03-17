# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(1)
        dummy.next = head

        lprev, curr = dummy, head
        for i in range(left-1):
            lprev = curr
            curr = curr.next

        prev = None
        for i in range(right-left+1):
            np = curr.next
            curr.next = prev
            prev = curr
            curr = np

        lprev.next.next = curr
        lprev.next = prev
        
        return dummy.next
            

        
