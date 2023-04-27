class Piloto:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__fechaNacimiento = None
        self.__pais = None
        self.__salarioAnual = None


    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato
        
        