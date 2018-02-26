# coding: utf-8

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 1:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert2(self, nums, target):
        """二分法
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print "start..."
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        left = 0
        right = len(nums) - 1
        mid = 0
        while right - left > 1:
            mid = (right + left) / 2
            print left, right, mid, nums[mid], target
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        print left, right, mid, nums[mid], target
        if target <= nums[right]:
            return right
        else:
            return right + 1

    def searchInsert(self, nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = (low+high) / 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


nums = [1, 3, 5, 6]
s = Solution()
assert(s.searchInsert(nums, 5) == 2)
assert(s.searchInsert(nums, 2) == 1)
assert(s.searchInsert(nums, 7) == 4)
print(s.searchInsert(nums, 0))
assert(s.searchInsert(nums, 0) == 0)
assert(s.searchInsert([1], 1) == 0)
assert(s.searchInsert([1, 3], 1) == 0)
