# coding: utf-8

'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
eg:
[4, 2, 5, 7, 9, 9, 1] -> [4, 2, 5, 7, 9, 9, 2]

[4, 2, 5, 7, 9, 9, 9] -> [4, 2, 5, 9, 0, 0, 0]
'''


class Solution(object):
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 只有尾数为9才会产生进位
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        pos = len(digits) - 1
        while pos > 0 and digits[pos] + 1 == 10:
            digits[pos] = 0
            pos -= 1
        # 查看第一位是否为9, 是9就需要进位，否则直接累加
        if pos == 0 and digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[pos] += 1
        return digits

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = 0
        for digit in digits:
            ans = ans * 10 + digit
        ans += 1
        res = []
        while ans > 0:
            res.append(ans % 10)
            ans = ans / 10
        return res[::-1]


s = Solution()
digits = [4, 2, 5, 7, 9, 9, 1]
print(s.plusOne(digits), [4, 2, 5, 7, 9, 9, 2])
digits = [4, 2, 5, 7, 9, 9, 9]
print(s.plusOne(digits), [4, 2, 5, 8, 0, 0, 0])
digits = [9, 9, 9, 9, 9, 9, 9]
print(s.plusOne(digits), [1, 0, 0, 0, 0, 0, 0, 0])
digits = [8, 9, 9, 9, 9, 9, 9]
print(s.plusOne(digits), [9, 0, 0, 0, 0, 0, 0])
