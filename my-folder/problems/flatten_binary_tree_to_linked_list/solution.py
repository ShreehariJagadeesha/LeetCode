# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node: return None,None
            left,left2=dfs(node.left)
            right,right2=dfs(node.right)
            node.left=None
            end=node
            if left:
                end.right=left
                end=left2
            if right:
                end.right=right
                end=right2
            return node,end
        dfs(root)
        