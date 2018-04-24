#!usr/bin/python
# coding:utf-8


class Solution(object):

    def insertsort(self, s):
        ss = {}
        ss[0] = s[0]
        for i in range(1, len(s)):
            for j in range(len(ss)):
                if s[i] < ss[j]:
                    # if j == len(ss) - 1:
                        # ss[j + 1] = ss[j]
                        # ss[j] = s[i]
                        # break
                    # else:
                    for k in range(len(ss) - 1, j - 1, -1):
                        ss[k + 1] = ss[k]
                    break
                else:
                    j += 1
            ss[j] = s[i]
        return ss.values()
        
solution = Solution()
assert(solution.insertsort([1,2,5,7,3,4]) == [1,2,3,4,5,7])
assert(solution.insertsort(['a',2,'c',7,'b',4]) == [2, 4, 7, 'a', 'b', 'c'])