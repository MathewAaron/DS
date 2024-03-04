

class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 
        self.level = None 

class BSTLevels():

    def __init__(self):
        self.root = None 

    def initialize_node(self,data):
        self.root = Node(data)

    def add_element(self,root,data):

        if self.root is None :
            self.initialize_node(data)

        if data < root.data :
            root.left = self.add_element(root.left,data)
        else :
            root.right = self.add_element(root.right,data)

        return root 
    
    def print_topview(self,root):

        q = []
        d = dict()

        root.level = 0
        q.append(root)
        
        while q :

            root = q.pop(0)

            if root.level not in d :
                d[root.level] = root.data
            if root.left :
                q.append(root)
                root.left.level = root.level - 1
            if root.right :
                q.append(root)
                root.right.level = root.level + 1
            
        print(*d.values())
