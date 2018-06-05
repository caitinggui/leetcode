# coding:utf-8


class Node(object):

    def __init__(self, data, position=None):
        self.data = data
        self.next = position


class LinkList(object):

    def __init__(self, data=None):
        if data:
            if type(data) in [tuple, list]:
                self.head = Node(data[0])
                if len(data) > 0:
                    p = self.head
                    for i in data[1:]:
                        p.next = Node(i)
                        p = p.next
            else:
                self.head = Node(data)
        else:
            self.head = None

    def append(self, data):
        p = self.go_index(self.get_length() - 1)
        p.next = Node(data)

    def clear(self):
        self.head = None

    def delete(self, index=None):
        if index is None:
            index = self.get_length() - 1
        elif index >= self.get_length():
            return 'The index is larger than LinkList length'

        if index == 0:
            if self.get_length() == 1:
                self.head = None
            else:
                p = self.go_index(index + 1)
                self.head = p
        elif index == self.get_length() - 1:
            p = self.go_index(index - 1)
            p.next = None
        else:
            p = self.go_index(index - 1)
            p.next = self.go_index(index + 1)

    def del_node(self, node):
        """
        这里只是改变的传进来的变量的值，并没有删除节点, 归根结底node不是可变变量，函数内赋值node只会使函数内的node变为新
        变量，但赋值node.data等内部数据，不会改变node的引用(id(node)不变)，也就是说修改了整个LinkList
        node = node.next
        """
        node.data = node.next.data
        node.next = node.next.next

    def get_length(self):
        p = self.head
        length = 0
        while p:
            p = p.next
            length += 1
        return length

    def go_index(self, index):
        if self.is_empty():
            return 'LinkList is empty'
        if index < 0 or type(index) != int:
            return 'The index should be natural number'
        if index >= self.get_length():
            return 'The index is larger than LinkList length'
        p = self.head
        while index > 0:
            p = p.next
            index -= 1
        return p

    def insert(self, index, data):
        if index >= self.get_length():
            return 'The index is larger than LinkList length'
        if index == 0:
            p = self.head
            self.head.next = p
            self.head.data = data
        else:
            pass

    def is_empty(self):
        return True if not self.head else False

    def reverse(self):
        inext = self.head
        old = None
        while inext:
            now = inext
            inext = now.next
            now.next = old
            old = now
        self.head = now
        return self.head
        ''' to return Node
        inext = self.head
        old = None
        while inext:
            now = inext
            inext = now.next
            now.next = old
            old = now
        return old
        '''

    def show(self):
        if self.is_empty():
            return 'LinkList is empty'
        p = self.head
        while p:
            print(str(p.data))
            p = p.next


linklist = LinkList([1, 2, 3, 4, 5, 6, 7])
print("---show---")
linklist.show()
print(linklist.reverse().data)
print("---reverse---")
linklist.show()
print("---delete index 2---")
linklist.delete(2)
linklist.show()
