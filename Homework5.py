immutable_var = 1, True, 'String'
print(immutable_var)
immutable_var [0] = 5
print(immutable_var)
# Элементы кортежа нельзя изменять, потому что происходит обращение к элементу в списке, а не в сам список.

mutable_list = [1, True, 'String']
print(mutable_list)
mutable_list [0] = 5
print(mutable_list)