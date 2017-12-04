# coding: utf-8

'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        参考94_binary_tree_inorder_traversal.py
        """
        if not root:
            return []
        result = []
        stack = [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if not root:
                continue
            if not is_visited:
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
            else:
                result.append(root.val)
        return result

    def postorderTraversalByRecursive(self, root):
        def _postorder(n):
            if not n:
                return
            _postorder(n.left)
            _postorder(n.right)
            result.append(n.val)
        result = []
        _postorder(root)
        return result


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
s = Solution()
print s.postorderTraversalByRecursive(tree)
print s.postorderTraversal(tree)
