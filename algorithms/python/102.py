# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = []
        if root is None:
            return res
        nodes_cnt = 1
        q.append(root)
        while len(q) > 0:
            row = []
            child_nodes_cnt = 0
            for i in range(nodes_cnt):
                node = q.pop(0)
                row.append(node)
                if node.left:
                    child_nodes_cnt += 1
                    q.append(node.left)
                if node.right:
                    child_nodes_cnt += 1
                    q.append(node.right)
            res.append([x.val for x in row])
            nodes_cnt = child_nodes_cnt
        return res
            
        
