#!usr/bin/python
# coding:utf-8


class Solution(object):

    def insertsort_second(self, numlist):
        exchangeflag = False
        numlen = len(numlist)
        for i in range(numlen):
            for j in range(numlen - i - 1):
                if numlist[j] < numlist[j + 1]:
                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
                    exchangeflag = True
                print i, j, str(numlist)
            if exchangeflag:
                exchangeflag = False
            else:
                return numlist
        return numlist
        
    def insertsort(self, numlist):
        exchangeflag = False
        numlen = len(numlist)
        lastexchange = numlen
        i = 0
        while i < numlen:
            lastexchange = 0
            for j in range(numlen - i - 1):
                if numlist[j] < numlist[j + 1]:
                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
                    lastexchange = j + 2
                print i, j, lastexchange, str(numlist)
            i += 1
            numlen = lastexchange
        return numlist
        
        
solution = Solution()
assert(solution.insertsort([1,2,5,7,3,4]) == [7,5,4,3,2,1])
assert(solution.insertsort(['a',2,'c',7,'b',4]) == ['c', 'b', 'a', 7, 4, 2])
assert(solution.insertsort([1,2,3,4,5,6]) == [6,5,4,3,2,1])
assert(solution.insertsort([6,5,4,3,2,1]) == [6,5,4,3,2,1])

