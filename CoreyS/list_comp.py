""" Comprehensions  # Easy way to create lists[], dicts{}, tuple() and sets{} """
""" List Comprehensions = # #, Hard way = # """
# nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n)
# print(my_list)

# # print([n for n in nums])

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n*n)
# # my_list =  [n*n for n in nums]
# # print(my_list)

# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print my_list

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# # my_list = [n for n in nums if n%2 == 0]
# # print(my_list)

# Using a filter + lambda Svårläst, andvänd ovan.
# my_list = filter(lambda n: n%2 == 0, nums)
# print my_list

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# # my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# # print(my_list)

# Dictionary Comprehensions   # # list=[, tuple=(, dict={
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#print(zip(names, heros)) <<<<<<< Python2
# # print(list(zip(names, heros)))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict
# #my_dict = {name: hero for name, hero in zip (names, heros)}
# # my_dict = {name: hero for name, hero in list(zip(names, heros)) if name != 'Peter'}
# # print(my_dict)

# If name not equal to Peter

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# # my_set = {n for n in nums}
# print(my_set)

# Generator Expressions     # #Different than list, set and dict.
# I want to yield 'n*n' for each 'n' in nums
# nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# # my_gen = (n*n for n in nums) # #Körs med for nedan

# for i in my_gen:
#     print(i)

""" Iterators """
# # print(dir(nums))
# i_nums = iter(nums)    ##  <> nums.__iter__() 
# # print(next(i_nums))
# while True:
#     try:
#       item = next(i_nums)
#       print(item)
#     except StopIteration:
#         break
# # print(dir(i_nums))

# class MyRange:

#     def __init__(self, start, end):
#         self.value = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current


# def my_range(start, end):
#     current = start
# #     while True:
#       while current < end:
#         yield current
#         current += 1


# nums = my_range(1, 10)

# for num in nums:
#     print(num)

""" TEST nedan """
# my_sentence = Sentence('This is a test')
# my_s = []

# for word in my_sentence:
#   for n in my_sentence:
#     if n != ' ':
#       my_s.append(n)
#     elif n == ')':
#       break
#     else:
#       print(my_s)
#       my_s = [] 
# #  print(word)

##### Generator vs class  >>>>>>>
class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

""" Generator är lättlästa """
def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentence = sentence('This is a test')

# for word in my_sentence:
#     print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))


# This should have the following output:
# This
# is
# a
# test