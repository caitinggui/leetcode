# coding: utf-8

'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        这种更好理解一些
        """
        if not root:
            return []
        stack = [root]
        used_stack = []    # 记录已经遍历过的节点，就是节点的值已经取出
        result = []
        while stack:
            node = stack.pop()
            # 右节点可能之前已经压栈，所以要判断一些是否在栈中,左节点无需判断
            if node.right and node.right not in stack and node.right not in used_stack:
                stack.append(node.right)
            # 判断是否遍历过
            if node.left and node.left not in used_stack:
                stack.append(node)    # 根节点继续压栈
                stack.append(node.left)
            else:
                result.append(node.val)
                used_stack.append(node)
        return result

    def inorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [(root, False)]    # 多加个值记录该节点是否已遍历
        while stack:
            node, is_visited = stack.pop()
            if not node:
                continue
            # 不管是根节点还是叶子节点都会被压栈2次,第一次时is_visited都是False
            if not is_visited:
                stack.append((node.right, False))
                stack.append((node, True))    # 已经遍历过一次根节点了
                stack.append((node.left, False))
            else:
                result.append(node.val)
        return result

    def inorderTraversalByRecursive(self, root):
        def _inorder(n):
            if not n:
                return
            _inorder(n.left)
            result.append(n.val)
            _inorder(n.right)
        result = []
        _inorder(root)
        return result


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
s = Solution()
print s.inorderTraversal(tree)
print s.inorderTraversalByRecursive(tree)
