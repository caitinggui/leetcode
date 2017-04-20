#!usr/bin/python
# coding:utf-8


class Solution(object):
        
    def onesort(self, sortlist, left, right):
        i = left
        j = right
        key = sortlist[i]
        while i < j:
            while i < j:
                if sortlist[j] > key:
                    sortlist[i] = sortlist[j]
                    i += 1
                    break
                j -= 1
            while i < j:
                if sortlist[i] <= key:
                    sortlist[j] = sortlist[i]
                    j -= 1
                    break
                i += 1
        sortlist[i] = key
        print 'i', i, j, str(sortlist)
        return i
        
    def realquicksort(self, sortlist, left, right):
        if left < right:
            keylocation = self.onesort(sortlist, left, right)
            self.realquicksort(sortlist, left, keylocation - 1)
            self.realquicksort(sortlist, keylocation + 1, right)
        return sortlist
        
    def quicksort(self, tosortlist):
        left = 0
        right = len(tosortlist) - 1
        sortlist = []
        for i in tosortlist:
            sortlist.append(i)
        return self.realquicksort(sortlist, left, right)
        
        
solution = Solution()
a=[6,7,5,8,4,9]
solution.quicksort(a)
print '---', a
assert(solution.quicksort([6,7,5,8,4,9]) == [9, 8, 7, 6, 5, 4])
assert(solution.quicksort(['a',2,'c',7,'b',4]) == ['c', 'b', 'a', 7, 4, 2])
assert(solution.quicksort([1,2,3,4,5,6]) == [6,5,4,3,2,1])
assert(solution.quicksort([6,5,4,3,2,1]) == [6,5,4,3,2,1])