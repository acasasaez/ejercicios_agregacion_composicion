class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 

print(yang is yin.yang) 

del(yang) 
print("?") 
print(" ")
#Reescribimos el código para que que el mensje "Yang destruido" aparezca antres que la interrogación:
class Yin: pass 
class Yang: 
    def __del__(self): 
        return "Yang destruido"
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 

print(yang is yin.yang) 

print(yang.__del__())

print("?") 

#La razón por la que ocurre esto es porque en el primer caso el valor se almacena en la memoria;
#el primer código no da resulatado en todoas las computadoras