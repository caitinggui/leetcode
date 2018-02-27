# coding: utf-8

'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''


class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这种方法虽然慢一些，但是可以知道最大结果是哪段
        """
        start = 0
        pos = start + 1
        tmp_total = nums[start]
        total = tmp_total
        while pos < len(nums):
            # print(start, pos, tmp_total, total)
            # 判断起点是否为负数
            if nums[start] < 0:
                start += 1
                pos += 1
                tmp_total = nums[start]
                if total < tmp_total:
                    total = tmp_total
                continue
            # 末尾节点为负数
            if nums[pos] < 0:
                # 先把临时结果加进去
                if total < tmp_total:
                    total = tmp_total
                # 如果整段和为负数，那么这段可以舍弃了
                if nums[pos] + tmp_total < 0:
                    start = pos
                    pos += 1
                    continue
            tmp_total += nums[pos]
            pos += 1
        # 最后一次的结果也要合进去
        if total < tmp_total:
            total = tmp_total
        # print(start, pos, tmp_total, total)
        return total

    def maxSubArray(self, nums):
        localMax, globalMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            if localMax < 0:
                localMax = 0
            localMax += nums[i]

            if localMax > globalMax:
                globalMax = localMax
        return globalMax


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums), 6)
nums = [-2, 1]
print(s.maxSubArray(nums), 1)
nums = [-2]
print(s.maxSubArray(nums), -2)
nums = [-2, -1, -2]
print(s.maxSubArray(nums), -1)
"""
只管累加或者记录起点终点
"""
