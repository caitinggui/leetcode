# coding: utf-8

'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        record = 2**len(nums)
        for num in nums:
            record = record | 0x1 << num - 1
        result = []
        record = bin(record)[3:]
        for k, v in enumerate(record[::-1]):
            if v == "0":
                result.append(k + 1)
        return result


s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums), [5, 6])
nums = [1,1]
print(s.findDisappearedNumbers(nums), [2])
