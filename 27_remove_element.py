# coding: utf-8
'''
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution(object):
    def removeElement_slow(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 1
        for v in nums[::-1]:
            if v == val:
                nums.pop(-i)
            else:
                i += 1
            print(nums, i)
        return len(nums)

    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            # 把与val不同的项从头开始覆盖原列表
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            print(nums)
        return i


if __name__ == "__main__":
    s = Solution()
    print s.removeElement([3, 2, 2, 3], 3)
    print(s.removeElement([], 0))
    print(s.removeElement([1], 1))
