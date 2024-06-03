import json
import os
from time import sleep


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


def fazer_cadastro_reserva(restauranteCad, nomeReserva, data, horario, quantPessoas, CPF):
    reserva = ler_arquivo_json('reservas.json')

    reserva.append({'restauranteCad': restauranteCad, 'nomeReserva': nomeReserva, 'data': data, 'horario': horario, 'quantPessoas': quantPessoas, 'CPF': CPF})

    with open('reservas.json', 'w') as arquivo:
        json.dump(reserva, arquivo, indent=4)
    print("\n😎 USUÁRIO ADICIONADO COM SUCESSO!")
    sleep(2)
    limpa()


def mudar_dados_reserva(CPF, dadoNovo, tipoDado):
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
                mudar_dados_reserva(dados["CPF"], novoCPF, 'CPF')
                dados["CPF"] = novoCPF

            case 2:
                novoRestauranteCad = input('Digite o novo Restaurante\n')
                dados["restauranteCad"] = novoRestauranteCad
                mudar_dados_reserva(dados["CPF"], novoRestauranteCad, 'restauranteCad')

            case 3:
                novoNomeReserva = input('Digite o novo Nome\n')
                dados["nomeReserva"] = novoNomeReserva
                mudar_dados_reserva(dados["CPF"], novoNomeReserva, 'nomeReserva')

            case 4:
                novoData = input('Digite a nova data\n')
                dados["data"] = novoData
                mudar_dados_reserva(dados["CPF"], novoData, 'data')

            case 5:
                novoQuantPessoas = input('Digite a nova quantidade de pesssoas\n')
                dados["quantPessoas"] = novoQuantPessoas
                mudar_dados_reserva(dados["CPF"], novoQuantPessoas, 'quantPessoas')

            case 6:
                novoHorario = input('Digite o novo horário\n')
                dados["horario"] = novoHorario
                mudar_dados_reserva(dados["CPF"], novoHorario, 'horario')

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
        fazer_cadastro_reserva(restauranteCad, nomeReserva, data, horario, quantPessoas, CPF)

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

    print("😡 RESERVA EXCLUÍDO COM SUCESSO!")
    
    
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







def menu_supervisor():
    print('|   Menu Supervisor   |')
    print('1. Visualize os Restaurantes')
    print('2. Adicione Seu Restaurante')
    print('3. Atualize seu Restaurante')
    print('4. Deletar Restaurante')
    print('5. Voltar')

def fazer_cadastro_restaurante(nome,cozinha,funcionamento):
    restaurante = ler_arquivo_json('restaurantes.json')

    restaurante.append({'nome': nome, 'cozinha': cozinha, 'funcionamento': funcionamento})

    with open('restaurantes.json', 'w') as arquivo:
        json.dump(restaurante, arquivo, indent=4)
    print("\n😎 RESTAURANTE ADICIONADO COM SUCESSO!")
    sleep(2)
    limpa()
    
def deletar_restaurante(nome):
    restaurantes = ler_arquivo_json('restaurantes.json')
    
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            restaurantes.remove(restaurante)
            print("😡 RESTAURANTE EXCLUÍDO COM SUCESSO!")
        else: 
            print("Restaurante não encontrado")
            
    
    with open('restaurantes.json', 'w') as arquivo:
        json.dump(restaurantes, arquivo, indent=4)

    


def atualizar_restaurante(dados):
    while True:
        limpa()
        print(f'1. Nome do Restaurante: {dados["nome"]}')
        print(f'2. Tipo de Cozinha: {dados["cozinha"]}')
        print(f'3. Horario de Funcionamneto: {dados["funcionamento"]}')
        print('4. Sair')
        
        resposta2 = int(input('Qual dado você deseja atualizar?\n'))

        limpa()
        match resposta2:
            case 1:
                novoRestauranteCadastrado = input('Digite o novo nome do Restaurante:\n').upper()
                mudar_dados_restaurante(dados['nome'], novoRestauranteCadastrado, 'nome')
                dados['nome'] = novoRestauranteCadastrado
                
            case 2:
                novaCozinhaCadastrada = input('Digite a nova cozinha do Restaurante: \n')
                mudar_dados_restaurante(dados['nome'], novaCozinhaCadastrada, 'cozinha')
                dados['cozinha'] = novaCozinhaCadastrada
            
            case 3:
                novoFuncionamentoCadastrado = input('Digite o novo horário de funcionamento: \n')
                mudar_dados_restaurante(dados['nome'], novoFuncionamentoCadastrado, 'funcionamento')
                dados['funcionamento'] = novoFuncionamentoCadastrado   
            
            case 4:
                print('Alteração feita com sucesso!!')
                break
        
    print('Alteração feita com sucesso!!')        

def mudar_dados_restaurante(nome, dadoNovo, tipoDado):
    restaurantes = ler_arquivo_json('restaurantes.json')
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            restaurante[tipoDado] = dadoNovo
    
    with open('restaurantes.json', 'w') as arquivo:
        json.dump(restaurantes, arquivo, indent=4)

def buscar_restaurante(nomeRestaurante):
    restaurantes = ler_arquivo_json('restaurantes.json')
    for restaurante in restaurantes:
        if restaurante['nome'] == nomeRestaurante:
            return restaurante
    return None


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
                        lista_de_restaurantes()
                        input('\nAperte qualquer tecla para voltar:\n')
                        main()
                        
                    case 2:
                        nome = input('Digite o Nome do Restaurante:\n').upper()
                        cozinha = input('Digite o tipo de culinária:\n') 
                        funcionamento = input('Digite o horário de funcionamento do Restaurante:\n')
                        fazer_cadastro_restaurante(nome,cozinha,funcionamento)
                       
                    case 3:
                        nomePesquisar = input('Digite o nome do seu Restaurante:\n').upper()
                        restaurante_encontrado = buscar_restaurante(nomePesquisar)
                        atualizar_restaurante(restaurante_encontrado)
                        
                    case 4:
                        nomeRestaurante = input("Qual o restaurante que você quer deletar: \n").upper()
                        deletar_restaurante(nomeRestaurante)
                        input('\nAperte qualquer tecla para voltar:\n')
                        limpa()
                        main()
                    case 5:
                        print('Voltando...')
                        sleep(2)
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

