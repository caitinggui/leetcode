# coding: utf-8

'''
 You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version > 0:
        return True
    return False


class Solution(object):
    def firstBadVersion_error(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) / 2
            mid_flag = isBadVersion(mid)
            mid_front_flag = isBadVersion(mid - 1)
            if not mid_flag and mid_front_flag:
                return mid
            elif mid_flag:
                left = mid
            else:
                right = mid
        return

    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.firstBadVersion(7), 1)
print(s.firstBadVersion(1), 1)
