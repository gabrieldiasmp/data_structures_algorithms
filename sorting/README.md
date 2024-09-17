## Bubble Sort

Write a function called `bubble_sort` that sorts a list of integers in ascending order using the Bubble Sort algorithm.

### The function should perform the following tasks:

1. **Accept a parameter** `my_list` that represents the list of integers to be sorted.
2. **Iterate through the list** from the last element to the first element. For each element `i`, perform the following steps:
   - Iterate through the list from the first element to the element at position `i - 1`. For each element `j`, perform the following steps:
     - Compare the element at position `j` with the element at position `j + 1`.
     - If the element at position `j` is greater than the element at position `j + 1`, **swap the two elements**.
3. **Return the sorted list**.

## Selection Sort