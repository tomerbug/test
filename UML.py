class shape:
    def __init__(self,area , helef):
        self.__area = area
        self.__helef = helef

    def __str__(self):
            return f'area ={self.__area} , helef={self.__helef} '

    def __repr__(self):
            return f'{self.__area} {self.__helef}'
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, a):
        self.__area = a

    @property
    def helef(self):  # getter
        return self.__helef

    @helef.setter
    def helef(self , val):
        self.__helef = val


calc = shape(1, 2)
print(calc.area)
print(calc.helef)

calc.area = 7
calc.helef = 9
print(calc)



