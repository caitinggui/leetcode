# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-07 09:47
 * Description   :
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 最好用self.res = [0] * len(nums + 1), 然后用self.res[i] = tmp, 避免数组重新分配空间（涉及到python内存管理)
        self.res = []
        tmp = 0
        for num in nums:
            tmp += num
            self.res.append(tmp)
        # 避免i=0的时候判断，因为0-1=-1,所以直接让-1位的为0即可
        # 也可以首位为0，然后用j+1, i来取值
        self.res.append(0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.res[j] - self.res[i-1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2,0,3,-5,2,-1])
print(obj.sumRange(0, 2), 1)
print
print(obj.sumRange(2, 5), -1)
print
print(obj.sumRange(0, 5), -3)
print
