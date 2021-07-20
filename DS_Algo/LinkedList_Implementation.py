# create node
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# create Linklist
class linkedList:
    def __init__(self):
        self.head = None
    
    # traversal
    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    # adding element at the beginning
    def add_beg(self,data):
        new_node1 = Node(data)
        new_node1.ref = self.head
        self.head = new_node1

    # adding element at the end
    def add_end(self,data):
        new_node2 = Node(data)
        if self.head is None:
            self.head = new_node2
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node2

    # adding the element after the given node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in linkedList")
        else:
            new_node3 = Node(data)
            new_node3.ref = n.ref
            n.ref = new_node3

    # adding the element before the given node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # deleting element at the beginning
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we cant delete!")
        else:
            self.head = self.head.ref

    # deleting element at the end
    def delete_end(self):
        if self.head is None:
            print("LL is empty so we cant delete!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # delete any Node by value 
    def delete_by_value(self,x):
        if self.head is None:
            print("cant delete LL is empty!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present!")
        else:
            n.ref = n.ref.ref

    # Revesre the linked list...
    def reverseLL(self):
        prevptr = None
        currptr = self.head
        while currptr != None:
            nextptr = currptr.ref
            currptr.ref = prevptr
            prevptr = currptr
            currptr = nextptr
        self.head = prevptr

    # Revesre linked list by k.....
    def reverseByk(self,head,k):
        prevptr = None
        currptr = self.head
        count = 0
        while currptr != None and count < k:
            nextptr = currptr.ref
            currptr.ref = prevptr
            prevptr = currptr
            currptr = nextptr
            count +=1
        
        if nextptr != None:
            self.head.ref = self.reverseByk(nextptr,k)
        return prevptr



LL1 = linkedList()
LL1.add_beg(10)
LL1.add_beg(20)
LL1.add_beg(30)
LL1.add_beg(40)
LL1.print_list() 
# LL1.reverseLL()
# LL1.add_end(100)
# LL1.add_after(30,20)
LL1.reverseByk(LL1.head,2)
LL1.print_list()           