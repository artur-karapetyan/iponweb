class BinarySearchTree:
    class Node:

        def __init__(self, key, left=None, right=None):
            self.__key = key
            self.__left = left
            self.__right = right

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

    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def insert(self, key):
        n = BinarySearchTree.Node(key)
        if self.root is None:
            self.root = n
            return
        prev = None
        temp = self.root
        while temp is not None:
            if temp.key > key:
                prev = temp
                temp = temp.left
            elif temp.key <= key:
                prev = temp
                temp = temp.right
        if prev.key > key:
            prev.left = n
        else:
            prev.right = n

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    def tree_max(self, root):
        walk = root
        while walk.right is not None:
            walk = walk.right

        return walk

    def delete(self, key):
        def delete_node(root, key):
            if root is None:
                return None
            if root.key < key:
                root.right = delete_node(root.right, key)
            elif root.key > key:
                root.left = delete_node(root.left, key)
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                pred = self.tree_max(root.left)
                root.key = pred.key
                root.left = delete_node(root.left, pred.key)
            return root

        self.root = delete_node(self.root, key)


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print(bst.tree_max(bst.root).key == 80)
print(bst.search(bst.root, 70).key)
bst.delete(70)
print(bst.search(bst.root, 70))
