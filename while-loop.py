while True:
    username = input("What is your username? ")
    if username != 'admin':
        continue
    password = input("What is your password?")
    if password == 'topsecret':
            break
print('Authorised')

list = [1, 2, 1, 3, 2]
list.remove(2)
print(list)

favourite_fruits = {}
favourite_fruits['Alex'] = 'Apple'
favourite_fruits['Alex'] = 'Satsuma'
print(favourite_fruits)

favourite_colours = {'Alice': 'Purple', 'Bob': 'Green', 'Charlie': 'Scarlet'}
del favourite_colours['Bob']
print(favourite_colours)

list = ['fourteen', 'fifteen', 16, 'seventeen']

for item in list:
    try:
            msg = 'processing ' + item
            print(msg)
            continue
    except TypeError:
            print('something went wrong')
            break
    finally:
            print('finally block')
    print('next item please!')

#def format_string(msg, prefix = 'String: ', postfix) -> int:
#    print(prefix + msg + postfix)
#format_string('hello', postfix='.')

3 + 5 * 6 => 3 + (5*6)

