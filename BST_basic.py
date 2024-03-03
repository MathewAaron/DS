class Node :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

class Tree:

    def create_node(self,data):

        return Node(data)
    
    def insert_element_rec(self,root,data):
        """
            Insert BST element using recursion
        """
        # first element
        if not root:
            return self.create_node(data)

        if data < root.data :
            root.left = self.insert_element(root.left,data)

        else: 
            root.right = self.insert_element(root.right,data)

        return root
    
    def traverse_inorder(self,root):

        if root :
            self.traverse_inorder(root.left)

            print(root.data)

            self.traverse_inorder(root.right)

    def traverse_preorder(self,root):

        if root :

            print(root.data)

            self.traverse_preorder(root.left)

            self.traverse_preorder(root.right)


    def traverse_postorder(self,root):

        if root :

            self.traverse_postorder(root.left)

            self.traverse_postorder(root.right)

            print(root.data)


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