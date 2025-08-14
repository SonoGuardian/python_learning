class Planet:

#class level atributes
    shape='round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

#has access to class level atributes (like shapes)
    @classmethod
    def commons(cls):
        return(f'All planets are {cls.shape} because of gravity')

#only have access to parameters that we pass into it individualy
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'