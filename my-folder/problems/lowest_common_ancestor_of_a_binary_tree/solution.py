# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans=None
        
        def dfs(node):    
            if not node:
                return False
            left=dfs(node.left)
            right=dfs(node.right)
            cur= node==p or node==q
            
            if (right and left) or (cur and left) or (cur and right):
                self.ans=node
                return
            return left or right or cur
        dfs(root)
        return self.ans