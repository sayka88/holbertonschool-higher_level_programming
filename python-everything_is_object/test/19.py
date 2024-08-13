#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)      # Ожидается: [1, 2, 3]
print(new_list)     # Ожидается: [1, 2, 3]

print(new_list == my_list)  # Ожидается: True, так как значения списков равны
print(new_list is my_list)  # Ожидается: False, так как это разные объекты

