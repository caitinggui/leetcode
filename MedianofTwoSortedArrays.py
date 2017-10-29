#!usr/bin/python
#coding:utf-8


'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(A) + len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2 -1) + self.findKth(A,B,l//2)) / 2.0
        
    def findKth(self, A, B, K):
        if len(A) > len(B):
            A,B = B,A
        if not A:
            return B[k]
        if k == len(A) + len(B) -1:
            return max(A[-1], B[-1])
        i = len(A)//2
        j = k-i
        if A[i] > B[i]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return  self.findKth(A[i:], B[:j], j)
            
            
class Solution_2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        l = len(num)
        mid = l / 2
        if l % 2:
            return num[mid]
        else:
            return (num[mid -1] + num[mid]) / 2.0