# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-05 18:35
 * Description   : bin或者%或者&

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''


class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for x in bin(n)[2:]:
            if x == '1':
                res += 1
        return res

    def hammingWeight2(self, n):
        res = 0
        while n:
            if n % 2:
                res += 1
            n = n / 2
        return res

    def hammingWeight(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count


s = Solution()
print(s.hammingWeight(11), 3)
