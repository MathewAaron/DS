class Node:

    def __init__(self,key,data):
        self.key = key
        self.data = data 
        self.next = None
        self.prev = None 

class LRUCacheDLL :

    def __init__(self,capacity) -> None:
        self.cap = capacity
        self.lru_dict = dict()
        self.head = Node('#',-1)
        self.tail = Node('-',-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def display_dll(self):
        current = self.head
        if current == None :
            print("List is empty")
            return 

        while current :
            print(f"{current.data}")
            current = current.next

    def add_element(self,node):
        # Recently used elements (on addition) will be appended in the begining of DLL
        # head <-> node2 <-> node1  <-> tail , where node2 is least recently used
        prev_first = self.head.next
        prev_first.prev = node
        node.next = prev_first
        node.prev = self.head
        self.head.next = node

    def delete_element(self,node):
        # deletes the node 
        # head <-> --n-o-d-e-1-- <-> node2 <-> node3 <-> tail
        prev_node , next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self,key):

        if key not in self.lru_dict:
            return -1
        node = self.lru_dict[key]
        self.delete_element(node)
        self.add_element(node)
        return node.data

    def put(self,key,value):

        if key in self.lru_dict:
            old_node = self.lru_dict[key]
            self.delete_element(old_node)
            del self.lru_dict[key]
        
        node = Node(key,value)
        self.add_element(node)
        self.lru_dict[key] = node 
        if len(self.lru_dict) > self.cap :
            old_node = self.tail.prev
            self.delete_element(old_node)
            del self.lru_dict[old_node.key]

lru_obj = LRUCacheDLL(3)

temp_node1 = Node(2,3)
temp_node2 = Node(3,10)
temp3 = Node(4,15)
temp4 = Node(5,20)

lru_obj.put(2,3)
lru_obj.put(3,10)
lru_obj.put(4,15)
lru_obj.display_dll()
lru_obj.put(5,20)
lru_obj.display_dll()
print(f"getting 3 : {lru_obj.get(3)}")
print(f"getting 1 : {lru_obj.get(1)}")
lru_obj.display_dll()

