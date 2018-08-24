print ("Números primos:")

entrada=input("Entre com dois números separados por um espaço: ").split(" ")

#validar
validar=True
if len(entrada)!=2:
    print ("Número de parametros inválido!")
    validar=False

if validar:
    for (i, item) in enumerate(entrada):
        if not item.isnumeric():
            print ("O item ",i+1," (",item,"), não é um número!")
            validar=False
            break
if validar:
    if entrada[0] < entrada[1]:
        print ("O primeiro valor (",entrada[0],") deve ser menor que o segundo (",entrada[1],")")
        validar=False

if validar:
    ini=int(entrada[0])
    fim=int(entrada[i])
    if ini<2:
        ini=2
    primos=""
    for numero in range(ini, fim):
        for i in range(2,numero):
            if numero % i == 0: break
        else:
            if primos!="":
                primos=primos+", "
            primos=primos+str(numero)
            
    print ("Primos: ",primos)

