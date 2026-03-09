unique: set = {1,2,3,4,5,6,6,7} # this is called a set
print(unique)

users = {'Guy': 1, 'Girl': 2}
print(users)

age = 10
name = 'bob'

print(f'Name: {name}, age: {age}')

def function(a: int, b: int) -> int:
    return a + b

print(function(1,2))

def hello(name: str, greeting: str) -> None:
    print(f'Hello, {greeting}, {name}')

hello('skibidi', 'hola')

input: str = input('Hello, how are you')
if input == 'hi':
    print('bye')

listy = [1,3,5,7,9]
listyy = [2,4,6,8,10]
for i in range(len(listyy)):
    listy.append(listyy[i])

listy.sort()
print(listy)


# lists = ['me', 'you', 'him', 'her']
#
# for i in range(4):
#     print(lists)
#
# while True:
#     user_input = input('enter an input')
#     if user_input is not None:
#         print('goob job')
#         break
#

# number = input('provide a number')
#
# try:
#     print(number)
# except:
#     print('thats not a number')
#
#
# def say_hi(name):
#     print('Hi, ' + name)
#
# def useless():
#     pass
#
# say_hi('kevin')
