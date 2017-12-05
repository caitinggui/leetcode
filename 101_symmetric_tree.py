# coding: utf-8

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, 0)]
        level_size = 1
        while stack:
            size = len(stack)
            level_size *= 2
            for _ in xrange(size):
                node, pos = stack.pop(0)
                if node.left:
                    stack.append((node.left, pos * 2))
                if node.right:
                    stack.append((node.right, pos * 2 + 1))
            if stack:
                left = len(stack) / 2 - 1
                right = len(stack) / 2
                # print left, right
                if left + right < len(stack) - 1:    # stack 长度不能为奇数
                    return False
                while left >= 0:
                    ln, lp = stack[left]
                    rn, rp = stack[right]
                    # print ln.val, lp, rn.val, rp
                    left -= 1
                    right += 1
                    if ln.val == rn.val and lp + rp == level_size -1:
                        pass
                    else:
                        return False
        return True


s = Solution()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
assert(s.isSymmetric(t1) is False)

t1.right.val = 2
assert(s.isSymmetric(t1) is True)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)
t2.left.right = TreeNode(3)
t2.right.right = TreeNode(3)
assert(s.isSymmetric(t1) is True)
