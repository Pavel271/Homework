# def test_func(*params):
#     print('Тип', type(params))
#     print('Аргумент:', params)
#
# test_func(1, 2, 3, 4)
# 2
# def summator(txt, *values, type='sum'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
# print(summator('Сумма чисел: ', 2, 3, 4, type='summator'))
#
# 3
# def info(value, *types, name='Pavel', **values):
#     print('Тип', type(values))
#     print('Аргумент:', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
# info('Пример использования параметров всех типов', 2, 3, 4, name = 'Pavel', course = 'Python')


# def my_sum(n, *args, txt='Сумма чисел'):
#     s = 0
#     for i in range(len(args)):
#         s += args[i] ** n
#     print(txt + ':', s)
#
# my_sum(1, 1, 2, 3, 4, 5)
# my_sum(2, 1, 2, 3, 4, 5, txt = 'Сумма квадратов')

def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for i in other_words:
        other_words_lower = i.lower()
        if root_word_lower in other_words_lower or other_words_lower in root_word_lower:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)