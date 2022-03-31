class Empresa: #Clase empresa
    def __init__(self,name):#La empresa cuenta con un atributo, el nombre
        self.name = name
        self.edificios =[]
        self.personas = []
        #Mediante atributos inducimos las relaciones de agrgación, 
        #nuestra empresa está compuesta por edificios y personas (empleados)
        #sin embargo, si destruímos la empresa esto no implica la desaparición de los edificios y empleados
        #Creamos los gets y los sets para poder llamar y modificar los elementos del constructor:
    def set_name(self,name):
        self.name =name
    def get_name(self): 
        return self.name
    
    def get_edificios (self, edificios):
        self.edificios.append(edificios)
        return self.edificios

    def get_personas (self, personas):
        self.persona.append(personas)
        return self.persona
