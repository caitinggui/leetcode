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

    def isBalanced2(self, root):
        """判断左右子树的最大高度差是否正确，效率太低"""
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        t2 = self.isBalanced(root.left)
        t3 = self.isBalanced(root.right)
        return t2 and t3

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

    def isBalanced(self, root):
        """利用helper一边计算左右子树高度时，一边判断子树是否平衡"""
        self.is_balanced = True
        self.helper(root)
        return self.is_balanced

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if abs(left - right) > 1:
            self.is_balanced = False
        return max(left, right) + 1


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

# tree4 = [1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]
