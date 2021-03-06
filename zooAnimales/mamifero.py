from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, 'pradera', genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, 'selva', genero, True, 4)

    @classmethod
    def getMamifero(cls):
        return cls._listado
    
    @classmethod
    def setMamifero(cls, listado):
        cls._listado = listado
    
    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def getPatas(self):
        return self._patas
    
    def setpatas(self, patas):
        self._patas = patas