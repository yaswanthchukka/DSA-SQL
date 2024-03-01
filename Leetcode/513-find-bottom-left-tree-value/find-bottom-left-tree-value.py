# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bfs(self,root):
        queue=[root]
        child_add=[]
        res=[[root.val]]
        child=[]
        while queue:
            node=queue.pop(0)
            if node.left:
                child_add.append(node.left)
                child.append(node.left.val)
            if node.right:
                child_add.append(node.right)
                child.append(node.right.val)
            if len(queue)==0:
                queue+=child_add
                child_add=[]
                if child:
                    res.append(child)
                    child=[]
        return res
    

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        k=self.bfs(root)
        return k[-1][0]



        