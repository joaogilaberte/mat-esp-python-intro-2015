import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# lista original fora de ordem
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
plt.figure()
plt.plot(range(0, 20, 1), lista, "ok") 
plt.title("Grafico Original")
plt.xlabel("x eh indice")
plt.ylabel("y eh lista original")
plt.savefig("bubble-inicio.png")
# definir o nome da lista, para a mesma ser identificada
print('lista original', lista)
n = 20 #temos 20 elementos
for i in range (0, n-1, 1): #valores que i podem assumir
    for j in range (i+1, n, 1): #valores que j podem assumir
        if lista[i] < lista[j]: #quando i for menor que j mantem
            continue
        else:
            temp = lista[i]  #quando j for menor que i, troca
            lista[i] = lista[j]
            lista[j] = temp
print ('lista crescente', lista) #escrever na tela lista crescente e a nova ordem dos dados
print ('lista dos cinco maiores', lista[15:21:1]) #aparecer na tela a frase lista com os cinco valores maiores, e depois os ultimos cinco da lista ordem crescente 
print ('lista dos cinco menores', lista[0:5:1]) ##aparecer na tela a frase lista com os cinco valores maiores, e depois os primeiros cinco da lista ordem crescente







 


            
            
            
            

            
            

    
 
