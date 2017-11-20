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
        pass

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

    def bfs(self, node):
        tree_stack = []
        tree_stack.append(node)
        while len(tree_stack) > 0:
            node_next = tree_stack.pop(0)
            print node_next.data
            if node_next.left:
                tree_stack.append(node_next.left)
            if node_next.right:
                tree_stack.append(node_next.right)


if __name__ == "__main__":
    bt = BinaryTree()
    bt.creat([1,5,6,3,2,8,19,45,32])
    bt.bfs(bt.root)
    bt.show()
