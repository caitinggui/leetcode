# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-15 17:04
 * Description   : 判断一个数是不是2的指数结果
Given an integer, write a function to determine if it is a power of two.
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))
