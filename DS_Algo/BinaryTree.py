class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    # Insert a key in BST
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    # Search a key in BST
    def search(self,data):
        if self.key == data:
            print("Node is present !")
        elif self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present !!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present !!")

    # Traversal operations......

    # 1. Preorder ---->> root->left->right
    def preOrder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    # 2. Inorder ---->> left->root->right
    # in this method we get sorted tree
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inOrder()

    # 3. Postorder ---->> left->right->root
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key,end=" ")

    # Delete node 
    def delete(self,data):
        if self.key is None:
            print("Tree is empty! ")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present in the tree. ")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree. ")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self

    # Find minimum key
    def min_node(self):
        cuurent = self
        while cuurent.lchild:
            cuurent = cuurent.lchild
        print(f"Node with smallest key {cuurent.key}")

    # Find maximum key
    def max_node(self):
        cuurent = self
        while cuurent.rchild:
            cuurent = cuurent.rchild
        print(f"Node with smallest key {cuurent.key}")




root = BST(10)
lst1 = [20,4,30,4,1,5,6]
for i in lst1:
    root.insert(i)
# root.search(10)
root.preOrder()
print()
# root.inOrder()
# print()
# root.postOrder()
# root.delete(20)
# print()
# root.preOrder()
# root.min_node()
# root.max_node()
# print(root.key)
# print(root.lchild)
# print(root.rchild)
