# adding elements to a list
my_list = [1, 2, 3]
my_list.append(4)  # Add 4 to the end of the list

print(my_list)  # Output: [1, 2, 3, 4]

my_list.insert(1, 1.5)  # Insert 1.5 at index 1
print(my_list)  # Output: [1, 1.5, 2, 3, 4]

another_list = [5, 6]

my_list.extend(another_list)  # Extend the list by appending elements from another_list
print(my_list)  # Output: [1, 1.5, 2, 3, 4, 5, 6]


# removing elements from a list
my_list = [1, 1.5, 2, 3, 4, 5, 6]
my_list.remove(1.5)  # Remove the first occurrence of 1.5
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

popped_element  = my_list.pop()  # Remove and return the last element
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(f"Popped element: {popped_element}")  # Output: Popped element: 6

popped_element_at_index = my_list.pop(0)  # Remove and return the element at index 0
print(my_list)  # Output: [2, 3, 4, 5]
print(f"Popped element at index 0: {popped_element_at_index}")  # Output: Popped element at index 0: 1

del my_list[1]  # Delete the element at index 1
print(my_list)  # Output: [2, 4, 5]


# modifying elements in a list
my_list = [2, 4, 5]
my_list[0] = 20  # Change the first element to 20
print(my_list)  # Output: [20, 4, 5]

my_list[-1] = 50  # Change the last element to 50
print(my_list)  # Output: [20, 4, 50]