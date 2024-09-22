# 01 - LL: Find Middle Node
Implement the `find_middle_node method` for the `LinkedList` class. 

Note: this `LinkedList` implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

- The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
- When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
- The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once. In other words, you can only use one loop.

# 02 - LL: Has Loop

Write a method called `has_loop` that is part of the linked list class. This method should detect if there is a cycle or loop present in the linked list using **Floyd's cycle-finding algorithm** (also known as the **"tortoise and the hare"** algorithm).

## Algorithm Explanation:

Floyd's algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves **one step** at a time, while the fast pointer moves **two steps** at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

### Guidelines:

1. **Initialize two pointers**, `slow` and `fast`, both initially pointing to the head of the linked list.
2. Traverse the list:
   - The `slow` pointer moves **one step** at a time.
   - The `fast` pointer moves **two steps** at a time.
3. **If a loop exists**, the fast pointer will eventually meet the slow pointer at some node.
   - In this case, return `True`.
4. **If no loop exists**, the fast pointer will encounter the end of the list (`None`).
   - In this case, return `False`.
