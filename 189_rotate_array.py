# coding: utf-8

'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]
Hint:
Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II
'''


class Solution(object):
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate2(self, nums, k):
        if not nums:
            return
        k = k % len(nums)
        if k == 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        # nums[-k:], nums[k:] = nums[:k], nums[-k:]

    def rotate(self, nums, k):
        if not nums:
            return
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 3)
print(nums, [5,6,7,1,2,3,4])
print

nums = []
s.rotate(nums, 0)
print(nums, [])
print

nums = [1]
s.rotate(nums, 0)
print(nums, [1])
print

nums = [1, 2]
s.rotate(nums, 5)
print(nums, [2, 1])
print

nums = [1, 2]
s.rotate(nums, 0)
print(nums, [1, 2])
print
