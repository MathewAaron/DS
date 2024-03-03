class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None 

    def push_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node

    def push_end(self,data):

        new_node = Node(data)
        new_node.next = None 
        last = self.head
        while last.next :
            last = last.next 
        last.next = new_node

    def print_list(self):

        curr = self.head 
        print("###########################")
        while curr :
            print(curr.data)
            curr = curr.next
        print("###########################")    

    def reverse(self):

        prev = None
        curr = self.head 
        while curr :
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        self.head = prev

    def remove_duplicate(self):

        ptr1 , ptr2 = None, None 
        ptr1 = self.head 

        while (ptr1 is not None) and (ptr1.next is not None):

            ptr2 = ptr1 
            while ptr2.next :

                if ptr1.data == ptr2.next.data :
                    ptr2.next = ptr2.next.next
                else :
                    ptr2 = ptr2.next 
            ptr1 = ptr1.next

    def swap_nodes(self, x, y):

        if x == y :
            return 0
        
        prev_x = None
        curr_x = self.head
        while (curr_x) and (curr_x.data != x):

            prev_x = curr_x
            curr_x = curr_x.next
        print(f"Prev_x : {prev_x.data}, Curr_x : {curr_x.data}")
        prev_y = None 
        curr_y = self.head
        while (curr_y) and (curr_y.data != y):

            prev_y = curr_y
            curr_y = curr_y.next
        
        if (curr_y == None):
            raise Exception(f"Not Swapping! {curr_y} not found")
        elif (curr_x == None) :
            raise Exception(f"Not Swapping! {curr_x} not found")

        if prev_x :
            prev_x.next = curr_y
        
        if prev_y :
            prev_y.next = curr_x
            

        temp = curr_x.next 
        curr_x.next = curr_y.next
        curr_y.next = temp 

if __name__ == '__main__':

    LL = LinkedList()
    LL.push_begining(5)
    LL.push_begining(15)
    LL.push_begining(25)
    LL.push_begining(35)
    LL.push_begining(45)
    LL.push_begining(55)
    LL.push_begining(65)
    LL.push_end(25)
    LL.print_list()
    LL.swap_nodes(45,15)
    LL.print_list()