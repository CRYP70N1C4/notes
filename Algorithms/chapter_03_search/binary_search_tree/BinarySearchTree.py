class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        pass


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def __compare(self, node, value):
        if node.value == value:
            return 0
        elif node.value > value:
            return 1;
        else:
            return -1;

    def insert(self, value):
        if self.isEmpty():
            return
        else:
            self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node == None:
            return TreeNode(value)
        if self.__compare(node, value) < 0:
            node.left = self.insert(node.left, value)
        elif self.__compare(node, value) > 0:
            node.right = self.insert(node.right, value)

    def find(self, value):
        if self.isEmpty():
            return None
        else:
            return self.__find(self.root, value)

    def __find(self, node, value):
        if self.__compare(node, value) < 0:
            return self.__find(node.left, value)
        elif self.__compare(node, value) > 0:
            return self.__find(node.right, value)
        else:
            return node;

    def findMax(self, value):
        return self.__find(self.root, value)

    def __findMax(self, node, value):
        while node.right != None:
            node = self.rigth
        return node.value

    def findMin(self, value):
        return self.__find(self.root, value)

    def __findMin(self, node, value):
        while node.left != None:
            node = self.left
        return node.value

    def __delete(self, node, value):
        if node == None:
            return node

        if self.__compare(node, value) < 0:
            node.left = self.__delete(node.left, value)
        elif self.__compare(node, value) > 0:
            node.right = self.__delete(node.right, value)
        else:
            if node.left != None and node.right != None:
                min = self.findMin(self, node.rigth)
                node.value = min
                node.rigth = self.__delete(self, node.right, min)
            elif node.left != None:
                node = node.left;
            else:
                node = node.rigth;

    def getTreeHight(self):
        return

    def __getTreeHight(self, node):
        i = self.__getTreeHight(node.left) + 1
        j = self.__getTreeHight(node.right) + 1
        return i if i > j else j;
