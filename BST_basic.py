class Node :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

class Tree:

    def create_node(self,data):

        return Node(data)
    
    def insert_element_iterative(self,root,data):
        """
            Insert BST element using iteration
        """
        if not root:
            return self.create_node(root)
        
        while True :

            if data < root.left :
                if root.left is None :
                    root.left = Node(data)
                    break
                else:
                    root = root.left
            else :
                if root.right is None :
                    root.right = Node(data)
                    break
                else :
                    root = root.right

    def height_of_tree(self,root):
        """
            using recursion

            checks for root to be None 
                 returns -1 if it is
            otherwise 
            returns max( height(root.left), height(root.right)) + 1
        """
        if root is None :
            return -1
        
        return max(self.height_of_tree(root.left),self.height_of_tree(root.right)) + 1

    def insert_element_rec(self,root,data):
        """
            Insert BST element using recursion
        """
        # first element
        if not root:
            return self.create_node(data)

        if data < root.data :
            root.left = self.insert_element_rec(root.left,data)

        else: 
            root.right = self.insert_element_rec(root.right,data)

        return root
    
    def traverse_inorder(self,root):
        """
        [ LEFT , ROOT , RIGHT ]

        ## This also prints elements in a sorted manner
        """
        if root :
            self.traverse_inorder(root.left)

            print(root.data)

            self.traverse_inorder(root.right)

    def traverse_preorder(self,root):
        """
        [ ROOT , LEFT , RIGHT]
        """
        if root :

            print(root.data)

            self.traverse_preorder(root.left)

            self.traverse_preorder(root.right)


    def traverse_postorder(self,root):
        """
        [ LEFT , RIGHT , ROOT ]
        """
        if root :

            self.traverse_postorder(root.left)

            self.traverse_postorder(root.right)

            print(root.data)

    def traverse_levelorder(self,root):
        """
        QUEUE : 
            root = pop(0)
            print(root)

            if root.left exists ?
                queue.push(root.left)
            if root.right exists ?
                queue.push(root.right)
        """
        print_queue = []
        print_queue.append(root)

        while print_queue :
            root = print_queue.pop(0)
            print(root.data)
            if root.left :
                print_queue.append(root.left)
            if root.right :
                print_queue.append(root.right)

if __name__ == "__main__":

    tree_obj = Tree()
    root = tree_obj.create_node(5)
    
    tree_obj.insert_element_rec(root,2)
    tree_obj.insert_element_rec(root,4)
    tree_obj.insert_element_rec(root,7)
    tree_obj.insert_element_rec(root,6)
    tree_obj.insert_element_rec(root,10)
    tree_obj.insert_element_rec(root,8)
    tree_obj.insert_element_rec(root,12)

    print("inorder --->>> ")
    tree_obj.traverse_inorder(root)

    print("pre order --->>>")
    tree_obj.traverse_preorder(root)

    print("post order --->")
    tree_obj.traverse_postorder(root)

    print("level order --->>>")

    tree_obj.traverse_levelorder(root)

    height = tree_obj.height_of_tree(root)

    print(f"Height of Tree is : {height}")