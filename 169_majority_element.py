# coding: utf-8

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''


class Solution(object):
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key, value in freq.iteritems():
            if value > n:
                return key

    def majorityElement1(self, nums):
        """消除不同的元素，剩下的一定是最多的那个，因为最多的大于n/2，极端情况下最多的元素一一和其他元素消除
        剩下的还是最多的元素"""
        key, count = None, 0
        for num in nums:
            if count == 0:
                key, count = num, 1
            elif num == key:
                count += 1
            else:
                count -= 1
            print key, count
        return key

    def majorityElement(self, nums):
        return sorted(nums)[len(nums)/2]


s = Solution()
nums = [1]
# print(s.majorityElement(nums), 1)
nums = [1, 1, 3, 4, 5, 1, 1]
print(s.majorityElement(nums), 1)
