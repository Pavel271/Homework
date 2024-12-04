import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users( 
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL, 
email TEXT NOT NULL, 
age INTEGER, 
balance INTEGER NOT NULL 
) 
''')
users_data = (
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
)
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)
cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id IN (SELECT id FROM Users WHERE id % 2 = 1)')
cursor.execute('DELETE FROM Users WHERE id IN (SELECT id FROM Users WHERE id % 3 = 1)')
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
result = cursor.fetchall()

for username, email, age, balance in result:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')
connection.commit()
connection.close()

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM users WHERE id = 6")
connection.commit()

cursor.execute("SELECT COUNT(*) FROM users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM users")
all_balances = cursor.fetchone()[0]

if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0
print(average_balance)
connection.close()