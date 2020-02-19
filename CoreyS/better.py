## Youtube -10 Python Tips and Tricks For Writing Better Code (Corey Schafer)

# -If else på en rad
# condition = False
# x = 1 if condition else 0
# print(x)

# # -Stora siffror, "_" för att "se" bättre (funkar fint i python). 
# # num1 = 10000000000
# num1 = 10_000_000_000
# # num2 = 100000000
# num2 = 100_000_000
# total = num1 + num2
# print(total)
# print(f'{total:,}')

#-Fil, öppna>läsa>stänga en fil.
#f = open('test.txt', 'r')
#file_contents = f.read()
#f.close()
#-Kod nedan(contents manager) ersätter 3 raderna ovan. Contents även vid db mm. <<<<<<
# with open('test.txt', 'r') as f:
#     file_contents = f.read()
# words = file_contents.split('')
# words_count = len(words)
# print(words_count)

#-Räknare när man loopar över något. enumerate retunerar både index och värde
# names = ['Corey', 'Chris', 'Dave', 'Travis']
# # index = 0
# # for name in names:
# #     print(index, name)
# #     index += 1
# ## for index, name in enumerate(names, start=1):
# for index, name in enumerate(names):
#     print(index, name)

# Loopa igenom 2 eller flera listor(list). Då kan man använda zip funktionen. Tips Itertools Module.
# Return a tuple. fore value skriver ut en tuple av de 3 värdena (Peter P, Spiderm, Marv)
# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# # for index, name in enumerate(names):
# #     hero = heroes[index]
# #     print(f'{name} is actually {hero}')
# # # for value in zip(names, heroes):
# # #     print(value)
# for name, hero in zip(names, heroes):
#     print(f'{name} is actually {hero}')

# -Unpack different value (list or tuple, i detta fall är det en tuple)
# -Om ett värde i tuple ej ska användas alt. ej skrivas ut
# # Normal
# # items = (1,2)   # Old way. Detta är en tuple av 2 värden (1,2)
# # print(items)

# # Unpacking
# # a, b = (1, 2)
# ## a, b, *c, d = (1, 2, 3, 4, 5)   - print(c) = [3, 4] dvs resten. '_' or '*_' nedan > ointressant värde.
# a, _ = (1, 2)

# print(a)
# #print(b)

# -Getting or setting attribute för ett object. Fånga atribute från ett object.
# OBS SETATTR/GETATTR är bra att förstå!!! <<<<<<<<<<<<<<<<<
# class Person():
#     pass
# person = Person()
# # first_key = 'first'
# # first_val = 'Corey'
# # setattr(person, first_key, first_val)
# # first = getattr(person, first_key)
# # print(first)
# person_info = {'first': 'Corey', 'last': 'Schafer'}
# for key, value in person_info.items():
#     setattr(person, key, value)
# for key in person_info.keys():
#     print(getattr(person, key))

# # -Hiding password and secret keys...  Python ibyggda funktion getpass
# from getpass import getpass
# username = input('Username: ')
# ##password = input('Password: ')    <<<password syns på skärmen här, inte bra!!
# password = getpass('Password: ')
# print('Logging In....')

## -m "modul" -c "argument" -n "argument". Import modul för att se vilka argument den kräver. <<<<<<<<
## import smtp -> help(smtpd)
## from datetime import datetime -> help(datetime)/dir(datetime) > datetime.today/datetime.today()
# python -m smtpd -c DebuggingServer -n localhost:1025

