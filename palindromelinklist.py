#!usr/bin/python
# coding:utf-8

'''
Given a singly linked list, determine if it is a palindrome.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        fast=slow=cur=head
        # find middle of linklist
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # avoid modify linklist
        data = []
        while slow:
            data.append(slow.val)
            slow = slow.next
        while data:
            if data.pop() != cur.val:
                return False
            cur = cur.next
        return True