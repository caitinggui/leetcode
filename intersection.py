#!usr/bin/python
# coding:utf-8

from leetcode import quicksort

class Solution(object):

    def intersection_own(self, nums1, nums2):
        Sorted = quicksort.Solution()
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums1 = Sorted.quicksort(nums1)
        nums2 = Sorted.quicksort(nums2)
        print nums1, '---', nums2
        result = []
        i = j = 0
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        while i < len_nums1 and j < len_nums2:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
                continue
            elif nums1[i] > nums2[j]:
                i += 1
            else:
                j += 1
        print result
        return result
    def intersection(self, nums1, nums2):
        if not (nums1 and nums2):
            return []
        nums1 = set(nums1)
        nums1 = sorted(nums1)
        nums2 = set(nums2)
        nums2 = sorted(nums2)
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        i = j = 0
        result = []
        while i < len_nums1 and j < len_nums2:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
        
solution = Solution()
assert(solution.intersection([1,2,5,7,3,4], [1,5,5,4]) == [1,4,5])
        