def selection_sort_algo(list_to_be_sorted):

    try:
        if not isinstance(list_to_be_sorted, list):
            raise TypeError("Input should be a list")
        
        for item in list_to_be_sorted:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements in the list should be numbers (int or float)")

        ### Selection sort algorithm
        for i in range(len(list_to_be_sorted) - 1):
            min_index = i
            for j in range(i+1, len(list_to_be_sorted)):
                if list_to_be_sorted[min_index] > list_to_be_sorted[j]:
                    min_index = j
            list_to_be_sorted[i], list_to_be_sorted[min_index] = list_to_be_sorted[min_index], list_to_be_sorted[i]
    
    
    except TypeError as te:
        return f"TypeError: {te}"
    
    except ValueError as ve:
        return f"ValueError: {ve}"

    print(list_to_be_sorted)
    return list_to_be_sorted

if __name__ == "__main__":
    
    list_to_be_sorted = [3, 6, 4, 5, 1, 2]
    selection_sort_algo(list_to_be_sorted)