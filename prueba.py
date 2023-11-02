"""
print("hola mundo")
print("hola mundo 2")
"""
"""
nigga
"""
"""#Variables
texto= "Oa"
nombre= "Adem Bougaoua Benabidi"
altura= "175cm"
year= "2023"

print (f"{texto} - {nombre} - {altura} - {year}")
"""
"""
#Entrada

sitioweb = input ("¿Cuál es tu página web?: ")
print("El sitio web del usuario es: " + sitioweb)
"""

"""
#Condiciones
altura= int(input("¿Cuál es tu altur?: "))
if altura >= 170:
    print("Eres una persona alta!!")
else:
    print("Eres enano")
    """
"""
#Funciones
var_altura= int(input("¿Cuál es tu altur?: "))

def mostrarAltura(altura):
    resultado = ""
    
    if altura >= 170:
        resultado = "Eres una persona alta!!"
    
    else:
        resultado = "Eres enano" 

    return resultado

print(mostrarAltura(var_altura))
"""
#Listas 
personas = ["Lotfi", "Joan", "Leo"]

print(personas[2])

for persona in personas :
    print("-" + persona)