# coding: utf-8

'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import Counter


class Solution(object):
    def findAnagrams_slowest(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        result = []
        pn = {}
        for x in p:
            pn[x] = pn.get(x, 0) + 1
        for i in range(len(s) - len(p) + 1):
            tn = {}
            j = i
            while j < len(s) and j - i < len(p):
                tn[s[j]] = tn.get(s[j], 0) + 1
                j += 1
            if tn == pn:
                result.append(i)
        return result

    def findAnagrams_slow(self, s, p):
        if not s or not p:
            return []
        res = []
        pCounter = Counter(p)
        # 提前将len(p)-1个元素统计好
        sCounter = Counter(s[:len(p) - 1])
        # i初始时，sCounter元素个数刚好等于pCounter
        # i - len(p) + 1意味这从0开始
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            # This step is O(1), since there are at most 26 English letters
            if sCounter == pCounter:
                res.append(i - len(p) + 1)   # append the starting index
            # decrease the count of oldest char in the window
            sCounter[s[i - len(p) + 1]] -= 1
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]   # remove the count if it is 0
        return res

    def findAnagrams(self, s, p):
        # two pointer template:
        # https://discuss.leetcode.com/topic/68976/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem

        p_map = dict()
        for x in p:
            p_map[x] = p_map.get(x, 0) + 1

        count = len(p_map)
        left, right = 0, 0
        ans = []

        while right < len(s):
            print(left, right, count, p_map)
            c = s[right]
            if c in p_map:
                p_map[c] -= 1
                if p_map[c] == 0:
                    count -= 1

            right += 1

            while count == 0:
                print(left, right, count, p_map, '--')
                c = s[left]
                if c in p_map:
                    p_map[c] += 1
                    if p_map[c] > 0:
                        count += 1
                if right - left == len(p):     # only difference with LC76 min widow substring
                    ans.append(left)
                left += 1

        return ans


s = Solution()
print(s.findAnagrams('abab', 'ab'), [0, 1, 2])
print
print(s.findAnagrams("cbaebabacd", 'abc'), [0, 6])
print
print(s.findAnagrams("", 'abc'), [])
print
print(s.findAnagrams("ab", ''), [])
print
print(s.findAnagrams("ab", 'ab'), [0])
print
print(s.findAnagrams("ab", 'a'), [0])
print
print(s.findAnagrams("a", 'ab'), [])
print
print(s.findAnagrams("bf", 'ae'), [])
print
