class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ###################################### TWO POINTER TECHNIQUE
    def find_middle_node(self):

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        # temp = self.head
        
        # if self.length % 2 == 1:
        #     middle_index = int(self.length // 2)
        # else:
        #     middle_index = int(self.length / 2)
        
        # for _ in range(middle_index):
        #     temp = temp.next

        # return temp

if __name__ == "__main__":

    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    my_linked_list.append(6)

    print( my_linked_list.find_middle_node().value )



    """
        EXPECTED OUTPUT:
        ----------------
        3
        
    """