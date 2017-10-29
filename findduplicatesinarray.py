#!/etc/bin/env python
# coding:utf-8 

'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

class Solution(object):
    def _find_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        statuslist = {}
        result = []
        for i, x in enumerate(nums):
            if statuslist.get(x, 0) == 1:
                result.append(x)
            else:
                statuslist[x] = 1
        return result


    def find_duplicates_low_speed(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        status = 0
        result = []
        for x in nums:
            tmp = 1 << x
            if tmp & status != 0:
                result.append(x)
            else:
                status = status | tmp
        return result
        
    def find_duplicates(self, nums):
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
            print nums
        return res



solution = Solution()
print solution.find_duplicates([4,3,2,7,8,2,3,1])

print solution.find_duplicates([])
print solution.find_duplicates([1])
print solution.find_duplicates([1,1])