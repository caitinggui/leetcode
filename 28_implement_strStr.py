# coding: utf-8

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class Solution(object):

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr_slow(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            if needle:
                return -1
            else:
                return 0
        return self.search(haystack, needle)

    def partial(self, needle):
        ret = [0]
        for i in range(1, len(needle)):
            j = ret[i - 1]
            while j > 0 and needle[j] != needle[i]:
                j = ret[j - 1]
            ret.append(j + 1 if needle[j] == needle[i] else j)
        return ret

    def search(self, haystack, needle):
        partial = self.partial(needle)
        print(partial)
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j:  # 判断是不是needle的首字符
                print("--", j, partial[j - 1])
                # (i - j) + (j - partial[j - 1])
                # i - j 表示开始匹配的那个位置
                # j - partial[j - 1] 是将起始点向后移动的位置, 用j - 1是因为j - 1是最后一个匹配到的字符
                i = i - partial[j - 1]
                j = 0
            else:
                i += 1  # 首字符不匹配，haystack的节点忘后移动1位
            print(i, j)
            if j == len(needle):
                return i - len(needle)
        return -1

    def strStr_error(self, haystack, needle):
        start = needle[0]
        i = j = k = 0
        import ipdb
        ipdb.set_trace()
        while i < len(haystack):
            if haystack[i] == start:
                first = True
                i += 1
                for x in needle[1:]:
                    if first and haystack[i] == start:
                        k = i
                        first = False
                    if haystack[i] == x:
                        i += 1
                    else:
                        if k:
                            i = k
                        i = k
                        break
                else:
                    return i - len(needle) + 1
            i += 1
            first = False


if __name__ == "__main__":
    s = Solution()
    assert(s.strStr("hello", 'll') == 2)
    assert(s.strStr("aaaaa", "bba") == -1)
    assert(s.strStr("", "") == 0)
    assert(s.strStr("", "a") == -1)
    assert(s.strStr("a", "") == 0)
    assert(s.strStr("mississippi", "issip") == 4)
