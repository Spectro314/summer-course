# print('\n\nExample 1\n')

# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2]
#     list2[0] = "hi"
#     list3 = "".join(list2)

# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list)
# print(a_str)

# print('\n\nExample 3\n')

# def double(my_list):
#     for i in range(len(my_list)):
#         my_list[i] = 2 * my_list[i]

# my_list = [1, 2, 3]
# double(my_list)
# print(my_list)

print('\n\nExample 4\n')

# pop()
def my_pop(my_list):
    return my_list[:-1]

# count()
def my_count(my_list):
    counter = 0
    for _ in my_list:
        counter += 1
    return counter

# extend
def my_extend(my_list, other_data):
    other_data = list(other_data)
    return my_list + other_data

# reverse
def my_reverse(my_list):
    return my_list[::-1]

# sort
def my_sort(my_list):
    sorted_list = []
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

my_list = [5, 3, 25, 4, 10]
popped = my_pop(my_list)
counted = my_count(my_list)
my_tuple = (1, 2)
extended = my_extend(my_list, my_tuple)
revrsd = my_reverse(my_list)
sortsort = my_sort(my_list)

print(popped)
print(counted)
print(extended)
print(revrsd)
print(sortsort)