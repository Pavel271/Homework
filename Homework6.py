my_dict = {'Павел':2005, 'Пётр': 1989, 'Антон': 1998}
print(my_dict)
print(my_dict['Павел'])
my_dict.update({'Василий': 2000,
               'Виктор': 1980})
print(my_dict)
my_dict.pop('Пётр')
print(my_dict)
print(my_dict.get('Даниил'))


my_set = {1, 1, 2, 2, 'String', 'String', (1, 2, 3)}
print(my_set)
my_set.add(5)
my_set.add(6)
print(my_set)
print(my_set.discard('String'))
print(my_set)