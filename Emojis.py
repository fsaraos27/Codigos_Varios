# funcion 1
def crearEmojisSignificados():
    
    linea=""
    for i in range(3):
        emoji=input("Emoji: ")
        significado=input("Significado: ")
        linea+=emoji+"*"+significado+"$"
    
    linea = ":<#*como estás$:-!*nos juntamos más tarde $>=<*atrasado$"
    return linea

# funcion 2
def buscarEmojiSignificado(emojiBuscar,linea):
    largo=len(linea)
    emoji=""
    i=0
    while i < largo:
        caracter=linea[i:i+1]
        if caracter=="*":
            i+=1
            traduccion=""
            caracter=linea[i:i+1]
            while caracter!="$":
                traduccion+=caracter
                i+=1
                caracter=linea[i:i+1]
            return traduccion.upper() # OJO >> eliminar xq está condicionado a una pregunta (if)
            emoji=""       
        else:
            emoji+=caracter
        i+=1
# PP
linea=crearEmojisSignificados()
textoAtraducir=input("Hola :<#, por favor :-! porque voy >=<") #input()
textoTraducido=""
largo=len(textoAtraducir)
p=0
while p<largo:
    caracter=textoAtraducir[p:p+1]
    cod=ord(caracter)
    if (cod>=65 and cod<=90) or (cod>=97 and cod<=122) or cod==32 or cod==44:
        textoTraducido += caracter
    else:
        emojiBuscar=textoAtraducir[p:p+3]
        texto=buscarEmojiSignificado(emojiBuscar,linea)
        textoTraducido += texto
        print(emojiBuscar)
        print(textoTraducido)
        break # eliminar
    p+=1