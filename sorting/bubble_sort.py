def bubble_sort_algo(my_list):

    try:
        if not isinstance(my_list, list):
            raise TypeError("Input should be a list")

        # Check if all elements in the list are comparable (numbers in this case)
        for item in my_list:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements in the list should be numbers (int or float)")

        # Sorting algo
        for i in range(len(my_list) - 1, 0, -1):
            for j in range(i):
                #print(f"------ STEP: {j} -------")
                #print(f"j = {my_list[j]}")
                #print(f"j+1= {my_list[j+1]}")
                if my_list[j] > my_list[j+1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # Swap
    except TypeError as te:
        return f"TypeError: {te}"
    
    except ValueError as ve:
        return f"ValueError: {ve}"

    print(my_list)
    return my_list

if __name__ == "__main__":
    list_to_be_sorted = [4, 4, 2, 6, 1, 3] #[1, 2, 3, 4, 5, 6] #[4,2,6,5,1,3] #[2, 6, 4, 5, 3, 1]
    bubble_sort_algo(list_to_be_sorted)