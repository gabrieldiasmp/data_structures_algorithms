# Key Concept: Passing Objects by Reference

In Python, when you assign an object (like an instance of a class) to a variable or pass it to a function, you are not copying the object itself. Instead, you are working with a reference to the original object. This means that multiple variables can point to the same object in memory. Any changes made through one reference will be reflected when accessing the object through any other reference.

## Important Clarification:

- **Primitive types** (like integers, floats, booleans) are immutable, so when you pass them to a function, you cannot change the original value directly.
- **Objects** (like lists, dictionaries, or class instances) are mutable, so when passed to a function, you can modify their internal state, because the function receives a reference to the same object in memory.

## How Object References Work:

### Creating an Object:
When you create an object, Python stores it in memory and returns a reference (like a "pointer" or "handle" to that memory location).

```python
node = Node(5)
```

Here, `node` is not the object itself but a reference to the `Node` object that is stored somewhere in memory. This means `node` "points" to the memory location where the `Node` object with `value = 5` is stored.

### Assigning the Object to Another Variable:
If you assign this `node` to another variable, both variables now refer to the same object in memory.

```python
temp = node
```

Now, both `temp` and `node` are references to the same object in memory. If you modify the object through `temp`, the change will be visible when accessing `node`.

```python
temp.value = 10  # Modifies the value through temp
print(node.value)  # Outputs 10, because both refer to the same object
```

### Passing the Object to a Function:
When you pass `node` as an argument to a function, Python passes the reference (not a copy of the object). This allows the function to modify the original object.

```python
def modify_node(n):
    n.value = 20  # Modifies the value of the original object

modify_node(node)
print(node.value)  # Outputs 20, because the object itself was modified
```

## Example: Using `set_value`

The `set_value` method demonstrates how passing objects by reference works.

```python
def set_value(self, index, new_value):
    temp = self.get(index)

    if temp:
        temp.value = new_value
        return True
    else:
        return False
```

### Breakdown of set_value:
- **Getting the Node**:

The method get(index) retrieves the node at the specified index and assigns it to temp. This node is a reference to an actual Node object in memory.

- **Modifying the Node's Value**:

If temp is not None (meaning a node was found), the value of this node is updated with new_value using temp.value = new_value. Since temp is a reference to the node, this change affects the original node in the linked list.

- **Return Statement**:

The method returns True if the value was successfully set, allowing the caller to know the operation was successful.
This demonstrates that even though temp is a temporary variable, it directly references the node in the linked list. Therefore, modifications made through temp are reflected in the linked list structure itself.