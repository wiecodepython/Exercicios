"""
Cap 11 - Dicionarios
1. Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está
usando como valor.
"""
pessoas = {
    'Pedro': 'Azul',
    'Miguel': 'Amarelo',
    'Claudia': 'Verde',
    'Marta': 'Verde',
    'Alexandre': 'Azul Claro'
}

print('EXERCICIO 5')
print('q1.')
print(f'Dicionario pessoas = {pessoas}')

"""
2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como
seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem
aula?).
"""
semana = {}
semana.update(segunda=['OEM para análise de sistemas',
                       'Sociologia aplicada a informatica'])
semana.update(terca=['Computacao grafica', 'Sistemas distribuidos'])
semana.update(quarta=['OEM para análise de sistemas'])
semana.update(quinta=['Computacao grafica', 'Sistemas distribuidos'])
semana.update(sexta=['Desenvolvimento Web em Python', 'Java avancado'])
semana.update(sabado=[])
semana.update(domingo=[])

print('\nq2.')
print(f'Dicionario semana = {semana}')

"""
3. Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro
dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes.
"""
filmes = {}
filmes['O silencio dos inocentes'] = {
    'vilao': 'Hannibal Lecter',
    'ano': '1991'
}
filmes['Psicose'] = {
    'vilao': 'Norman Bates',
    'ano': '1960'
}
filmes['Gladiador'] = {
    'vilao': 'Lucius Aurelius Commodus',
    'ano': '2000'
}
filmes['Hellraiser'] = {
    'vilao': 'Pinhead',
    'ano': '1987'
}
filmes['Senhor dos Aneis: A sociedade do anel'] = {
    'vilao': 'Sauron',
    'ano': '2001'
}

print('\nq3.')
# Me recuso a colocar alguns como vilões, tipo Darth Vader ou Coringa...:)
print(f'Dicionario filmes = {filmes}')
