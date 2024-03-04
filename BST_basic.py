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

    def sum_of_tree(self,root):
        """
            if root is None; return 0

            if root.left exists ; left = sum_of_tree(root.left)t else left = 0
            if root.right exists ; right = sum_of_tree(root.right) else right = 0

            return root.data + left + right
        """

        if not root :
            return 0
        left = self.sum_of_tree(root.left)
        right = self.sum_of_tree(root.right)

        return root.data + left + right
    
    def reverse_a_bst(self,root):
        """
            checks if root is None : returns 0
            
            i.e. left , right     =  end of elements right , end of elements left
            root.left , root.right = reverse_a_bst(root.right), reverse_a_bst(root.left)
        """
        if root is None :
            return 0

        root.left, root.right = self.reverse_a_bst(root.right), self.reverse_a_bst(root.left)
        return root

    def find_max_element(self,root):

        """
            Checks if root is none : returns 0

            returns max(root.data, find_max_element(root.left), find_max_element(root.right))
        """
        if root is None:
            return 0
        
        return max(root.data,self.find_max_element(root.left),self.find_max_element(root.right))
    
    def search_element(self,root,value):
        """
        Checks if root is None: returns False

        returns root.data == value or search_element(root.left) or search_element(root.right)
        """
        if root is None :
            return False
        return root.data == value or self.search_element(root.left,value) or self.search_element(root.right,value)
    
    def is_tree_balanced(self,root):
        """
            base condition
            if root is None:
                return [True,-1]
            recursively gets 
                    left, right 
            checks for balance
            if left[0] and right[0]:
                balanced = abs(left[1]-right[1]) <= 1
            return [balanced, max(left,right)+1]
        """
        def dfs(root):
            if root is None:
                return [True,-1]
            left, right = dfs(root.left),dfs(root.right)
            balanced = abs(left[1] + right[1]) <= 1 and left[0] and right[0]

            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]
    
    def max_path_sum(self,root):
        max_sum = root.data

        def dfs(root):
            if root is None:
                return 0
            # dont add negative values
            left, right = max(0,dfs(root.left)), max(0,dfs(root.right))
            max_sum = max(max_sum,root.data + left + right)
            return root.data + max(left , right)
        
        dfs(root)

        return max_sum

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
    
    sumTree = tree_obj.sum_of_tree(root)
    print(f"sum of tree -->> {sumTree}")

    # tree_obj.reverse_a_bst(root)
    # tree_obj.traverse_inorder(root)
    tree_obj.find_max_element(root)
    print(f"Max element in the tree is : {tree_obj.find_max_element(root)}")

    element_flag = tree_obj.search_element(root,12)
    print(f"Element found : {element_flag}")
    element_flag = tree_obj.search_element(root,50) # should print false
    print(f"Element found : {element_flag}")

    balanced_flag = tree_obj.is_tree_balanced(root)
    print(f"Is the tree balanced? {balanced_flag}")