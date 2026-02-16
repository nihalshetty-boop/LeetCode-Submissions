# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(a, b):
            dummy = curr = ListNode() 
            while a and b:
                if a.val < b.val:
                    curr.next = a
                    a, curr = a.next, a
                
                else:
                    curr.next = b
                    b, curr = b.next, b
                
            if a or b:
                curr.next = a if a else b

            return dummy.next

        if not lists or len(lists) == 0:
            return None

        for i in range(1,len(lists)):
            lists[i] = merge2Lists(lists[i - 1], lists[i])

        return lists[-1]