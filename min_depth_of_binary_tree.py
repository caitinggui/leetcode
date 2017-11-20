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
        """正确的解法，速度第二"""
        if not root:
            return 0
        tree_stack = []
        stop = "tier"
        depth = 1
        has_child = 0
        tree_stack.append(root)
        tree_stack.append(stop)
        while len(tree_stack) > 0:
            node = tree_stack.pop(0)
            has_child = 0
            if node == "tier":
                # 已经遍历完一层，所以层数加1，并且加上分层符
                depth += 1
                tree_stack.append(stop)
                continue
            if node.left:
                tree_stack.append(node.left)
                has_child += 1
            if node.right:
                tree_stack.append(node.right)
                has_child += 1
            if has_child == 0:
                # 无子节点，说明遇到最浅的树了
                break
        return depth

    def minDepth2(self, root):
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

    def minDepth3(self, root):
        """正确的解法，速度第三"""
        if not root:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1

    def minDepthError(self, root):
        """错误的解法
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
# import pdb; pdb.set_trace()
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
