import json
import os
from time import sleep


#arquivo = os.path.join(os.path.dirname(__file__),'restaurantes.json')

#Definindo as funções
def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo) 
    return dados
     
def menu_Inicial():
    print('|  Bem vindo ao Super CRUD 🦸🏽‍♂️  |')
    print('1. Modo Supervisor') 
    print('2. Modo Cliente')
    print('3. Sair do sistema')

def limpa():
    os.system('cls')




#Funções do Cliente
def menu_cliente():
    print('|   Menu Cliente   |')
    print('1. Pesquise o Restaurante')
    print('2. Visualize sua reserva')
    print('3. Voltar')

def escolha_restaurante():
    limpa()
    print('Escolha o restaurante')
    lista_de_restaurantes()
    resposta = int(input('\n'))
    limpa()
    restaurante = ler_arquivo_json('restaurantes.json')
    print(f"{restaurante[resposta-1]['nome']}")
    print(f"Cozinha: {restaurante[resposta-1]['cozinha']}")
    print(f"Horário de Funcionamento: {restaurante[resposta-1]['funcionamento']}\n")
    print('1. Fazer Cadastro')
    print('2. Voltar')
    return resposta

def lista_de_restaurantes():
    restaurantes = ler_arquivo_json('restaurantes.json')
    print("|  Restaurantes  |")
    for indice, restaurante in enumerate(restaurantes, start=1):
        print (f"{indice}. {restaurante['nome']}")

def fazer_cadastro(restauranteCad, nomeReserva, data, horario, quantPessoas, CPF):
    reserva = ler_arquivo_json('reservas.json')

    reserva.append({'restauranteCad': restauranteCad, 'nomeReserva': nomeReserva, 'data': data, 'horario': horario, 'quantPessoas': quantPessoas, 'CPF': CPF})

    with open('reservas.json', 'w') as arquivo:
        json.dump(reserva, arquivo, indent=4)
    print("\n😎 USUÁRIO ADICIONADO COM SUCESSO!")
    sleep(2)
    limpa()

def mudar_dados(CPF, dadoNovo, tipoDado):
    reservas = ler_arquivo_json('reservas.json')
    
    for reserva in reservas:
        if reserva['CPF'] == CPF:
            reserva[tipoDado] = dadoNovo
    
    with open('reservas.json', 'w') as arquivo:
        json.dump(reservas, arquivo, indent=4)

def atualizar_reserva(dados):
    while True:
        limpa()
        print(f'1. Reserva no CPF {dados["CPF"]}')
        print(f'2. Restaurante: {dados["restauranteCad"]}')
        print(f'3. Nome da Reserva: {dados["nomeReserva"]}')
        print(f'4. Data: {dados["data"]}')
        print(f'5. Quantidade de Pessoas: {dados["quantPessoas"]}')
        print(f'6. Horário: {dados["horario"]}')
        print('\n7. Encerrar atualização')
        
        resposta2 = int(input('Qual dado você deseja atualizar?\n'))

        match resposta2:
            case 1:
                novoCPF = input('Digite o novo CPF\n')
                mudar_dados(dados["CPF"], novoCPF, 'CPF')
                dados["CPF"] = novoCPF

            case 2:
                novoRestauranteCad = input('Digite o novo Restaurante\n')
                dados["restauranteCad"] = novoRestauranteCad
                mudar_dados(dados["CPF"], novoRestauranteCad, 'restauranteCad')

            case 3:
                novoNomeReserva = input('Digite o novo Nome\n')
                dados["nomeReserva"] = novoNomeReserva
                mudar_dados(dados["CPF"], novoNomeReserva, 'nomeReserva')

            case 4:
                novoData = input('Digite a nova data\n')
                dados["data"] = novoData
                mudar_dados(dados["CPF"], novoData, 'data')

            case 5:
                novoQuantPessoas = input('Digite a nova quantidade de pesssoas\n')
                dados["quantPessoas"] = novoQuantPessoas
                mudar_dados(dados["CPF"], novoQuantPessoas, 'quantPessoas')

            case 6:
                novoHorario = input('Digite o novo horário\n')
                dados["horario"] = novoHorario
                mudar_dados(dados["CPF"], novoHorario, 'horario')

            case 7:
                print('😙 Dados Atualizados com SUCESSO!!')
                sleep(1)
                limpa()
                break

def pesquisar_restaurante():
    restaurante = ler_arquivo_json('restaurantes.json')
    resposta = escolha_restaurante()
    resposta2 = int(input(''))
    limpa()

    if resposta2 == 1:
        restauranteCad = restaurante[resposta-1]['nome']
        print(f'Reserva no {restaurante[resposta-1]['nome']}\n')
        nomeReserva = input('Digite seu nome:\n')
        CPF = input('Digite seu CPF:\n')
        data = input('Data:\n')
        horario = input('Horário:\n')
        quantPessoas = input('Quantidade de Pessoas:\n')
        fazer_cadastro(restauranteCad, nomeReserva, data, horario, quantPessoas, CPF)

    elif resposta2 == 2:
        pesquisar_restaurante()        

def buscar_reserva(CPF):
    reservas = ler_arquivo_json('reservas.json')
    for reserva in reservas:
        if reserva['CPF'] == CPF:
            return reserva
    return None

def deletar_reserva(CPF):
    reservas = ler_arquivo_json('reservas.json')
    
    for reserva in reservas:
        if reserva['CPF'] == CPF:
            reservas.remove(reserva)
    
    with open('reservas.json', 'w') as arquivo:
        json.dump(reservas, arquivo, indent=4)

    print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")
    
def exibir_dados(dados):
    if dados:
        print(f'Reserva no CPF {dados["CPF"]}\n')
        print(f'Restaurante: {dados["restauranteCad"]}')
        print(f'Nome da Reserva: {dados["nomeReserva"]}')
        print(f'Data: {dados["data"]}')
        print(f'Horário: {dados["horario"]}')
        print(f'Quantidade de Pessoas: {dados["quantPessoas"]}')
        
        print('1. Atualizar')
        print('2. Deletar')
        print('3. voltar')

        resposta = int(input(''))
        if resposta == 1:
            atualizar_reserva(dados)
        elif resposta == 2:
            deletar_reserva(dados['CPF'])
            sleep(2)
            limpa()
        elif resposta == 3:
            limpa()
            visualizar_reserva()
    else:
        print("Código não encontrado.")
        sleep(2)
        limpa()
        visualizar_reserva()

def visualizar_reserva():

    CPF = input('Digite o CPF da reserva:\n')
    CPF_encontrado = buscar_reserva(CPF)
    exibir_dados(CPF_encontrado)   




#Funções do Supervisor
def menu_supervisor():
    print('|   Menu Supervisor   |')
    print('1. Lista de Restaurantes')
    print('2. Adicione Seu Restaurante')
    print('3. Visualize seu Restaurante')
    print('4. Voltar')




#Função principal que chama as outras funções
def main():
    
    while True:
        menu_Inicial()
        resposta_Inicial = int(input('Selecione o modo que deseja utilizar:\n'))
        match (resposta_Inicial):
            
            case 1:
                print ('Abrindo Sistema...')
                sleep(2)
                limpa()
                menu_supervisor()
                resposta1 = int(input('Escolha uma opção\n'))
                match resposta1:
                    case 1:
                        #Mostrar Lista dos Restaurantes
                        print('Em Desenvolvimento...')
                    case 2:
                        #Adicionar Seu Próprio Restaurante
                        print('Em Desenvolvimento...')
                    case 3:
                        #Vizualizar e modificar dados do Restaurante
                        print('Em Desenvolvimento...')
                    case 4:
                        print('Voltando...')
                        sleep
                        main()
                

            case 2: 
                print ('Abrindo Sistema...')
                sleep(2)
                limpa()
                menu_cliente()
                resposta = int(input('Escolha uma opção\n'))
                match (resposta):
                    
                    case 1:
                        pesquisar_restaurante()
                        main()

                    case 2:
                        limpa()
                        visualizar_reserva()
                        sleep(1)
                        main()

                    case 3:
                        print('Voltando...')
                        sleep
                        main()
                    

            case 3:
                print('Saindo...😁')
                sleep(3)
                break

            case __:
                print('Opção inválida 😑')
                sleep(1)
                main()

if __name__ == '__main__':
    main()

