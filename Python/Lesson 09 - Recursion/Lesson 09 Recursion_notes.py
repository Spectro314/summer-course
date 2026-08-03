def sum_list_recursion(num_list: list[int]) -> int:
    # Base case: single element
    if len(num_list) == 1:
        return num_list.pop(0)
    # Recursive case: sum the last element and the sum of the rest
    last = num_list.pop()
    print(f"Calculating {num_list[:]} + {last}")
    return sum_list_recursion(num_list[:]) + last
    
#     # Recursive case: sum the first element and the sum of the rest
#     return num_list[0] + sum_list_recursion(num_list[1:])



# print("Numbers using recursion:")
# print(f"sum_list_recursion([1, 2, 3, 4]) = {sum_list_recursion([1, 2, 3, 4])}")
# print(f"sum_list_recursion([9, 9]) = {sum_list_recursion([9, 9])}")
# print(f"sum_list_recursion([5]) = {sum_list_recursion([5])}")       
# print()

from unittest import result


def sum_list(input_list):
    if len(input_list) == 1:
        return 0
    
    result = input_list[0] + sum_list(input_list[1:])
    print(f"received {result} for {input_list}")
    
    return result   