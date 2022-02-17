# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output=[]
        
        def inordertraversersalhelper(node):
            if not node: return None
            output.append(node.val)
            inordertraversersalhelper(node.left)
            inordertraversersalhelper(node.right)
            
        
        inordertraversersalhelper(root)
        return output