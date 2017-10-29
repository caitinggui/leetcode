#!/usr/bin/python
#coding:utf-8

# s can be:'', 'au', 'a', 'aab', 'abcabc'
class Solution(object):

    def solve(self):
        s = 'aab'
        first = 0
        result = ''
        all_different = True
        for i, x in enumerate(s):
            if x in s[first:i]:
                all_different = False
                print first, s[first:i], len(s[first:i])
                if len(result) < len(s[first:i]):
                    result = s[first:i]
                first = self.get_rank(x, s[first:i]) + first
        if len(result) < len(s[first:]):
            result = s[first:]
        if all_different:
            result = s
        return (result, len(result))

    # 判断重复的数字在第几位，0代表没有该重复数字，1代表第一位
    def get_rank(self, target, string_str):
        for i, x in enumerate(string_str[::-1]):
            if x == target:
                return len(string_str) - i
        return 0
    

    
    

problem = Solution()
result = problem.solve()
print result
  