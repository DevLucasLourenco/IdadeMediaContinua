marker = 0
continuar = ''
nome_familiares = []
idade_familiares = []

while continuar != 'n':

    nome_familiares.append(input(f'Insira o nome do {marker + 1}º familiar').strip().title())
    idade_familiares.append(int(input(f'Insira a idade de {nome_familiares[marker]}')))
    qtde_familiares = [len(nome_familiares)]
    marker += 1
    continuar = input('Pressione <Enter> para continuar, "n" para parar').strip().lower()

familia = dict(zip(nome_familiares, idade_familiares))

print(f'{"Detalhes da Família":^23}')
print('='*23)
for nome, idade in familia.items():
    print(f'|{nome:^10}|{idade:^6}anos|')
print('='*23)

idade_media_familiar = round(sum(idade_familiares) / len(idade_familiares))
print(f'Idade Média:{idade_media_familiar:^11}')