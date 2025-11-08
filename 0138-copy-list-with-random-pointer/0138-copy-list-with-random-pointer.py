"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        LLmap = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            LLmap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = LLmap[curr]
            copy.next = LLmap[curr.next]
            copy.random = LLmap[curr.random]
            curr = curr.next

        return LLmap[head]
