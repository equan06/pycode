class DLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.nxt = None
        

class DLL:
    def __init__(self):
        """
        Initialize a doubly linked list, with a head and tail pointer.
        """
        self.head = None
        self.tail = None
        
    def append(self, node):
        """
        Add a DLLNode to the DLL's tail.
        """
        if self.head is None:
            self.head = node
        elif self.tail is not None:
            self.tail.nxt = node
            node.prev = self.tail
        self.tail = node
    
    def remove(self, node):
        """
        Remove a given node reference from the DLL.
        """
        if node.prev is not None:
            node.prev.nxt = node.nxt
        
        if node.nxt is not None:
            node.nxt.prev = node.prev

        if node == self.head: 
            self.head = node.nxt
        if node == self.tail:
            self.tail = node.prev

    def __str__(self):
        curr = self.head
        lst = []
        while curr is not None:
            lst.append(curr.val)
            curr = curr.nxt
        return str(lst)       
    
