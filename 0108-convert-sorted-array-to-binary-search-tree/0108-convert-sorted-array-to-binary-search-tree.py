# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        n = len(nums)
        mid = n//2
        root = TreeNode(nums[mid])

        q = deque()
        q.append((root, 0, mid-1))
        q.append((root, mid+1, n-1))

        while q:
            parent, l, r = q.popleft()
            if l <= r:
                mid = (l+r)//2
                child = TreeNode(nums[mid])
                if nums[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child

                q.append((child, l, mid-1))
                q.append((child, mid+1, r))
        
        return root


