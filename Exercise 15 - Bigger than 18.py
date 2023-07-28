#Exercício 15:
#Elabore um programa que recebe a idade de 10 pessoas e
#que imprima quantas pessoas tem idade superior a 18

contar_18=0
for contador in range (0,10,+1):
    idade=int(input("introduza a idade"))
    if idade>18:
        contar_18 = contar_18+1

print("existe", contar_18, "pessoas acima de 18")

    


