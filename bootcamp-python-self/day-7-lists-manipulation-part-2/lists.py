# Initial list of numbers
my_list = [3, 1, 4, 1, 5, 9, 2, 6]

# The sort() method sorts the list in-place (modifies the original list)
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Another list to demonstrate the sorted() function
another_list = [3, 1, 4, 1, 5, 9, 2, 6]
# The sorted() function returns a new sorted list, leaving the original list unchanged
sorted_list = sorted(another_list)
print(another_list)  # Output: [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted_list)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# The reverse() method reverses the elements of the list in-place
# Note: my_list was already sorted, so this will reverse the sorted list
my_list.reverse()
print(my_list)  # Output: [9, 6, 5, 4, 3, 2, 1, 1] - Corrected expected output after sort then reverse

# The count() method returns the number of occurrences of a specified value
print(my_list.count(1))  # Output: 2

# clear the list
# Re-initialize my_list for the clear() demonstration
my_list = [1, 2, 3, 4, 5]
# The clear() method removes all elements from the list, making it empty
my_list.clear()
print(my_list)  # Output: []