#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

peso_kg = float(input("Inserta tu peso en kg: "))
estatura_metros = float(input("Inserta tu estarua en metros(Ej. 1.95m): "))

IMC = float(peso_kg / (estatura_metros**2))

print(f"Tu índice de masa corporal es de {IMC}")