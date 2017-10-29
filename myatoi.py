#!usr/bin/python
# coding:utf-8

import re

# 进一步优化方法：去除对str裁剪，然后for x in str改为for x in str[nonumlength:]
class Solution(object):

    def my_atoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        atoidic = {
                   '0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
        }
        if str == '':
            return 0
        str = str.upper()
        base = 10
        nagativeflag = False
        len_str = len(str)
        blanklength = 0
        errorflag = 0
        while(str[blanklength] == ' '):
            blanklength += 1
            if blanklength == len_str:
                return 0
        str = str[blanklength:]
        if str[0] == '-':
            nagativeflag = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        if (not str) or (str[0] not in atoidic.keys()):
            return 0
        num = 0
            
        for x in str:
            if x == '.':
                is_behind_point = True
                continue
            if x not in atoidic.keys():
                break
            num = num * base + atoidic[x]
        if nagativeflag:
            num = 0 - num
        if num >= 2147483648:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num

    def my_atoi_any(self, str):
        """
        :type str: str
        :rtype: int
        """
        atoidic = {
                   '0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   'A': 10,
                   'B': 11,
                   'C': 12,
                   'D': 13,
                   'E': 14,
                   'F': 15,
        }
        if str == '':
            return 0
        str = str.upper()
        len_str = len(str)
        nonumlength = 0
        nagativeflag = 0
        while(str[nonumlength] not in atoidic.keys()):
            if str[nonumlength] == '-':
                nagativeflag += 1
            nonumlength += 1
            if nonumlength == len_str:
                return 0
        str = str[nonumlength:]
        if re.search('[A|B|C|D|E,F]', str):
            base = 16
        else:
            base = 10
        nagativeflag = nagativeflag % 2
        is_behind_point = False
        nagative_length = 0
        str_num_front = 0
        str_num_behind = 0
            
        for x in str:
            if x == '.':
                is_behind_point = True
                continue
            if x not in atoidic.keys():
                break
            if not is_behind_point:
                str_num_front = str_num_front * base + atoidic[x]
            else:
                str_num_behind = str_num_behind * base + atoidic[x]
                nagative_length += 1
        if nagative_length:
            num = str_num_front + str_num_behind * 1.0 / (base**nagative_length)
        else:
            num = str_num_front
        if nagativeflag:
            num = 0 - num
        return num

        
solution = Solution()
assert solution.my_atoi('0') == 0
assert solution.my_atoi('') == 0
assert solution.my_atoi('+34') == 34
assert solution.my_atoi('+-4') == 0
assert solution.my_atoi('     -4') == -4
assert solution.my_atoi('     -4  3') == -4
assert solution.my_atoi('+') == 0
assert solution.my_atoi("  -0012a42") == -12
assert solution.my_atoi("  -0012M42") == -12
assert solution.my_atoi("2147483648") == 2147483647
assert solution.my_atoi(" b11228552307") == 0

assert solution.my_atoi_any('2.0') == 2.0
assert solution.my_atoi_any('0.44') == 0.44
assert solution.my_atoi_any('0') == 0
assert solution.my_atoi_any('') == 0
assert solution.my_atoi_any('+34') == 34
assert solution.my_atoi_any('+-4') == -4
assert solution.my_atoi_any('     -4') == -4
assert solution.my_atoi_any('+') == 0
assert solution.my_atoi_any("  -0012a42") == -76354
assert solution.my_atoi_any("  -0012M42") == -12
assert solution.my_atoi_any("2147483648") == 2147483648
assert solution.my_atoi_any(" b11228552307") == 194691544195847
assert solution.my_atoi_any(" m11228552307") == 11228552307
assert solution.my_atoi_any('2.44') == 2.44
assert solution.my_atoi_any('-2.44') == -2.44


def break_str(max_len=90):
    s = 'ehisaoj dfuek dfaei 3iadfkj fiasf \n{} \t\t'
    l = len(s)
    i, x = 0, max_len
    res = []
    while i < l:
       res.append(s[i:i + max_len])
       i += x
       print str(res)
    return '\n{}'.format('\t' * 5).join(res)
    
break_str()