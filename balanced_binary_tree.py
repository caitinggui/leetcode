# coding: utf-8

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isBalanced(self, root):
        if not root:
            return True
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if self.hasChild(node) == 1:
                    if self.hasChild(node.left) or self.hasChild(node.right):
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        is_balanced = True
        min_depth = self.minDepth(root)
        max_depth = self.maxDepth(root)
        if (not root.left or not root.right) and max_depth > 2:
            is_balanced = False
        return is_balanced and (max_depth - min_depth <= 1)

    def hasChild(self, root):
        if not root:
            return 0
        num = 0
        if root.left:
            num += 1
        if root.right:
            num += 1
        return num

    def isBalancedError(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        is_balanced = True
        min_depth = self.minDepth(root)
        max_depth = self.maxDepth(root)
        if (not root.left or not root.right) and max_depth > 2:
            is_balanced = False
        return is_balanced and (max_depth - min_depth <= 1)

    def minDepth(self, root):
        """正确的解法，速度第一"""
        if not root:
            return 0
        queue = [root]
        level = 1
        while queue:
            size = len(queue)
            # 每层单独一个循环，这样可以很轻松的知道层数
            for i in range(size):
                x = queue.pop(0)
                # print "i, val = ",i, x.val
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                if not x.left and not x.right:
                    return level
            level += 1
        return level

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
print s.isBalanced(tree)
assert s.isBalanced(tree) is True
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
print s.isBalanced(tree)
assert s.isBalanced(tree) is True
tree.left.right = TreeNode(0)
# import pdb; pdb.set_trace()
assert s.isBalanced(tree) is True
tree.right.right.left = TreeNode(0)
assert s.isBalanced(tree) is False
tree.right.right.left.left = TreeNode(0)
assert s.isBalanced(tree) is False

tree2 = TreeNode(0)
tree2.left = TreeNode(0)
tree2.right = TreeNode(0)
tree2.left.left = TreeNode(0)
tree2.left.right = TreeNode(0)
print s.isBalanced(tree2)
assert s.isBalanced(tree2) == True

tree3 = TreeNode(0)
tree3.right = TreeNode(1)
tree3.right.left = TreeNode(2)
assert s.isBalanced(tree3) == False

tree4 = [1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]
