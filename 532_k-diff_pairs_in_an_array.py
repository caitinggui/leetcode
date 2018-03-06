# coding: utf-8

'''
 Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
'''


class Solution(object):
    def findPairs_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        # 用small和big好区分组合是否已经存在
        tmp_small = set()
        tmp_big = set()
        res = set()
        for num in nums:
            if num in tmp_small:
                res.add((num, num + k))
            if num in tmp_big:  # 不能用elif，因为2, 4, 6, 当k=2，num=4时应该有两个
                res.add((num - k, num))
            tmp_small.add(num - k)
            tmp_big.add(num + k)
        # print(res)
        return len(res)

    def findPairs(self, nums, k):
        if k < 0:
            return 0
        map = {}
        res = 0
        for num in nums:
            if num not in map:
                if num+k in map:
                    res += 1
                if num-k in map:
                    res += 1
                map[num] = 1
            elif k == 0 and map[num] == 1:
                res += 1
                map[num] += 1
        return res


s = Solution()
print(s.findPairs([3, 1, 4, 1, 5], k=2), 2)
print
print(s.findPairs([1, 2, 3, 4, 5], k=1), 4)
print
print(s.findPairs([1, 3, 1, 5, 4], k=0), 1)
print
print(s.findPairs([1, 3, 1, 3, 4], k=0), 2)
print
print(s.findPairs([6, 3, 5, 7, 2, 3, 3, 8, 2, 4], k=2), 5)
print
