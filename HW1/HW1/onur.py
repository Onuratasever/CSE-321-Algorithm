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

    def _merge(self, cur_node):
        if cur_node:
            self._merge(cur_node.left)
            self.add(cur_node.data)
            self._merge(cur_node.right)

    # the following function will merge two BSTs using preorder traversal
    def merge(self, bst):
        if self.root:
            self._merge(bst.root)

    def findKthElement(self, kTH):
        curNode = self.root
        k = [kTH]
        self._findKthElement(curNode, k)

    def _findKthElement(self, cur_node, k):

        if cur_node:
            self._findKthElement(cur_node.left, k)
            k[0] = k[0] - 1
            if k[0]==0:
                print("Found ", cur_node.data)
            else:
                self._findKthElement(cur_node.right, k)




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
bst2.add(1)
bst2.add(2)
bst2.add(3)
bst2.add(4)
bst2.add(5)


bst1.merge(bst2)

print("Kth element is:")
bst1.findKthElement(6)