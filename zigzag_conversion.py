#!usr/bin/python
# coding:utf-8

''' The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

("PAYPALISHIRING", 3) ('ab', 2), ('abc', 2), ('abcd', 2)
'''
from collections import defaultdict


class Solution(object):
    # @param {string} s
    # @param {integer} numrows
    # @return {string}

    def convert(self, s, numrows):

        if numrows == 1:
            return s
        lines = defaultdict(str)
        for i, c in enumerate(s):
            rem = i % (numrows + numrows - 2)
            if rem < numrows:
                lines[rem] += c
            else:
                lineno = numrows * 2 - 2 - rem
                lines[lineno] += c
            print str(lines)
        ss = "".join([lines[i] for i in range(numrows)])
        return ss


class Solution_ok(object):

    def convert(self, s, numrows):
        """
        :type s: str
        :type numrows: int
        :rtype: str
        """

        # The key is started with zero line
        if numrows <= 1:
            return s
        linelength = 2 * numrows - 2
        ss = [[] for i in range(numrows)]
        sm = []
        for i, x in enumerate(s):
            numlocation = i % linelength
            if numlocation >= numrows:
                numlocation = numrows - 1 - (numlocation - numrows + 1)
            ss[numlocation].append(x)
        for i in range(numrows):
            sm += (ss[i])
        return ''.join(sm)


solution = Solution()
assert 'PAHNAPLSIIGYIR' == solution.convert("PAYPALISHIRING", 3)
assert 'ab' == solution.convert("ab", 2)
assert 'acb' == solution.convert("abc", 2)
assert 'acbd' == solution.convert("abcd", 2)
