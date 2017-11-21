# coding: utf-8

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level


tree = TreeNode(0)
s = Solution()
print s.maxDepth(tree)
assert s.maxDepth(tree) == 1
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
print s.maxDepth(tree)
assert s.maxDepth(tree) == 3
tree.left.right = TreeNode(0)
# import pdb; pdb.set_trace()
assert s.maxDepth(tree) == 3
tree.right.right.left = TreeNode(0)
assert s.maxDepth(tree) == 4
tree.left.right.left = TreeNode(0)
assert s.maxDepth(tree) == 4

tree2 = TreeNode(0)
tree2.left = TreeNode(0)
tree2.right = TreeNode(0)
tree2.left.left = TreeNode(0)
tree2.left.right = TreeNode(0)
print s.maxDepth(tree)
assert s.maxDepth(tree2) == 3
