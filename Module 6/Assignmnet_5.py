def filter_even_numbers(original_list):
    for n in original_list:
        if n % 2 != 0:
            original_list.remove(n)
    return original_list


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", original_list)
print("List with even numbers only:", filter_even_numbers(original_list))