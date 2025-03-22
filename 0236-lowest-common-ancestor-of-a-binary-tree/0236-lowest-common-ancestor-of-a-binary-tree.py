# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent = {root: None}
        anc = set()

        while queue:
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
                parent[curr.left] = curr

            if curr.right:
                queue.append(curr.right)
                parent[curr.right] = curr

            if p in parent and q in parent:
                break

        while p:
            anc.add(p)
            p = parent[p]

        while q:
            if q in anc:
                return q
            q = parent[q]

            