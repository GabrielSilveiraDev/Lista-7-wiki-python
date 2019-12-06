#Lista 7 wiki python
#Exercício 1:


def verificador(ipTest):

    if len(ipTest) != 4:

        return False

    for i in range (3):
        if 0 >= int(ipTest[i]) or int(ipTest[i]) >= 255:

            return False

    else:
        return True


validos = ['Endereços válidos: ']
invalidos = ['Endereços inválidos: ']
ips = []

f = open('IPs python 7.txt','r')

for line in f:
    ip = verificador(line.strip().split('.'))
    if ip:
        validos.append(line.strip())

    elif not ip:
        invalidos.append(line.strip())

f.close()

file = open('SaidaIPs','w')

for i in validos:
    file.write(f'{i}\n')

for i in invalidos:
    file.write(f'\n{i}')

file.close()

""

#Exercicio 2:

f = open('usuarios.txt','r')

listaUsuario = []
listaConsumo = []
listaDados = []
listaPorcentagem = []
total = 0

for line in f:

    listaDados.append(line.strip().split('       '))

f.close()

for i in range(len(listaDados)):

    listaConsumo.append(listaDados[i][1])

    total += int(listaDados[i][1])

    listaUsuario.append(listaDados[i][0])

for i in range(len(listaConsumo)):

    porcentagem = (100*int(listaConsumo[i]))/total
    listaPorcentagem.append(porcentagem)
    listaConsumo[i] = int(listaConsumo[i])/1048576

arquivo = open('Relatório.txt', 'w')

arquivo.write('Nr.  Usuário         Espaço utilizado       % do uso')
arquivo.write('\n')

for i in range (len(listaConsumo)):

    arquivo.write(f'{i+1}   {listaUsuario[i]}         {round(listaConsumo[i],2)} MB           {(round(listaPorcentagem[i],2))}%\n')

arquivo.write('\n')
arquivo.write(f'Espaço total ocupado: {round(sum(listaConsumo),2)} MB\nEspaço médio ocupado: {round(sum(listaConsumo)/len(listaConsumo),2)} MB')

arquivo.close()

""