import os
from module1hard import dict_

print('Текущая директория:', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория:', os.getcwd())
os.chdir(r'D:\PyCharm Community Edition 2022.2.4\UniversityUrbant')
print('Текущая директория:', os.getcwd())
print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
