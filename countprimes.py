# coding:utf-8

'''
Count the number of prime numbers less than a nonnegative number, n.
'''

class Solution(object):
    def count_primes(self, n):

        if n <=2:
            return 0
        prime = [True] * n
        pn = []
        prime[:2] = [False, False]
        for base in xrange(2, int((n-1) ** 0.5) + 1):
            if prime[base]:
                prime[base ** 2:n:base] = [False] * len(prime[base ** 2:n:base])
        for i, x  in enumerate(prime):
            if x:
                pn.append(i)
        return pn
        return sum(prime)
                
                
                
                
                
solution = Solution()
print solution.count_primes(10)
print solution.count_primes(1000000)