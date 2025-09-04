print('Estrutura de Dados e Algoritmos - Python ')

#Listas (Arrays)
#encontrar o maior número em uma lista
numeros = [3, 5, 2, 8, 1]
maior = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
        
print(f'O maior número é: {maior}')