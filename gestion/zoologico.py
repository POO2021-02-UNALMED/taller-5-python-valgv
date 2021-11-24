from zooAnimales.animal import Animal

class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        animales = 0;
        for i in range(len(self.getZona)):
            zonaS = self.getZona()[i]
            a = zonaS.getAnimales()
            animales+=len(a)
        return animales    

    def getZona(self):
        return Zoologico._zonas
    
    def setZonas(self, zonas):
        Zoologico._nombre = zonas    
         
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._nombre = ubicacion
    
    