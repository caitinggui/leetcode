# coding:utf-8

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = Node()
    def creat(self, datalist):
        for data in datalist:
            self.insert(data)
        return self.root
    def insert(self, data, node=None):
        if node is None:
            node = self.root
        if self.root.data is None:
            self.root = Node(data)
        elif data < node.data:
            if node.left is not None:
                self.insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self.insert(data, node.right)
            else:
                node.right = Node(data)
        return self.root

    def preorder(self, node):
        if node is None:
            return 
        else:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)

    def preorder_stack(self):
        

    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)

    def postorder(self, node):
        if node in None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data

    def show(self):
        self.preorder(self.root)