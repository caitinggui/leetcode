# coding: utf-8

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


class Solution(object):
    def rob_error(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        path = {1: {3: {5: {7: {}}, 6: {}, 7: {}}, 4: {}, 5: {}, 6: {}, 7: {}}}
        sum_odd = 0
        sum_even = 0
        for i in range(0, len(nums), 2):
            sum_odd += nums[i]
        for i in range(1, len(nums), 2):
            sum_even += nums[i]
        if sum_odd > sum_even:
            return sum_odd
        else:
            return sum_even

    def rob1(self, nums):
        """f(k) = max(f(k-2) + nums[k], f(k-1))"""
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now

    def rob(self, nums):
        rob = 0  # max monney can get if rob current house
        notrob = 0  # max monney can get if not rob current house
        for num in nums:
            currob = notrob + num  # if rob current value, previous house must not be robbed
            notrob = max(notrob, rob)  # if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            rob = currob
            print currob, rob, notrob
        return max(rob, notrob)


s = Solution()
# nums = [1]
# print(s.rob(nums), 1)
# print
# nums = [1, 2]
# print(s.rob(nums), 2)
# print
# nums = [1, 3, 2]
# print(s.rob(nums), 3)
# print
# nums = [1, 2, 2, 2]
# print(s.rob(nums), 4)
# print
nums = [2, 1, 1, 2]
print(s.rob(nums), 4)
print
