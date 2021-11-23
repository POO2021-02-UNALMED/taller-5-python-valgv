from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, zona, genero, colorPiel, venenoso):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._zona = zona
        self._genero = genero
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"
    
    #def crearRana():
    
    #def crearSalamandra(cls, nombre, edad, genero):

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
    
    def getColorPiel(self):
        return _colorPiel
    
    def setColorPiel(self, col):
        self._colorPiel = col

    def getVenenoso(self):
        return _venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso =  venenoso