# coding: utf-8

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 或许可以想想后缀表达式
        symbol = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "["}
        stack = []
        for x in s:
            if stack:
                # if x == stack[0]:
                    # stack.pop(0)
                # 先进后出
                if x == stack[-1]:
                    stack.pop()
                else:
                    stack.append(symbol[x])
            else:
                stack.append(symbol[x])
            # if stack and x == stack[0]:
                # stack.pop(0)
            # else:
                # stack.append(symbol[x])
            print(stack)
        if stack:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert(s.isValid("{}()[[]]") is True)
    assert(s.isValid("{([])}") is True)
    assert(s.isValid("{]}") is False)
    assert(s.isValid('([)]') is False)
