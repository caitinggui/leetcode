# coding: utf-8

'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):
    def thirdMax_slow(self, nums):
        """用一个数组记录第1，第2，第3大的值
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        result = [min(nums)] * 3
        for num in nums:
            print(result)
            if num > result[0]:
                result[1], result[2] = result[0], result[1]
                result[0] = num
            elif num > result[1]:
                result[2] = result[1]
                result[1] = num
            elif num > result[2]:
                result[2] = num
        if result[1] == result[2]:
            return result[0]
        else:
            return result[2]

    def thirdMax_slow2(self, nums):
        result = [None, None, None]
        for num in nums:
            print(result)
            if num > result[0]:
                result[1:] = result[:-1]
                result[0] = num
            elif num > result[1] and num != result[0]:
                result[2] = result[1]
                result[1] = num
            elif num > result[2] and num not in result[:2]:
                result[2] = num
        if result[2] is not None:
            return result[2]
        return result[0]

    def thirdMax(self, nums):
        first_max = None
        second_max = None
        third_max = None
        for member in nums:
            if member > first_max:
                third_max = second_max
                second_max = first_max
                first_max = member
            elif member > second_max and first_max != member:
                third_max = second_max
                second_max = member
            elif member > third_max and second_max != member and first_max != member:
                third_max = member
        if third_max == None:
            return first_max
        return third_max


s = Solution()
nums = [3, 2, 1]
print(s.thirdMax(nums), 1)
print

nums = [2, 1]
print(s.thirdMax(nums), 2)
print

nums = [2, 2, 3, 1]
print(s.thirdMax(nums), 1)
print

nums = [2]
print(s.thirdMax(nums), 2)
print
