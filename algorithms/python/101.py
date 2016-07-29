# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isS(left,right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val !=  right.val:
                return False
            else:
                return _isS(left.left, right.right) and _isS(left.right, right.left)
        
        if root is None:
            return True
        else:
            return _isS(root.left, root.right)
        
