class NodeBST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root == None:
            self.root = NodeBST(data)
        else:
            self._add(data, self.root)

    def _add(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = NodeBST(data)
            else:
                self._add(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = NodeBST(data)
            else:
                self._add(data, cur_node.right)
        else:
            print("Value is already present in tree.")

    def printTree(self):
        if self.root:
            self._printTree(self.root)

    def _printTree(self, cur_node):
        if cur_node:
            self._printTree(cur_node.left)
            print(cur_node.data)
            self._printTree(cur_node.right)

    def isBalanced(self):
        if self.root:
            res = self._isBalanced(self.root)
            if res == -1:
                return False
            else :
                return True
        else:
            return True

    def _isBalanced(self, cur_node):
        if cur_node:
            if not cur_node.left and not cur_node.right:
                return 0
            else:
                left = self._isBalanced(cur_node.left)
                right = self._isBalanced(cur_node.right)

                if left == -1 or right == -1:
                    return -1
                if abs(left - right) > 1:
                    return -1
                else:
                    return max(left, right) + 1
        else:
            return 0

    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return 0
    def _height(self, cur_node):
        if cur_node:
            if not cur_node.left and not cur_node.right:
                return 0
            else:
                left = self._height(cur_node.left)
                right = self._height(cur_node.right)
                return max(left, right) + 1
        else:
            return 0
# main.py
bst1 = BST()
bst2 = BST()
bst1.add(5)
bst1.add(3)
bst1.add(2)
bst1.add(4)
bst1.add(7)
bst1.add(6)
bst1.add(8)
bst1.add(10)
bst1.add(9)


print(bst1.isBalanced())

bst1.printTree()

print("height : ", bst1.height())

