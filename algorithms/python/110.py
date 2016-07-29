# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _treeDepth(node):
            if node is None:
                return 0
            else:
                return 1 + max(_treeDepth(node.left), _treeDepth(node.right))
        
        if root is None:
            return True
        else:
            return abs(_treeDepth(root.left)-_treeDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
