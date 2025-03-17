# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = []  
        
        curr = head
        while curr:  
            x.append(curr.val)
            curr = curr.next
        
        return x == x[::-1]  




        