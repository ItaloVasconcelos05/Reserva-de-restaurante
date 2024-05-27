import json
import os

#Código
def abrir_Restaurante():
     with open('restaurantes.json', 'r') as arquivo:
        restaurantes = json.load(arquivo) 
        return restaurantes
     
def menu_Inicial():
    print('|  Digite a opção desejada  |')
    print('1. Pesquise seu Restaurante')
    print('2. Mostrar Lista de Restaurante')
    print('3. Sair do Sistema')
    resposta = int(input('\n'))
    return resposta

def voltarAoMenu():
    resultado = input('\n Digite "b" para voltar ao Menu Inicial\n')
    if resultado.upper() == 'B':
        main()

def listaDeRestaurantes():
    restaurantes = abrir_Restaurante()
    print("|  Restaurantes  |")
    for indice, restaurante in enumerate(restaurantes, start=1):
        print (f"{indice}. {restaurante['nome']}")

def limpa():
    os. system('cls')

def main():
    limpa()
    resposta = menu_Inicial()
    limpa()

    match resposta:
        
        case 1: 
            print('Ainda em Desenvolvimento')
            
            limpa()

        case 2:
            restaurantes = abrir_Restaurante()
            listaDeRestaurantes()
            info = int(input('Digite o número do restaurante para saber mais\n'))
            limpa()
            match info:
                case 1:
                    print(f"{restaurantes[info-1]['nome']}")
                    print(f"Culinária: {restaurantes[info-1]['cozinha']}")
                    print(f"Horário de Funcionamento: {restaurantes[info-1]['funcionamento']}")
        case 3:
            print('Saindo...')

if __name__ == '__main__':
    main()

