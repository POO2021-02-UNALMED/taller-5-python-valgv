from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        Animal._totalAnimales += 1
        self._colorPlumas = colorPlumas
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None 
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, 'montanas', genero, 'cafe glorioso')
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, 'montanas', genero, 'blanco y amarillo')
    
    @classmethod
    def getAve(cls):
        return cls._listado
    
    @classmethod
    def setAve(cls, listado):
        cls._listado = listado
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, plumas):
        self._colorPlumas = plumas