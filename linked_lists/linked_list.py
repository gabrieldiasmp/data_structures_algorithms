class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedListAlgo:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.head.next == None:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
        self.length -= 1

        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            
            ### My second solution (best one)
            for _ in range(index):
                temp = temp.next
            return temp
            
            ### My first solution
            # index_count = 0
            # while temp is not None:
            #     print(f"index: {index_count}")
            #     print(f"value: {temp.value}")
            #     if index_count == index:
            #         print("**** got into index!!")
            #         return temp.value
            #     else:
            #         temp = temp.next
            #         print(f"------- next value: {temp.value}")

            #         index_count += 1

    def set_value(self, index, new_value):
        
        temp = self.get(index)

        if temp:
            temp.value = new_value
            return True
        else:
            return False

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

if __name__ == "__main__":
    

    # print("------ Append example:")
    # my_linked_list = LinkedListAlgo(1)
    # my_linked_list.append(2)
    # my_linked_list.append(3)
    # my_linked_list.append(15)
    # my_linked_list.append(47)
    # my_linked_list.print_list()

    # print(f"Get index: {my_linked_list.get(4)}")

    # print("------ After pop:")
    # my_linked_list.pop()
    # my_linked_list.print_list()

    # print("------ After pop first:")
    # my_linked_list.pop_first()
    # my_linked_list.print_list()

    # print(f"------ New head: {my_linked_list.head.value}")

    print("------ Set value example:")
    my_linked_list = None
    my_linked_list = LinkedListAlgo(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(15)

    my_linked_list.set_value(index=2, new_value=47)
    my_linked_list.print_list()
    print(f"Head value: {my_linked_list.head.value}")
    print(f"Tail value: {my_linked_list.tail.value}")





