# coding: utf-8

'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        没有用到赋值，所以看起来比较乱
        如果递归的函数参数有列表，在递归的时候，列表是deepcopy的
        """
        def helper(nums, root, left, right):
            if left == right:
                return
            middle = (left + right) / 2
            if nums[left] >= root.val:
                root.right = TreeNode(nums[middle])
                helper(nums, root.right, left, middle)
                helper(nums, root.right, middle + 1, right)
            else:
                root.left = TreeNode(nums[middle])
                helper(nums, root.left, left, middle)
                helper(nums, root.left, middle + 1, right)

        if not nums:
            return
        middle = len(nums) / 2
        root = TreeNode(nums[middle])
        helper(nums, root, 0, middle)
        helper(nums, root, middle + 1, len(nums))
        return root

    def sortedArrayToBST(self, nums):
        """原理其实和上面的一致，都是取列表中间的值去判断，其实有点类似于快排"""
        if not nums:
            return
        middle = len(nums) / 2
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:])
        return root

    def show(self, root):
        if not root:
            return
        print root.val
        self.show(root.left)
        self.show(root.right)


nums = [1, 2, 3, 4, 5]
s = Solution()
tree = s.sortedArrayToBST(nums)
s.show(tree)

nums = [1]
tree = s.sortedArrayToBST(nums)
s.show(tree)

nums = [1, 2]
tree = s.sortedArrayToBST(nums)
s.show(tree)
