'''
# Duck Typing and Easier to ask forgiveness than permission (EAFP)
# We care if it's can do what we ask (not what kind of object it's).
'''

# Example from the Python Docs
# Easyer to ask forgivness then permission <<<<
# https://www.tutorialspoint.com/python/python_exceptions.htm 

import os

my_file = "/home/bohell/Python_Workspace/test.txt"

# # Race Condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File can not be accessed')

# No Race-Condition
try:
    f = open(my_file)
    if f.name == 'Currupt_test.txt':
        raise Exception     # Egna error-kod Går ner till except Exception....
#    bad = bad_var
except FileNotFoundError:
    print('File does not exist!')
except IOError as e:
    print('File can not be accessed')
except Exception as e:
    print(e)        # (e) ger>> "name 'bad_var' is not defined"
else:
    with f:
        print(f.read())
        f.close()
finally:            # Körs alltid. Här kan t.e.x. stänga databas/fil mm.
    pass


# class Duck:
    
#     def quack(self):
#         print('Quack, quack')

#     def fly(self):
#         print('Flap, Flap!')

# class Person:

#     def quack(self):
#         print("I´m Quackiong Like a Duck!")

#     def fly(self):
#         print("I´m Flapping my Arms!")

# def quack_and_fly(thing):
#     # EAFP (Pythonic)
#     try:
#         thing.quack()
#         thing.fly()
#         ##thing.bark()
#     except AttributeError as e:
#         print(e)
#     # # Not Duck-Typed(Non-Pythonic)
#     # if isinstance(thing, Duck):
#     #     thing.quack()
#     #     thing.fly()
#     # else:
#     #     print('This has to be a Duck!')
    
#     print()

# d = Duck()  #Instans of class Duck
# quack_and_fly(d)    #Funktion

# p = Person()
# quack_and_fly(p)

# Duck Typing and Easier to ask forgiveness than permission (EAFP)

# person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}   #Dictionary
# #person = {'name': 'Jess', 'age': 23}

# # LBYL (Non-Pythonic)
# # if 'name' in person and 'age' in person and 'job' in person:
# #     print("I´m {name}. I´m {age} years old and I am a {job}".format(**person))
# # else:
# #     print('Missing some keys')

# #EAFP (Pythonic)
# try:
#     print("I´m {name}. I´m {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))

# my_list = [1, 2, 3, 4, 5, 6]
# #Pythonic
# try:
#     print(my_list[5])
# except IndexError:
#     print('That index does not exist')

'''
###-Variable Scope - Understanding the LEGB rule and global/nonlocal statements
LEGB  -Local, Enclosing, Global, Built-in   (nonlocal)
'''
# #import builtins
# #print(dir(builtins))
# x = 'global x'

# def outer():
#     x = 'outer x'
#     print(x)
#     def inner():
#         x = 'inner x'
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)