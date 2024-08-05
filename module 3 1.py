def count_calls(call):
    global calls
    calls += call
    return calls

def string_info(string):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a

def is_contains(string_info, is_contains):
    string_info.lower()
    new_contains = []
    count_calls(1)
    for i in is_contains:
        new_contains.append(i.lower())
    return (string_info.lower() in new_contains)


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)