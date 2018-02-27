# coding: utf-8

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
题意是n=1时输出字符串1；n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；n=3时，由于上次字符是11，有2个1，所以输出21；n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。依次类推，写个countAndSay(n)函数返回字符串。
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ['1', '11', '21', '1211', '111221']
        while n > len(result):
            current = result[-1]
            start = 0
            pos = 1
            next = ''
            while pos < len(current):
                if current[pos] == current[start]:
                    pos += 1
                else:
                    next = next + str(pos - start) + current[start]
                    # next += [str(pos - start), current[start]]
                    start = pos
            next = next + str(pos - start) + current[start]
            # next += [str(pos - start), current[start]]
            result.append(''.join(next))
        return result[n - 1]


s = Solution()
print(s.countAndSay(1), 1)
print(s.countAndSay(2), 11)
print(s.countAndSay(5), 111221)
print(s.countAndSay(6), 312211)
print(s.countAndSay(7), 13112221)
print(s.countAndSay(8), 1113213211)
