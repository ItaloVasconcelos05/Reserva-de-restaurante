import json
import os
from time import sleep


#arquivo = os.path.join(os.path.dirname(__file__),'restaurantes.json')

#Código de abertura 
def abrir_Restaurante():
     with open('restaurantes.json', 'r') as arquivo:
        restaurantes = json.load(arquivo) 
        return restaurantes

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

def pesquisar_Restaurante(nome):
    with open('restaurantes.json','r') as arquivo:
       restaurantes = json.load(arquivo)  
    encontrado = False

    for procurar_nome in restaurantes:
       if procurar_nome['nome'] == nome:
            print(f"Nome do restaurante:{procurar_nome['nome']}, \nCozinha:{procurar_nome['cozinha']}, \nFuncionamento:{procurar_nome['funcionamento']}")
            encontrado = True
    if not encontrado:
            print ('Usuário não cadastrado.')    

def listaDeRestaurantes():
    restaurantes = abrir_Restaurante()
    print("|  Restaurantes  |")
    for indice, restaurante in enumerate(restaurantes, start=1):
        print (f"{indice}. {restaurante['nome']}")

def fazerCadastro(restauranteCad, nomeReserva, data, horario, quantPessoas):
    with open('reserva.json', 'r') as arquivo:
        reserva = json.load(arquivo)

    reserva.append({'restauranteCad': restauranteCad, 'nomeReserva': nomeReserva, 'data': data, 'horario': horario, 'quantPessoas': quantPessoas})

    with open('reserva.json', 'w') as arquivo:
        json.dump(reserva, arquivo, indent=4)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def

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
                        resposta2 = int(input(''))
                        limpa()
                        if resposta2 == 1:
                            restauranteCad = restaurante[resposta-1]['nome']
                            nomeReserva = input('Digite seu nome').upper
                            data = input('Data')
                            horario = input('Horário')
                            quantPessoas = input('Quantidade de Pessoas')
                            fazerCadastro(restauranteCad, nomeReserva, data, horario, quantPessoas)

            
            case 3:
                print('Saindo...😁')
                sleep(3)
                break
            case __:
                print('Opção inválida 😑')

if __name__ == '__main__':
    main()

