from statistics import geometric_mean, harmonic_mean, fmean
from operator import mul
from functools import reduce
print('VARIAVEIS')
"""
1 - Supondo que a cotação do dólar esteja em R$ 3,25,
salve esse valor em uma variável e utilize-o para
calcular quanto você teria ao cambiar R$65,00 para
dólares.
"""
valor = 65.0  # em reais
cotacao = 3.25  # em reais


def dolar_to_brl(valor: float, cotacao: float) -> float:
    return valor*cotacao


print('q1')
print(f'R${valor:.2f} equivale a U${(dolar_to_brl(valor, cotacao)):.2f} na cotação de R${cotacao:.2f}')

"""
2 - Abelindo é um professor muito malvado. Ele quer
decidir como reprovar Rondinelly, que tirou 8.66, 5.35,
5 e 1, respectivamente, nas provas P1, P2, P3 e P4. 
Para isso, ele pode calcular a nota final usando 
média aritmética (M.A.), média geométrica (M.G.) ou 
média harmônica (M.H.).

MA = (P1 + P2 + P3 + P4)/4
MG = (|P1*P2*P3*P4|)**(1/4)
MH = 4/(1/P1 + 1/P2 + 1/P3 + 1/P4)
"""
lista = [8.66, 5.35, 5, 1]


def media_aritmetica(lista: list) -> float:
    return sum(lista)/len(lista)


def media_geometrica(lista: list) -> float:
    # return pow(reduce(lambda x,y: x*y, lista), 1/len(lista))
    return pow(reduce(mul, lista), (1/len(lista)))


def media_harmonica(lista: list) -> float:
    return len(lista)/sum(1/x for x in lista)


ma = media_aritmetica(lista)
mg = media_geometrica(lista)
mh = media_harmonica(lista)

mas = fmean(lista)
mgs = geometric_mean(lista)
mhs = harmonic_mean(lista)

result = {
    ma: 'Média Aritmética',
    mg: 'Média Geométrica',
    mh: 'Média Harmônica'
}

res_statst = {
    mas: 'Média Aritmética',
    mgs: 'Média Geométrica',
    mhs: 'Média Harmônica'
}


def print_dict(dicionario: dict) -> None:
    for k, v in list(dicionario.items()):
        print(f'{v} = {k}')


print('\nq2')
print('Na unha'.upper())
print_dict(result)
print('Usando biblioteca statistics'.upper())
print_dict(res_statst)
print(f'\n{result.get(max(result))} dá a maior nota e a {result.get(min(result))} a pior nota.')

"""
3 - Josefson deseja fazer compras na China. Ela quer 
comprar um celular de USD 299,99, uma chaleira de 
USD 23,87, um gnomo de jardim de USD 66,66 e 6 
adesivos de unicórnio de USD 1,42 cada um. O frete de 
tudo isso para a cidade de Rolândia, no Paraná, ficou 
em USD 12,34.
a. Calcule o valor total da compra em dólares.
b. Usando o mesmo valor do dólar do exercício anterior,
calcule o preço final em Reais. Lembre-se que o valor do IOF
é de 6,38 %.
c. Quanto ela pagou apenas de IOF?

"""

valor_celular = 299.99
valor_chaleira = 23.87
valor_gnomo = 66.66
valor_adesivo = 1.42
valor_frete = 12.34

total = (valor_celular +
         valor_chaleira +
         valor_gnomo +
         6*valor_adesivo +
         valor_frete)

iof = total*6.38/100

print('\nq3')
print('a.')
print(f'Valor total da compra = U${total:.2f}')
print('b.')
print(f'Preço final = R${dolar_to_brl(total+iof, cotacao):.2f}')
print('c.')
print(f'Valor do IOF = R${dolar_to_brl(iof,cotacao):.2f}')

print('\nSTRINGS')
print('q1.')
"""
1 - Dada a frase Python é muito legal., use fatiamento para dar nome
às variáveis contendo cada palavra. 
"""
frase = 'Python é muito legal.'
print('Frase =', frase)

palavra1 = frase[:6]
palavra2 = frase[7]
palavra3 = frase[9:14]
palavra4 = frase[15:-1]


palavras = {
    'palavra 1': palavra1,
    'palavra 2': palavra2,
    'palavra 3': palavra3,
    'palavra 4': palavra4
}

print('PALAVRAS')
for k, v in palavras.items():
    print(f'{k} = {v}')

"""
2 - Qual o tamanho dessa frase? E qual o tamanho de cada palavra?
"""
print('\nq2.')
print(f'Tamanho da frase({frase}) = {len(frase)}')
for k, v in palavras.items():
    print(f'Tamanho da {k}({v}) = {len(v)}')


"""
3 - Use slicing (mais especificamente o passo do fatiamento) para
inverter a string «Python»
"""
print('\nq3.')
palavra = 'Python'
print(f'Palavra: {palavra}, palavra invertida: {palavra[::-1]}')


print('\nLEITURA DO TECLADO')
print('q1.')
"""
1 - Leia um nome pelo teclado e imprima "Olá, <seu nome>!"
"""
nome = input('Informe um nome: ')
print(f'Olá, {nome}!')

"""
2 - Leia outro nome pelo teclado e imprima:
<nome lido> roubou o pão na casa do <nome lido 2>!
<nome lido 2> ficou triste e com fome,
porque o bandeijão estava fechado.
"""
print('\nq2.')
nome2 = input('Informe outro nome: ')

print(f'{nome} roubou o pão na casa de {nome2}!')
print(f'{nome2} ficou triste e com fome,\nporque o bandeijão estava fechado.')


"""
3 - Leia uma frase pelo teclado e a imprima ao contrário. Por
exemplo, se a frase for ​"Manjo muito de Python!​", a saída deverá
ser ' ​ !nohtyP ed otium ojnaM'​.
"""
print('\nq3.')
frase_lida = input('Digite uma frase: ')
print(f'frase ao contrário: {frase_lida[::-1]}')
