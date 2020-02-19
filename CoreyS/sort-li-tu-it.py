from operator import attrgetter

li = [9,1,8,2,7,3,6,4,5]
li1 = [-6,-5,-4,1,2,3]
ci = ['History', 'Math', 'Physics', 'CompSci']
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}

## print(8 in li)
for index, item in enumerate(ci, start=1):
    print(index, item)
print(' - '.join(ci))
print(' - '.join(ci).split(' - '))
# s_li = sorted(li, reverse=True)   """ Sorted funktion, mer flexibel """
# li.sort()           """ Sorted metod """
# print('Sorted Variabel:\t', s_li)
# print('Sorted Variabel:\t',)
# print('Original Variabel:\t',)
# s_di = sorted(di)
# print('Dict\t', s_di)
# print(li1)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employees = [e1,e2,e3]
"""Custum funktion, attrgetter eller lambda"""
# def e_sort(emp):
#     return emp.name
# s_employess = sort(employees, key=e_sort)
# s_employees = sorted(employees, key=attrgetter('age'))
s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees)