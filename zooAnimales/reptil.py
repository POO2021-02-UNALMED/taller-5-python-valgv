from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(nombre, edad, 'humedal', genero, 'verdes', genero)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(nombre, edad, 'jungla', genero, 'blanco', 1)
    
    @classmethod
    def getReptil(cls):
        return cls._listado
    
    @classmethod
    def setReptil(cls, listado):
        cls._listado = listado
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largo):
        self._largoCola = largo