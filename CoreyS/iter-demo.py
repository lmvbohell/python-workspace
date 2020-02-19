import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

# data = [100, 200, 300, 400]
## counter = itertools.cycle(('On', 'Off'))
# daily_data = list(zip(itertools.count(), data))
# # daily_data = list(zip(range(10), data))
# # # daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

# counter = itertools.repeat(2, times=3)
# squares = map(pow, range(10), itertools.repeat(2))
# squares = itertoools.starmap(paw, [(0, 2), (1, 2), (2, 2)])
# print(list(squares))
# result = itertools.combinations(letters, 2)   ## <> permutations (ger alla kombinationer)
# combined = itertools.chain(letters, numbers, names)
# for item in result:
#     print(item)
# selectors = [True, True, False, True]
# result = itertools.accumulate(numbers)
# result = itertools.compress(letters, selectors)
# for item in result:
#     print(item)
# with open('testl.log', 'r') as f:
#     header = itertools.islice(f, 3)
#     for line in header:
#         print(line, end='')

def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)

for key, group in person_group:
    print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()