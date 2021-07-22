# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            if root is None:
                return []
            in_left=inorder(root.left)
            root_val=[root.val]
            in_right=inorder(root.right)
            return in_left+root_val+in_right
        
        return inorder(root)[k-1]