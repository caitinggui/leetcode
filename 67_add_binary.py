# coding: utf-8

'''
 Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(self.binary2decimal(int(a)) + self.binary2decimal(int(b)))[2:]

    def binary2decimal(self, num):
        bit = 0
        result = 0
        while num:
            result += num % 10 * 2**bit
            num = num / 10
            bit += 1
        return result

    def addBinary2(self, a, b):
        return bin(int(a, base=2) + int(b, base=2))[2:]


s = Solution()
print(s.addBinary("11", "1"), "100")
