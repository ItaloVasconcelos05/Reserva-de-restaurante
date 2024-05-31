import json
import os
from time import sleep


#arquivo = os.path.join(os.path.dirname(__file__),'restaurantes.json')

#Código de abertura 
def abrir_Restaurante():
     with open('restaurantes.json', 'r') as arquivo:
        restaurantes = json.load(arquivo) 
        return restaurantes
     
def abrir_Reserva():
     with open('reserva.json', 'r') as arquivo:
        reservas = json.load(arquivo) 
        return reservas

def menu_Inicial():
    print('|  Bem vindo ao Super CRUD 🦸🏽‍♂️  |')
    print('1. Modo Supervisor') 
    print('2. Modo Cliente')
    print('3. Sair do sistema')
     
def menu_Cliente():
    print('|  Digite a opção desejada  |')
    print('1. Pesquise o Restaurante')
    print('2. Visualize sua reserva')
    print('3. Sair do Sistema')

def escolhaRestaurante():
    limpa()
    print('Escolha o restaurante')
    listaDeRestaurantes()
    resposta = int(input('\n'))
    limpa()
    restaurante = abrir_Restaurante()
    print(f"{restaurante[resposta-1]['nome']}")
    print(f"Cozinha: {restaurante[resposta-1]['cozinha']}")
    print(f"Horário de Funcionamento: {restaurante[resposta-1]['funcionamento']}\n")
    print('1. Fazer Cadastro')
    print('2. Voltar')
    return resposta

def listaDeRestaurantes():
    restaurantes = abrir_Restaurante()
    print("|  Restaurantes  |")
    for indice, restaurante in enumerate(restaurantes, start=1):
        print (f"{indice}. {restaurante['nome']}")

def listaDeReservas():
    reservas = abrir_Reserva()
    print("|  Reservas  |")
    for indice, reserva in enumerate(reservas, start=1):
        print (f"{indice}. {reserva['restauranteCad']}")

def fazerCadastro(restauranteCad, nomeReserva, data, horario, quantPessoas):
    with open('reserva.json', 'r') as arquivo:
        reserva = json.load(arquivo)

    reserva.append({'restauranteCad': restauranteCad, 'nomeReserva': nomeReserva, 'data': data, 'horario': horario, 'quantPessoas': quantPessoas})

    with open('reserva.json', 'w') as arquivo:
        json.dump(reserva, arquivo, indent=4)
    print("\n😎 USUÁRIO ADICIONADO COM SUCESSO!")
    sleep(2)
    limpa()
def atualizarReserva(restauranteAntigo,nomeAntigo,novoRestaurante,novoNome,novaData,novoHorario,novaQuantPessoas):
    with open('reserva.json', 'r') as arquivo:
        reserva = json.load(arquivo)
    
    for reservas in reserva:
        if reservas['restauranteCad'] == restauranteAntigo and reservas['nomeReserva'] == nomeAntigo:
           reservas['restauranteCad'] = novoRestaurante
           reservas['nomeReserva'] = novoNome
           reservas['data'] = novaData
           reservas['horario'] = novoHorario
           reservas['quantPessoas'] = novaQuantPessoas
           break
        else:
            print("Essa reserva não existe =(")
    with open('reserva.json', 'w') as arquivo:
        json.dump(reserva, arquivo, indent=4)
    print("😎 RESERVA ATUALIZADA COM SUCESSO!")

def pesquisaRestaurante():
    restaurante = abrir_Restaurante()
    resposta = escolhaRestaurante()
    resposta2 = int(input(''))
    limpa()

    if resposta2 == 1:
        restauranteCad = restaurante[resposta-1]['nome']
        nomeReserva = input('Digite seu nome:\n')
        data = input('Data:\n')
        horario = input('Horário:\n')
        quantPessoas = input('Quantidade de Pessoas:\n')
        fazerCadastro(restauranteCad, nomeReserva, data, horario, quantPessoas)

    elif resposta2 == 2:
        pesquisaRestaurante()

def limpa():
    os.system('cls')

#Função principal que chama as outras funções
def main():
    
    while True:
        menu_Inicial()
        resposta_Inicial = int(input('Selecione o modo que deseja utilizar:\n'))
        match (resposta_Inicial):
            
            case 1:
                print('Em manutenção...')
                break

            case 2: 
                print ('Abrindo Sistema...')
                sleep(2)
                limpa()
                menu_Cliente()
                resposta = int(input('Escolha uma opção\n'))
                match (resposta):
                    
                    case 1:
                        pesquisaRestaurante()
                        sleep(2)
                        main()

                    case 2:
                        limpa()
                        listaDeReservas()
                        resposta2 = int(input(''))
                        limpa()
                        print('1. Atualizar Reserva')
                        print('2. Voltar')
                        resposta4 = int(input(''))
                        limpa()
                        if resposta4 == 1:
                            limpa()
                            restauranteAntigo = input("Digite o nome do restaurante cadastrado:\n")
                            nomeReserva = input("Digite o nome da reserva cadastrada:\n")
                            novoRestaurante = input("Digite o novo restaurante da reserva:\n")
                            novoNome = input("Digite o novo nome da reserva:\n")
                            novaData = input("Digite a nova data da reserva:\n")
                            novoHorario = input("Digite o novo horário da reserva:\n")
                            novaQuantPessoas = input("Digite a nova quantidade de pessoas:\n")
                            atualizarReserva(restauranteAntigo,nomeReserva,novoRestaurante,novoNome,novaData,novoHorario,novaQuantPessoas)
                        
            case 3:
                print('Saindo...😁')
                sleep(3)
                break
            case __:
                print('Opção inválida 😑')

if __name__ == '__main__':
    main()

