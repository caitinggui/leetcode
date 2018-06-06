# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-06-05 17:40
 * Description   :
 You are given a license key represented as a string S which consists only alphanumeric character and dashes.
 The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters,
except for the first group which could be shorter than K, but still must contain at least one character.Furthermore,
there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it
could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
'''
from __future__ import print_function, unicode_literals, division, absolute_import


class Solution(object):
    def licenseKeyFormatting_slow(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        for s in S[::-1]:
            if s != "-":
                res.append(s.upper())

        result = []
        for index in range(0, len(res), K):
            result.append("".join(res[index: index + K]))
        return "-".join(result)[::-1]

    def licenseKeyFormatting(self, S, K):
        S = S.replace('-', '')[::-1].upper()
        return '-'.join([S[i:i + K] for i in range(0, len(S), K)])[::-1]


s = Solution()
S = "5F3Z-2e-9-w"
print(s.licenseKeyFormatting(S, 4), "5F3Z-2E9W")
S = "2-5g-3-J"
print(s.licenseKeyFormatting(S, 2), "2-5G-3J")
