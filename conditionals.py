# Example 1

# Declaramos Una Variable
qualification = input( "Introduce Tu Calificaciòn De La Certificaciòn AZ-900: " )

qualification = int(qualification)

# Preguntamos Si La Calificaciòn Es Menor a 700
if qualification < 700 :
    print(" Vees, Por No Estudiar ") #Si Es Menor A 700, Muestra Este Mensaje

elif qualification > 1000 :
    print( "Mientes !!!!, No Puedes Sacar Màs De Mil" )

else : # Si No Se Cumple El "if" Anterior, Pasa A Esta Linea
    print( "Felicidades, Pasa Por Tu Certificado" ) # Se Ejecuta Si Ninguno De Las Dos Condiciones Se Cumplen 

# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# Example 2

# Verificador De Mayoria De Edad.

age = input( "Introduce Tu Edad " )
age = int(age)

if  age >= 18 and age <= 100 :
    print( "Bienvenid@ Al Mamitas " )

elif age > 100 :
    print( "Si Vienes Acompañad@ De Tus Abuelitos, Si Te Podemos Fiar " )

elif age < 0 :
    print( "Ni Que Fueras Viajer@ Del Tiempo " )

else :
    print( "No Puedes Llevarte Esos Cigarros " )

# En Python No Existe Switch / Case.