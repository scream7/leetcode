# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        stack = [(root,[str(root.val)])]
        res = []
        while len(stack):
            node,string = stack.pop()
            if node.left is None and node.right is None:
                res.append('->'.join(string))
            if node.left:
                stack.append((node.left,string + [str(node.left.val)]))
            if node.right:
                stack.append((node.right,string + [str(node.right.val)]))
        return res
