def saludo(nombre,app,año_nac):
    clave= nombre[1]+app[len(app)-1]+'_'+año_nac[3:5]
    return(clave)


def c_edad(año_nac):
    edad=2023-(int(año_nac[6:10]))
    return(edad)
    

def comparacion(palabra,largo):
    palabra= len(palabra)
    largo= int(largo)
    return(palabra==largo)

def r_correo(correo):
    arroba=int(correo.find('@')+1)
    correo=correo[arroba:]
    return(correo)
correo=input('ingrese el correo: ')
print (r_correo(correo))

#año_nac=input('INgrse año de nacimiento DD/MM/AAAA: ')
#palabra= input('ingrese la palabra: ')
#largo= input('ingrese el largo: ')
#print('la clave es: ',saludo(nombre,app,año_nac))    
#print('La edad de',nombre,'es: ',c_edad(año_nac))
#print(comparacion(palabra,largo))