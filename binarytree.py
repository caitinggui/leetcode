# coding:utf-8

# 请参考94_binary*.py and 144_binary*.py and 145_binary*.py

class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = TreeNode()
    def creat(self, datalist):
        for data in datalist:
            self.insert(data)
        return self.root
    def insert(self, data, node=None):
        if node is None:
            node = self.root
        if self.root.data is None:
            self.root = TreeNode(data)
        elif data < node.data:
            if node.left is not None:
                self.insert(data, node.left)
            else:
                node.left = TreeNode(data)
        else:
            if node.right is not None:
                self.insert(data, node.right)
            else:
                node.right = TreeNode(data)
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


def createTree(datas):
    """按照Leecode的格式创建树
    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
    总的思想是，把已经初始化的节点加入nodes，然后一个个弹出，绑定子节点，
    此时，子节点也应继续加入nodes中. try是为了防止超出datas长度
    """
    root = TreeNode(datas[0])
    nodes = [root]
    datas_index = 1
    while nodes:
        node = nodes.pop(0)
        if not node:
            # 一个node对应两个子节点，如果node为空，说明接下来的子节点也可以舍弃
            datas_index += 2
            continue
        try:
            if datas[datas_index]:
                node.left = TreeNode(datas[datas_index])
            nodes.append(node.left)
            datas_index += 1
        except IndexError:
            pass
        try:
            if datas[datas_index]:
                node.right = TreeNode(datas[datas_index])
            nodes.append(node.right)
            datas_index += 1
        except IndexError:
            pass
    return root


if __name__ == "__main__":
    bt = BinaryTree()
    bt.creat([1,5,6,3,2,8,19,45,32])
    bt.bfs(bt.root)
    bt.show()
