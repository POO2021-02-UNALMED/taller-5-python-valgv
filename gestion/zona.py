class Zona:

    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoologico = zoo
        self._animales = []
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)

    def getZoologico(self):
        return self._zoologico  

    def setZoo(self, zoo):
        self._zoologico = zoo     
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getAnimales(self):
        return self._animales
    
    def setAnimales(self, animales):
        self._animales = animales