#1)	El centro meteorológico de Coyhaique recomienda 
#que sí Está lloviendo y está soplando el viento, 
# o nevando las personas permanezcan por 
# precaución en sus casa. 
for i in range(1,17):
    print("Sr(a) meteorolog@ responda:") 
    print("0 si no esta lloviendo")
    print("ingrese otro numero si está lloviendo")
    p=int(input())
    print("Sr(a) meteorolog@ responda:") 
    print("0 si no esta soplando viento")
    print("ingrese otro numero si esta soplando viento")
    q=int(input())
    print("Sr(a) meteorolog@ responda:") 
    print("0 si no esta nevando")
    print("ingrese otro numero si esta nevando")
    r=int(input())
    p=bool(p)
    q=bool(q)
    r=bool(r)
    if((p and q)or r):
        print("Debe quedarse en casa")
    else:
        print("Puede salir")
