# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        arr = [root]
        while arr:
            depth += 1
            for i in range(len(arr)):
                k = arr.pop(0)
                if k.left:
                    arr.append(k.left)
                if k.right:
                    arr.append(k.right)
        return depth

        