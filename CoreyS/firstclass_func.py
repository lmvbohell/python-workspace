""" First-Class Functions -Andvänds vid logging, Closures and Decorator """

# def html_tag(tag):

#     def wrap_text(msg):
#         print('<{0}>{1}</{0}>'.format(tag, msg))

#     return wrap_text

# print_h1 = html_tag('h1')   #Raden gör inget (förutom tag'en nedan). = Wrap_text function.
# print_h1('Test Headline!')
# print_h1('Another Headline!')

# print_p = html_tag('p')
# print_p('Test Paragraph!')

""" Closures (Has memory of prev function) - How to Use Them and Why They Are Useful """

# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)


# def logger(func):
#     def log_func(*args):
#         logging.info(
#             'Running "{}" with arguments {}'.format(func.__name__, args))
#         print(func(*args))
#     return log_func


# def add(x, y):
#     return x+y


# def sub(x, y):
#     return x-y

# add_logger = logger(add)
# sub_logger = logger(sub)

# add_logger(3, 3)
# add_logger(4, 5)

# sub_logger(10, 5)
# sub_logger(20, 10)

""" Decorators """

# def outer_function(msg):
#     def inner_function():
#         print(msg)      # Free Varible
#     #return inner_function()
#     return inner_function   # Return function without executing it.

# #outer_function()
# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

""" Samma Decorators i 2 funktioner kräver * ** """

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function     # Ersätter "display = decorator_function(display)", samma sak.
# def display():
#     print('display function ran')

# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Johan', 25)
# display()

# #display = decorator_function(display)
# # decorated_display = decorator_function(display)
# # decorated_display()

""" Decorators in decorators Display & logg-fil """
# Decorators
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info = my_logger(my_timer(display_info)) = @my_logger, @my_timer

display_info('Tom', 22)