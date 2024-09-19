team1_num = 10
team2_num = 8
score_1 = 22
score_2 = 33
team1_time = 2426.3
team2_time = 1364.3

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result

tasks_total = score_1 + score_2

time_avg = round(((team1_time / score_1) + (team2_time / score_2)) / 2,2)


print('Использование %:')
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

print('Использование format():')
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} c!'.format(team1_time))

print('Использование f-строк:')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')