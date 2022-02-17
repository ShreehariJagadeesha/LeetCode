# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output=[]
        
        def inordertraversersalhelper(node):
            if not node: return None
            inordertraversersalhelper(node.left)
            
            inordertraversersalhelper(node.right)
            output.append(node.val)
        
        inordertraversersalhelper(root)
        return output