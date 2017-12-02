# coding: utf-8

'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:  # 右节点后出栈，所以要先压栈
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def preorder(self, root):

        def helper(n):
            if not n:
                return
            result.append(n.val)
            helper(n.left)
            helper(n.right)
        result = []
        helper(root)
        return result


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
s = Solution()
print s.preorderTraversal(tree)
print s.preorder(tree)
