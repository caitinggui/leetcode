# coding: utf-8

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            tmp = []
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.append(tmp)
        return result[::-1]


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(5)
t1.right.right.left = TreeNode(6)
s = Solution()
print s.levelOrderBottom(t1)
