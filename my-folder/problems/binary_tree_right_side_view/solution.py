# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l=defaultdict(list)
        def dfs(node,h):
            if not node:return 0
            l[h].append(node.val)
            dfs(node.left,h+1)
            dfs(node.right,h+1)
        
        dfs(root,0)
        
        return [v[-1] for k,v in l.items()]
        