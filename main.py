def delete_occurrences(lst, element):
    modified_list = [x for x in lst if x != element]
    return modified_list

# Example usage:
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_delete = 2
updated_list = delete_occurrences(my_list, element_to_delete)
print("Updated list:", updated_list)
