#!usr/bin/python
#coding:utf-8

'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = previous = None
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = s / 10, s % 10
            node = ListNode(val)
            if previous:
                previous.next = node
            else: 
                head = node
            previous = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head