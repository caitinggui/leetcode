#coding:utf-8

'''
A tree.
'''


class Tree(object):

    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data