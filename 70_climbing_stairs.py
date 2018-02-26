# coding: utf-8

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        total = self.helper1(n, total)
        return total

    def helper1(self, n, total):
        if n == 2:
            return 2
        elif n == 0:
            return 1
        elif n < 0:
            return 0
        total += self.helper(n - 1, 0)
        total += self.helper(n - 2, 0)
        return total

    def climbStairs2(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs3(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in xrange(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b

    def climbStairs4(self, n):
        self.result = {1: 1, 2: 2}
        return self.helper4(n)

    def helper4(self, n):
        if n not in self.result:
            self.result[n] = self.helper4(n - 1) + self.helper4(n - 2)
        return self.result[n]

    def climbStairs5(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        f = [None for i in range(n)]
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]
        return f[n - 1]

    def climbStairs(self, n):
        current, next = 1, 2
        # 确保n=1时结果正确
        for _ in range(1, n):
            current, next = next, current + next
        return current


s = Solution()
print(s.climbStairs(1), 1)
print(s.climbStairs(2), 2)
print(s.climbStairs(3), 3)
print(s.climbStairs(4), 5)
print(s.climbStairs(35), 14930352)

"""
3个台阶时，如果最后一步为1个台阶，那么方法数为: 2个台阶时的总数，如果最后一步为2个台阶，那么方法数为: 1个台阶时的总数，总方法数: 2个台阶的总数 + 1个台阶的总数
4个台阶时，...                                  3个台阶时的总数，...                                  2个台阶时的总数, ...       3个台阶的总数 + 2个台阶的总数
5个台阶时，...                                  4个台阶时的总数, ...                                  3个台阶时的总数, ...       4个台阶的总数 + 3个台阶的总数
所以，这就是一个斐波那契数列
"""
