class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, zona, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._zona = zona
        self._genero = genero
        _totalAnimales += 1
    
    def movimiento(self):
        return "desplazarse"
    
    #@classmethod
    #def totalPorTipo(cls):
    
    def toString(self):
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo().getNombre()

    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales
    
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