def trocar (listaptroca):
    auxlista=['oi']
    total=len(listaptroca)
    auxlista = listaptroca[total-1]
    for x in range(total-1, 1, -1):
        listaptroca [x]=listaptroca[x-1]
        if(x==2):
            listaptroca[1] = auxlista

    return(listaptroca)


def qtde(times,listamenu):
    if(times<1):
        return(listamenu)
    else:
        listamenu.clear()
        for x in range(times):
            time=input('Digite o nome do time')
            listamenu.append(time)
        return(listamenu)


    #  começo do programa


pontos={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
vitorias={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
empate={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
golspro={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
saldodegols={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
golscontra={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
derrotas={'corinthians':0,'palmeiras':0,'santos':0,'flamengo':0,'botafogo':0,'sport':0}
lista=['corinthians','palmeiras','santos','flamengo','botafogo','sport']
qtdetime=input('digite a quantidade de times')
listaderesultado=[]
lista= qtde(int(qtdetime),lista)
from random import randint



if(len(lista)%2==0):
    ultimo=len(lista)
    fim=ultimo/2
    for i in range(ultimo-1):
        ultimo = len(lista)
        if (i==0):
            print('\n',i+1,'RODADA \n')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2= (randint(0,5))
                print(lista[x],resultado1,' x ',resultado2,lista[ultimo-1])
                golspro[(lista[x])]= golspro[(lista[x])] +resultado1
                golscontra[(lista[x])] += resultado2
                golspro[(lista[ultimo-1])]+=resultado2
                golscontra[(lista[ultimo - 1])] += resultado1

                if (resultado1 == resultado2):
                    empate[lista[ultimo - 1]] = empate[lista[ultimo - 1]] + 1
                    empate[lista[x]] = empate[lista[x]] + 1
                else :
                    if(resultado1 > resultado2):
                        vitorias[lista[x]]+= 1
                        derrotas[lista[ultimo-1]]+= 1
                    else:
                        vitorias[lista[ultimo-1]]= vitorias[lista[ultimo-1]]+1
                        derrotas[lista[x]]=derrotas[lista[x]]+1
                ultimo -= 1



        else:
            lista= trocar(lista)
            print('\n',i+1,' RODADA\n')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[x],resultado1,' x ',resultado2,lista[ultimo-1])
                golspro[(lista[x])] += resultado1
                golscontra[(lista[x])] += resultado2
                golspro[(lista[ultimo - 1])] += resultado2
                golscontra[(lista[ultimo - 1])] += resultado1

                if (resultado1 == resultado2):
                    empate[lista[ultimo - 1]] +=  1
                    empate[lista[x]] += 1
                else:
                    if (resultado1 > resultado2):
                        vitorias[lista[x]] +=  1
                        derrotas[lista[ultimo - 1]] +=  1
                    else:
                        vitorias[lista[ultimo - 1]] += 1
                        derrotas[lista[x]]+= 1
                ultimo -=1



    ultimo = len(lista)
    lista= trocar(lista)
    for cont in range(ultimo-1):
        ultimo = len(lista)
        if (cont==0):
            print('\n',cont+i+2,'RODADA \n')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[ultimo-1],resultado1,' x ',resultado2,lista[x])
                golspro[(lista[x])] += resultado2
                golscontra[(lista[x])] += resultado1
                golspro[(lista[ultimo - 1])] += resultado1
                golscontra[(lista[ultimo - 1])] += resultado2

                if (resultado1 == resultado2):
                    empate[lista[ultimo - 1]] += 1
                    empate[lista[x]] += 1
                else:
                    if (resultado2 > resultado1):
                        vitorias[lista[x]] += 1
                        derrotas[lista[ultimo - 1]] += 1
                    else:
                        vitorias[lista[ultimo - 1]] +=1
                        derrotas[lista[x]] +=1
                ultimo -=1


        else:
            lista= trocar(lista)
            print('\n',cont+i+2,' RODADA\n')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[ultimo - 1], resultado1, ' x ', resultado2, lista[x])
                golspro[(lista[x])]+= resultado2
                golscontra[(lista[x])] += resultado1
                golspro[(lista[ultimo - 1])] += resultado1
                golscontra[(lista[ultimo - 1])] += resultado2

                if (resultado1 == resultado2):
                    empate[lista[ultimo - 1]] +=1
                    empate[lista[x]] += 1
                else:
                    if (resultado2 > resultado1):
                        vitorias[lista[x]] += 1
                        derrotas[lista[ultimo - 1]] += 1
                    else:
                        vitorias[lista[ultimo - 1]] +=1
                        derrotas[lista[x]] += 1
                ultimo -= 1



else:
    print ('é impar')
    ultimo = len(lista)
    fim = (ultimo-1) / 2
    for i in range(ultimo - 1):
        ultimo = len(lista)
        if (i == 0):
            print('\n', i + 1, 'RODADA \n')
            print(lista)
            print('NESTA RODADA', lista[ultimo - 1], 'NÃO JOGOU')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[x],resultado1, ' x ',resultado2, lista[ultimo - 2])
                ultimo = ultimo - 1

        else:
            lista = trocar(lista)
            print('\n', i + 1, ' RODADA\n')
            print('NESTA RODADA', lista[ultimo - 1], 'NÃO JOGOU')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[x], resultado1, ' x ', resultado2, lista[ultimo - 2])
                ultimo = ultimo - 1



    ultimo = len(lista)
    lista = trocar(lista)
    for cont in range(ultimo - 1):
        ultimo = len(lista)
        if (cont == 0):
            print('\n', cont + i + 2, 'RODADA \n')
            print('NESTA RODADA', lista[ultimo - 1], 'NÃO JOGOU')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[ultimo - 2],resultado1, ' x ',resultado2, lista[x])
                ultimo = ultimo - 1


        else:
            lista = trocar(lista)
            print('\n', cont + i + 2, ' RODADA\n')
            print('NESTA RODADA', lista[ultimo - 1], 'NÃO JOGOU')
            for x in range(int(fim)):
                resultado1 = (randint(0, 5))
                resultado2 = (randint(0, 5))
                print(lista[ultimo - 2], resultado1, ' x ', resultado2, lista[x])
                ultimo = ultimo - 1


print('VITÓRIAS',vitorias)
print('EMPATES',empate)
print('DERROTAS',derrotas)
print('GOLS PRÓ',golspro)
print('GOLS CONTRA',golscontra)

for time in pontos.keys():
    pontos[time]= vitorias[time]*3 + empate[time]
print('PONTOS',pontos)

#ordem=list(pontos.values())
#ordem.sort()                                   ordena itens no dicionario
#print(ordem)
#for valor in sorted(pontos):
 #   print(valor,'=',pontos[valor])
pontos2=pontos.copy()
print ('O',(max (pontos,key=pontos.get)),'FOI CAMPEÃO COM',max(pontos.values()),'PONTOS')
for cada in range(len(pontos)):
    listaderesultado.append(max(pontos2, key=pontos.get))
    deletar = listaderesultado[cada]
    del pontos2[(deletar)]

print('a classificaçao ficou assim',listaderesultado)
print(pontos)
final=len(listaderesultado)

#                                       calculnado saldo de gol
for cada in pontos:
    saldodegols[(cada)]=golspro[(cada)]-golscontra[(cada)]
print('SALDO=',saldodegols)

for contador in range(final-1):
    if(pontos[(listaderesultado[contador])] == pontos[(listaderesultado[contador+1])]):
        if (vitorias[(listaderesultado[contador])]<vitorias[(listaderesultado[contador+1])]):
            variavel=listaderesultado[contador]
            listaderesultado[contador]=listaderesultado[contador+1]
            listaderesultado[contador+1]=variavel

print(listaderesultado)







