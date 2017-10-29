#!usr/bin/python
# coding:utf-8


'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
s = a, bb, abb, 123218888888822222, abcba
'''


class Solution(object):

    def longestPalindrome(self):
        """
        :type s: str
        :rtype: str
        """
        s = "123218888888822222"
        self.s = s
        self.len_s = len(self.s)
        num = 1
        if self.len_s == 1:
            return s
        elif self.len_s == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        result = s[0]

        for num in xrange(self.len_s):
            shortpalindrome1 = self._find_palindrome(num, num + 1)
            if len(result) < len(shortpalindrome1):
                result = shortpalindrome1
            shortpalindrome2 = self._find_palindrome(num - 1, num + 1)
            if len(result) < len(shortpalindrome2):
                result = shortpalindrome2
        return result

    def _find_palindrome(self, startlocation, endlocation):
        while (startlocation >= 0 and endlocation < self.len_s
                and self.s[startlocation] == self.s[endlocation]):
            startlocation -= 1
            endlocation += 1
        # 循环结束时两个location都被多加了1，所以：self.s[startlocation+1: endlocation-1+1]
        return self.s[startlocation + 1: endlocation]

    # 这种扩展法耗时更大
    def find_palindrome(self, num):
        i = 0
        j = 0
        o_flag = False
        print num
        while True:
            if self.s[num - i] == self.s[num + i]:
                i += 1
            else:
                i -= 1
                break
            if num - i < 0 or num + i > self.len_s - 1:
                i -= 1
                break
        shortpalindrome = self.s[num - i:num + i + 1]
        print i, shortpalindrome

        while True:
            if self.s[num + j] == self.s[num - j - 1]:
                j += 1
                o_flag = True
            elif j == 0:
                break
            else:
                j -= 1
                break
            if num + j > self.len_s - 1 or num - j - 1 < 0:
                j -= 1
                break
        if o_flag:
            shortpalindrome_o = self.s[num - j - 1:num + j + 1]
        else:
            shortpalindrome_o = ''
        print j, shortpalindrome_o

        if 2 * i + 1 < len(shortpalindrome_o):
            return j, self.s[num - j - 1:num + j + 1]
        else:
            return i, shortpalindrome


# 这种做法为暴力解法，时间复杂度O(n^3)
s = "123218888888822222"
result = ''
for i in xrange(len(s)):
    for j in xrange(i, len(s)):
        temp_str = s[i:j + 1]
        if temp_str in temp_str[::-1]:
            if len(result) < len(temp_str):
                result = temp_str
print result


class Solution(object):

    def longestPalindrome(self):
        """
        :type s: str
        :rtype: str
        """
        s = '123218888888822222'
        len_s = len(s)
        num = 1
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        result = s[0]
        while num < len_s - 1:
            i = self.find_pa(num, 1, s, len(s))
            if len(result) < 2 * i:
                result = s[num - i:num + i + 1]
            if i == 0:
                num += 1
            else:
                num += i
            # print i, num
        print result
        return result

    def find_palindrome(self, num, s):
        i = 0
        len_s = len(s)
        while s[num - i] == s[num + i]:
            i += 1
            if num < i or num + i > len_s - 1:
                break

        while s[num + i] == s[num - i - 1]:
            i += 1
            if num + i > len_s - 1 or num < i + 1:
                break

        return s

    def is_to_long(self):
        pass

    def find_pa(self, num, i, s, len_s):
        if (num - i < 0) or (num + i > len_s - 1):
            return i - 1
        elif s[num - i] != s[num + i]:
            if s[num] == s[num + i]:
                return 1
            else:
                return i - 1
        else:
            i += 1
            return self.find_pa(num, i, s, len_s)

    # def find_pa(self, num, i, s, len_s):
        # if (num-i<0) or (num+i > len_s-1) or s[num-i] != s[num+i]:
            # return i - 1
        # else:
            # i += 1
            # return self.find_pa(num, i, s, len_s)


a = Solution()
print a.longestPalindrome()
