# coding: utf-8

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the
shortest path from the root node down to the nearest leaf node.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.length_list = []
        self.length = 0
        self.preorder(root)
        print "length_list: ", self.length_list
        if len(self.length_list):
            return min(self.length_list)
        else:
            return 0

    def preorder(self, node):
        if node is None:
            if self.length:
                self.length_list.append(self.length)
            self.length = 0
            return
        else:
            self.length += 1
            print 'length:', self.length
            self.preorder(node.left)
            self.preorder(node.right)

tree = TreeNode(0)
s = Solution()
assert s.minDepth(tree) == 1
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
assert s.minDepth(tree) == 1
tree.left.right = TreeNode(0)
assert s.minDepth(tree) == 2
