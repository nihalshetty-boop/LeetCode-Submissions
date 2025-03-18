# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        maxh = {}
        d = 0

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                if node.left is None:
                    lh = 0
                else:
                    lh = maxh.pop(node.left)
                if node.right is None:
                    rh = 0
                else:
                    rh = maxh.pop(node.right)

                d = max(d, lh+rh)
                maxh[node] = max(lh, rh) + 1
            
        return d
        