# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-13 12:19
 * Description   :
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.
'''


from collections import Counter


class Solution(object):
    def topKFrequent_error(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = {}
        w_ptr = 0
        min_word = words[0]
        while len(counter) < k and w_ptr < len(words):
            word = words[w_ptr]
            counter[word] = counter.get(word, 0) + 1
            if counter[word] <= counter.get(min_word, 0) and \
               word > min_word:
                min_word = word
            w_ptr += 1
        print "min_word", min_word
        result = set(counter.keys())
        while w_ptr < len(words):
            word = words[w_ptr]
            counter[word] = counter.get(word, 0) + 1
            if word not in result and counter[word] >= counter.get(min_word, 0) and \
               word < min_word:
                result.remove(min_word)
                min_word = word
                result.add(word)
            print result
            w_ptr += 1
        tmp = {}
        for word in result:
            tmp[word] = counter[word]
        return result

    def topKFrequent_error2(self, words, k):
        c = Counter(words)
        res = []
        for k, v in c.most_common(k):
            res.append(k)
        return res

    def topKFrequent(self, words, k):
        """时间为O(n + mlnm), m为n中的不重复元素个数，时间复杂度不符合O(nlnn)"""
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        ret = sorted(d, key=lambda word: (-d[word], word))
        return ret[:k]


s = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print(s.topKFrequent(words, k=4), ["the", "is", "sunny", "day"])

words = ["i", "love", "leetcode", "i", "you", "coding"]
print(s.topKFrequent(words, k=2), ["i", "coding"])

words = ["aaa", "aa", "a"]
print(s.topKFrequent(words, k=1), ["a"])
