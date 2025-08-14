
# name = "shaun"
# age = 20
# nums = [1,2,3,4]
 
# print (f'Name is', type(name), '. Age is', type(age), '. Nums is', type(nums))
# print (name.upper())
#============

class Planet:
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 20000
        self.gravity = 5.5
        self.system = 'Hoth System'
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet()
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')
print(hoth.orbit())