
# creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
list_of_lists = [[1, 2], [3, 4], [5, 6]]

print(empty_list)
print(*numbers)
print(*strings)
print(*mixed)
print(list_of_lists)


# accessing elements
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])


# slicing lists
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])

# mutability of lists
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)

fruits = ["apple", "banana", "cherry"]
fruits[-1] = "mango"
print(fruits)