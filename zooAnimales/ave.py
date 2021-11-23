from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, zona, genero, colorPlumas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._zona = zona
        self._genero = genero
        self._colorPlumas = colorPlumas
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "volar"
    
    #def crearHalcon(cls, nombre, edad, genero):
    
    #def crearAguila(cls, nombre, edad, genero):

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
    
    def getColorPlumas(self):
        return _colorPlumas
    
    def setColorPlumas(self, plumas):
        self._colorPlumas = plumas