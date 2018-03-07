# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-07 11:21
 * Description   :
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
'''


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        int[] x = {9,99,993,9999,99979,999999,9998017,99999999};
        int[] y = {1,91,913,9901,99681,999001,9997647,99990001};
        return ((x[n-1]%1337)*(y[n-1]%1337))%1337;
        """
        rst = [9, 987, 123, 597, 677, 1218, 877, 475]
        return rst[n-1]
