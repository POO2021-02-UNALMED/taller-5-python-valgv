from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, zona, genero, pelaje, patas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._zona = zona
        self._genero = genero
        self._pelaje = pelaje
        self._patas = patas
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    #def crearCaballo(cls, nombre, edad, genero):

    #def crearLeon(cls, nombre, edad, genero):

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
    
    def getPelaje(self):
        return _pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def getPatas(self):
        return _patas
    
    def setpatas(self, patas):
        self._patas = patas