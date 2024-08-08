# 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 7)
print_params(a = 2, b = 'компьютер')
print_params(a = 6, b = 'автомобиль', c = False)
print_params(b = 25)
print_params(c = [1,2,3])
# 2
values_list = [741, 'телефон', True]
values_dict = {'a': 852, 'b': 'тетрадь', 'c': False}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = ['string', True]
print_params(values_list_2, 42)