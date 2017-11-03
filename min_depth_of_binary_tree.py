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
        if not root:
            return 0
        if root.left:
            return self.minDepth(root.left) + 1
        elif root.right:
            return self.minDepth(root.right) + 1
        else:
            min_left = self.minDepth(root.left)
            min_right = self.minDepth(root.right)
            return min(min_left+1, min_right+1)
        # node = root
        # min_left = self.minDepth(node.left)
        # min_right = self.minDepth(node.right)
        # if not node.left and not node.right:

        # self.length_list = []
        # self.length = 0
        # self.preorder(root)
        # print "length_list: ", self.length_list
        # if len(self.length_list):
            # return min(self.length_list)
        # else:
            # return 0

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
print s.minDepth(tree)
assert s.minDepth(tree) == 1
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
print s.minDepth(tree)
assert s.minDepth(tree) == 2
tree.left.right = TreeNode(0)
assert s.minDepth(tree) == 3
tree.right.right.left = TreeNode(0)
assert s.minDepth(tree) == 3
tree.left.right.left = TreeNode(0)
assert s.minDepth(tree) == 4

tree2 = TreeNode(0)
tree2.left = TreeNode(0)
tree2.right = TreeNode(0)
tree2.left.left = TreeNode(0)
tree2.left.right = TreeNode(0)
print s.minDepth(tree)
assert s.minDepth(tree2) == 2
