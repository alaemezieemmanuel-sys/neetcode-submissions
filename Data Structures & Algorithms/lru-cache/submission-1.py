class Node():
    def __init__(self,key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #Defining the leftmose and rightmost Node
        self.left = Node(None,None)
        self.right = Node(None,None)
        self.left.next = self.right
        self.right.prev = self.left

        self.Cache  = {}
    #Make an node most recently used
    def insert(self,Node):
        prev, nxt = self.right.prev, self.right
        prev.next, Node.prev = Node, prev
        Node.next, nxt.prev = nxt,Node




    def remove(self,Node):
        prev, nxt = Node.prev, Node.next
        prev.next,nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.Cache:
            self.remove(self.Cache[key])
            self.insert(self.Cache[key])
            return self.Cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        NewNode = Node(key, value)
        if key in self.Cache:
            self.remove(self.Cache[key])
        self.insert(NewNode)
        self.Cache[key] = NewNode
        if len(self.Cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.Cache[lru.key]

