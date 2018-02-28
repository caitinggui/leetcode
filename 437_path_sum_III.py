# coding: utf-8

'''
You are given a binary tree in which each node contains an integer val.

Find the number of paths that sum to a given val.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the vals are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum1(self, root, sum):
        """遍历节点，然后计算每个节点的path num"""
        if not root:
            return 0
        stack = [root]
        all = 0
        while stack:
            stack_len = len(stack)
            for i in range(stack_len):
                node = stack.pop(0)
                if node:
                    all += self.helper(node, sum)
                    stack.append(node.left)
                    stack.append(node.right)
        return all

    def helper(self, root, sum):
        """当前节点符合答案的路径数"""
        if not root:
            return 0
        all = 0
        if root.val == sum:
            all += 1
        all += self.helper(root.left, sum - root.val)
        all += self.helper(root.right, sum - root.val)
        # print root.val, sum, all
        return all

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(root, mapping, pSum):
            if not root:
                return 0
            pSum += root.val
            # get number of ways that end at the current node
            res = mapping.get(pSum - sum, 0)
            mapping[pSum] = mapping.get(pSum, 0) + 1  # update number of ways
            res += helper(root.left, mapping, pSum) + \
                helper(root.right, mapping, pSum)
            print mapping
            mapping[pSum] -= 1  # update number of ways
            return res
        mapping = {0: 1}
        res = helper(root, mapping, 0)
        return res


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(3)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

s = Solution()
print(s.pathSum(root, 18), 3)

# 笨方法：每个节点遍历，每个节点计算
