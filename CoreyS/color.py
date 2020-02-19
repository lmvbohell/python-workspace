from colorama import init, Fore, Back, Style
init()
# print(Fore.RED + 'Red')
# print(Fore.GREEN + 'Green')
# print(Fore.BLUE + 'Blue')
# print(Style.RESET_ALL)

class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print(Fore.RED + f'Name is: {hoth.name}')
print(Fore.WHITE + f'Radius is: {hoth.radius}')
print(f'the gravity is: {hoth.gravity}')
print(hoth.orbit())

naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name is: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())
