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

Here, node is not the object itself but a reference to the Node object that is stored somewhere in memory. This means node "points" to the memory location where the Node object with value = 5 is stored.