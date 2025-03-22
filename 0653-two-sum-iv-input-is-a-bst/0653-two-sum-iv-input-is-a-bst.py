# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        nums = set()

        while q:
            curr = q.popleft()
            if (k-curr.val) in nums:
                return True
            else:
                nums.add(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return False

