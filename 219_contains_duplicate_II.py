# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-07 11:04
 * Description   :

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''


class Solution(object):
    def containsNearbyDuplicate_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res = {}
        for i, num in enumerate(nums):
            if num in res:
                if i - res[num] <= k:
                    return True
                else:
                    res[num] = i  # 更新最新的位置
            else:
                res[num] = i
        return False

    def containsNearbyDuplicate(self, nums, k):
        """和上面的区别在于去掉多余的else"""
        res = {}
        for i, num in enumerate(nums):
            if num in res and i - res[num] <= k:
                return True
            res[num] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 1], 0), False)
