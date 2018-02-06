# coding: utf-8

# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        data = {}
        for s in strs:
            if not s:
                return ''
            tmp = data
            for x in s:
                if x not in tmp:
                    tmp[x] = {}
                tmp = tmp[x]
            # 统计词频，这道题用tmp[""] = ""标记字符串结束就可以，这里统计词频是为了模仿trie树
            tmp["freq"] = tmp.get("freq", 0) + 1
        answer = []
        while data:
            if len(data) != 1:
                break
            key, data = data.popitem()
            answer.append(key)
        return ''.join(answer)


if __name__ == "__main__":
    s = Solution()
    strss = [["a", "aa"], ["", "aa"], ["", ""], ["123456787", "12345", "123de"]]
    for strs in strss:
        print(strs)
        print(s.longestCommonPrefix(strs))
