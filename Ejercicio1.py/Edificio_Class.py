class Edificio (): 
    def __init__ (self,name):
        self.name = name 

    #Creamos los gets y los sets para poder llamar y modificar los elementos del constructor:
    def set_name(self,name):
        self.name =name
    def get_name(self): 
        return self.name    
        