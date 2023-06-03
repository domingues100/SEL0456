#Gabriel Montagni Domingues Filho - 11800903

#listas sendo usadas
list_fib = []
list_fat = []

#receber o arquivo e ler as entradas
with open("input.dat") as input: linhas = input.read()

#for com a lógica
for i in range(len(linhas)) :
    if linhas[i] == ',' or linhas[i] == ' ' :  #achar a virgula ou o espaço
        list_fib.append(linhas[i-1])          #adiciona o que vai ser utilizado no fibonacci
        list_fat.append(linhas[i+1])         #adiciona o que vai ser utilizado como fatorial

#funções para fazer o fib e fat
fib = lambda x: fib(x-1) + fib(x-2 ) if x >= 2 else 1  #funcional do fib, com as devidas condições
fat = lambda y: y * fat(y-1) if y >= 2 else 1


#saída desejada no formato Linha n: Fib(x)=X Fact(y)=Y
with open("output.dat",'w') as output:
    for i in range (len(list_fat)):
        output.write(f"Linha {i+1}: Fib({list_fib[i]})={fib(int(list_fib[i]))} Fat({list_fat[i]}) ={fat(int(list_fat[i]))}\n")





