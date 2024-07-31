# while True:
#     number = int(input("Введите число "))
#     if number % 2 == 0:
#         print("Число чётное")
#         continue
#     else:
#         print("Число нечётное")
#     print("Меня не забыли")
# a=5


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    if my_list[a] < 0:
        break
    if my_list[a] > 0:
        print(my_list[a])
    a += 1
