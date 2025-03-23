# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            nodes.append(curr.val)
            curr = curr.right

        n = len(nodes)

        def constructBST(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nodes[mid])
            node.left = constructBST(l, mid - 1)
            node.right = constructBST(mid + 1, r)
            return node
            
        return constructBST(0, n - 1)
