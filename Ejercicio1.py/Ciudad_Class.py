class Ciudad(): #Definimod la clase ciudad 
    def __init__(self, name) :#La clase ciudad cuenta con el atributo del nombre
        self.name = name
        self.edificios =[] #los elementos de la lista serán objetos de la clase edificio
        self.persona = []#los elementos de la lista serán de la clase persona
    #Mediante atributos le inducimos las relaciones de composición
    #si destruimos la ciudad (cataciclismo) desaparecen las personas y los edificios
    # (lo tomamos como una relación de composición) 

    #Creamos los gets y los sets para poder llamar y modificar los elementos del constructor:
    def set_name(self,name):
        self.name =name
    def get_name(self): 
        return self.name


    
    
    

    