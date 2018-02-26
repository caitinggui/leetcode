# coding: utf-8

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''


class Solution(object):
    """前两种方法不考虑由大到小的顺序"""

    def merge(self, nums1, m, nums2, n):
        pos = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
            pos -= 1

        while j >= 0:
            nums1[pos] = nums2[j]
            j -= 1
            pos -= 1

    def merge2(self, nums1, m, nums2, n):
        m_ptr = m + n - 1
        a_ptr = m - 1
        b_ptr = n - 1
        while a_ptr >= 0 and b_ptr >= 0:
            if nums1[a_ptr] > nums2[b_ptr]:
                nums1[m_ptr] = nums1[a_ptr]
                a_ptr -= 1
            else:
                nums1[m_ptr] = nums2[b_ptr]
                b_ptr -= 1
            m_ptr -= 1
        while a_ptr >= 0:
            nums1[m_ptr] = nums1[a_ptr]
            m_ptr -= 1
            a_ptr -= 1
        while b_ptr >= 0:
            nums1[m_ptr] = nums2[b_ptr]
            m_ptr -= 1
            b_ptr -= 1

    def merge3(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 要改变入参的数组，就不能直接赋值
        while len(nums1) > m:
            nums1.pop()
        while len(nums2) > n:
            nums2.pop()
        # nums1 = nums1[:m]
        # nums2 = nums2[:n]
        if not nums2:
            return
        if not nums1:
            while nums1:
                nums1.pop()
            for num in nums2:
                nums1.append(num)
            return
        tmp = []
        n = 0
        big_endian = False
        if nums1[-1] < nums1[0]:
            tmp_nums1 = nums1[::-1]
            big_endian = True
        else:
            tmp_nums1 = nums1
        if nums2[-1] < nums2[0]:
            nums2 = nums2[::-1]
        for num in tmp_nums1:
            while n < len(nums2) and num > nums2[n]:
                tmp.append(nums2[n])
                n += 1
            tmp.append(num)
        if n < len(nums2):
            for num in nums2[n:]:
                tmp.append(num)
        if big_endian:
            tmp = tmp[::-1]
        else:
            tmp = tmp
        while nums1:
            nums1.pop()
        for num in tmp:
            nums1.append(num)
        return


s = Solution()
nums1 = [1, 2, 3, 5, 6, 0, 0]
nums2 = [7, 9]
print(s.merge(nums1, 5, nums2, len(nums2)))
print(nums1)
print([1, 2, 3, 5, 6, 7, 9])

nums1 = [1, 2, 3, 15, 26, 0, 0, 0]
nums2 = [7, 9, 23]
print(s.merge(nums1, 5, nums2, len(nums2)))
print(nums1)
print([1, 2, 3, 7, 9, 15, 23, 26])

nums1 = [26, 25, 3, 2, 1, 0, 0, 0]
nums2 = [23, 9, 7]
print(s.merge(nums1, 5, nums2, len(nums2)))
print(nums1)
print([26, 23, 15, 9, 7, 3, 2, 1])

nums1 = [0]
nums2 = [1]
print(s.merge(nums1, 0, nums2, len(nums2)))
print(nums1)
print([1])
