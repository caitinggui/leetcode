# coding: utf-8

'''
kmp算法的实现
参考:http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
'''


class KMP(object):

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


if __name__ == "__main__":
    kmp = KMP()
    print(kmp.search('BBC_ABCDAB_ABCDABCDABDE', 'ABCDABD'))
    print(kmp.search("mississippi", "issip"))
