# coding: utf-8

'''
 Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

Input: "USA"
Output: True

Example 2:

Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.capitalize() or word == word.upper() or word == word.lower():
            return True
        return False

    def detectCapitalUseNew(self, word):
        if len(word) == 1:
            return True
        # 首字母大写
        if word[0].isupper():
            if word[1].isupper():
                for w in word[2:]:
                    if w.islower():
                        return False
            else:
                for w in word[2:]:
                    if w.isupper():
                        return False
        else:
            for w in word[1:]:
                if w.isupper():
                    return False
        return True


s = Solution()
word = 'U'
assert s.detectCapitalUse(word) is True
word = 'USA'
assert s.detectCapitalUse(word) is True
word = 'UsA'
assert s.detectCapitalUse(word) is False
word = 'Usa'
assert s.detectCapitalUse(word) is True

word = 'USA'
assert s.detectCapitalUseNew(word) is True
word = 'UsA'
assert s.detectCapitalUseNew(word) is False
word = 'Usa'
assert s.detectCapitalUseNew(word) is True
