from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, zona, genero, colorEscamas, cantidadAletas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._zona = zona
        self._genero = genero
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    
    #def crearSalmon(cls, nombre, edad, genero):
    
    #def crearBacalao(cls, nombre, edad, genero):

    def getNombre(self):
        return _nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return _edad
    
    def setEdad(self, edad):
        self._edad =  edad

    def getHabitat(self):
        return _habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat 

    def getGenero(self):
        return _genero
    
    def setGenero(self, genero):
        self._genero = genero
    
    def getZona(self):
        return _zona
    
    def setZona(self, zona):
        self._zona = zona    
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    
    def getColorEscamas(self):
        return _colorEscamas
    
    def setColorEscamas(self, col):
        self._colorEscamas = col

    def getCantidadAletas(self):
        return _cantidadAletas
    
    def setCantidadAletas(self, aletas):
        self._cantidadAletas = aletas