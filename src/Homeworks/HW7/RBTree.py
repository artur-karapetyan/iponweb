class RedBlackTree:
    class Node:
        def __init__(self, key, color='red'):
            self.__key = key
            self.__left = None
            self.__right = None
            self.__color = color

        @property
        def key(self):
            return self.__key

        @key.setter
        def key(self, key):
            self.__key = key

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, left):
            self.__left = left

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, right):
            self.__right = right

        @property
        def color(self):
            return self.__color

        @color.setter
        def color(self, color):
            self.__color = color

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def insert(self, key):
        self.root = self.__rebalance_insert(self.root, key)
        self.root.color = 'black'

    def __rebalance_insert(self, node, key):
        if not node:
            return RedBlackTree.Node(key)
        if key < node.key:
            node.left = self.__rebalance_insert(node.left, key)
        else:
            node.right = self.__rebalance_insert(node.right, key)
        if node.right and node.right.color == 'red':
            node = self.__rebalance_left(node)
        if node.left and node.left.color == 'red' and node.left.left and node.left.left.color == 'red':
            node = self.__rebalance_right(node)
        if node.left and node.right and node.left.color == 'red' and node.right.color == 'red':
            node = self.__change_color(node)
        return node

    def search(self, key):
        return self.__search_node(self.root, key)

    def __search_node(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.__search_node(node.left, key)
        else:
            return self.__search_node(node.right, key)

    def delete(self, key):
        self.root = self.__rebalance_delete(self.root, key)
        if self.root:
            self.root.color = 'black'

    def __rebalance_delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self.__rebalance_delete(node.left, key)
        elif key > node.key:
            node.right = self.__rebalance_delete(node.right, key)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            temp = node
            node = self.__tree_min(temp.right)
            node.right = self.__delete_min(temp.right)
            node.left = temp.left
        if node.right and node.right.color == 'red':
            node = self.__rebalance_left(node)
        if node.left and node.left.color == 'red' and node.left.left and node.left.left.color == 'red':
            node = self.__rebalance_right(node)
        if node.left and node.right and node.left.color == 'red' and node.right.color == 'red':
            node = self.__change_color(node)
            return node

    def __rebalance_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 'red'
        return x

    def __rebalance_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 'red'
        return x

    def __change_color(self, node):
        node.left.color = 'black'
        node.right.color = 'black'
        node.color = 'red'
        return node

    def __tree_min(self, node):
        while node.left:
            node = node.left
        return node

    def __delete_min(self, node):
        if not node.left:
            return node.right
        node.left = self.__delete_min(node.left)
        if node.right and node.right.color == 'red':
            node = self.__rebalance_left(node)
        if node.left and node.left.color == 'red' and node.left.left and node.left.left.color == 'red':
            node = self.__rebalance_right(node)
        if node.left and node.right and node.left.color == 'red' and node.right.color == 'red':
            node = self.__change_color(node)
        return node


# Testing functions
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(40)
rbt.insert(4)
rbt.insert(14)
print(rbt.search(20).color)
print(rbt.search(10).color)
print(rbt.search(30).color)
rbt.delete(20)
print(rbt.search(20))
