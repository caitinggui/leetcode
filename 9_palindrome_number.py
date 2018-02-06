# Determine whether an integer is a palindrome. Do this without extra space.

# click to show spoilers.
# Some hints:

    # Could negative integers be palindromes? (ie, -1)

    # If you are thinking of converting the integer to string, note the restriction of using extra space.

    # You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

    # There is a more generic way of solving this problem.


class Solution(object):
    def isPalindrome_slow(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp = []
        # 0也是回文
        if x < 0:
            return False
        while x:
            tmp.append(x % 10)
            x = x / 10
        return tmp == tmp[::-1]

    def isPalindrome(self, x):
        x_str = str(x)
        return x_str == x_str[::-1]
