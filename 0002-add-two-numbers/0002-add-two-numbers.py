# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = sum = 0
        dummy = ListNode() 
        n1 = dummy

        while l1 or l2:
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0

            sum = c1 + c2 + carry
            carry = sum // 10

            n1.next = ListNode(sum%10)
            n1 = n1.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            n1.next = ListNode(carry)

        return dummy.next

