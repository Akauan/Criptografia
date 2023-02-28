from os import system,name
from urllib import request

#Lista com o nome e endereço dos arquivos
arquivos = {'cesar.py' : 'https://raw.githubusercontent.com/Akauan/Criptografia/2f5db0709d863fba68f9368dc8ab81b067224d3f/cesar.py',
            'transposicao.py' : 'https://raw.githubusercontent.com/Akauan/Criptografia/2f5db0709d863fba68f9368dc8ab81b067224d3f/transposicao.py'}

#For para baixar os aquivos
for item in arquivos.keys():
    file = item
    file_url = arquivos[item]
    request.urlretrieve(file_url,file)

from cesar import cesar
import transposicao

#Função que limpa a tela
def apagar():
    return system('cls' if name == 'nt' else 'clear')

#Função do menu geral
def menuGeral():
    while True:
        apagar()
        print('''=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
            Akauan Cifras
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
1 - Cifra de Cesar
2 - Cifra de Transposição
8 - Ajuda
0 - Sair''')
        case = input('> ')

        if case == '0':
            print('Até a próxima :)')
            exit()
            pass
        
        elif case == '1':
            apagar()
            menuCesar()
            
            pass

        elif case == '2':
            apagar()
            menuTransposicao()
            
            pass

        elif case == '8':
            apagar()
            print('''=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
              Akauan Cifras
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
             | Ajuda Geral|
1.Cifra de Cesar: 
    É um tipo de cifra de substituição
na qual cada letra do texto é substituída
por outra, que se apresenta no alfabeto
abaixo dela um número fixo de vezes.

2.Cifra de Transposição: 
    Uma cifra de transposição é aquela
que, ao contrário da cifra vista anterior-
mente, não substitui nenhum caractere da
mensagem original, apenas “rearruma” esses
caracteres de acordo com algum sistema
específico, para que, qualquer um que
conheça esse sistema, possa ler a mensagem.

''')
            input('Aperte enter para continuar...')
            pass

#Função do menu de Cifra de Cesar
def menuCesar():
    numc = []
    while True:
        apagar()
        print('''=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
        Menu Cifra de Cesar
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
1 - Cifrar
2 - Descifrar
3 - Descifrar cifra anterior
8 - Ajuda
9 - Voltar
0 - Sair''')
        case = input('> ')

        if case == '0':
            print('Até a próxima :)')
            exit()

        elif case == '1':
            print('Digite a frase que deseja cifrar:')
            frase = input('> ')
            print('Digite o NÚMERO da chave:')
            chave = input('> ')
            cifrado = cesar(frase,chave,1)
            print(f'Palavra Cifrada: {cifrado}')
            print()
            input('Aperte enter para continuar...')

            
        elif case == '2':
            print('Digite a frase que deseja descifrar:')
            frase = input('> ')
            print('Digite o NÚMERO da chave:')
            chave = input('> ')
            print(f'Palavra Cifrada: {cesar(frase,chave,0)}')
            print()
            input('Aperte enter para continuar...')
            pass
        
        elif case == '3':
            if 'chave' in locals():
                print(f'Descifrando a cifra anterior : {cifrado}...')
                print(f'Palavra Descifrada: {cesar(cifrado,chave,0)}')
                print()
                input('Aperte enter para continuar...')
            else:
                print('NÃO TEM NENHUMA CIFRA GUARDADA.')
                print()
                input('Aperte enter para continuar...')

        elif case == '8':
            print('''=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
              Akauan Cifras
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
             | Cesar Ajuda |
1.Cifrar: 
    Você vai dizer qual o texto plano 
(String) que será cifrado, e após isso 
dirá qual a chave (int) que será usada 
para cifrar o texto.

2.Descifrar: 
    Você irá informar o texto cifrado 
(String) que deseja descifar e logo em 
seguida dirá qual a chave (int) que foi 
usada para fazer essa cifra.

3.Descifrar cifra anterior:
    Essa opção descifra a ultima frase 
cifrada, ou seja, ela pega a chave e a 
palavra cifrada anterior e mostra a 
palavra descifrada correspondente. 
Nota: Se não houver uma cifra anterior 
ele apenas cancela a operação.
                  ''')
            input('Aperte enter para continuar...')

        elif case == '9':
            break

#Função do menu de Cifra de transposição
def menuTransposicao():
    while True:
        apagar()
        print('''=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
      Menu Cifra de Transposição
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
1 - Cifrar
2 - Descifrar
8 - Ajuda
9 - Voltar
0 - Sair''')
        case = input('> ')

        if case == '0':
            print('Até a próxima :)')
            exit()

        elif case == '1':
            print('Digite a frase que deseja cifrar:')
            frase = input('> ')
            print('Digite a chave:')
            chave = input('> ')
            print(f'Palavra Cifrada: {transposicao.cript(frase,chave)}')
            print()
            input('Aperte enter para continuar...')

        elif case == '2':
                print('Digite a frase que deseja descifrar:')
                frase = input('> ')
                print('Digite a chave:')
                chave = input('> ')
                print(f'Palavra Descifrada: {transposicao.decript(frase,chave)}')
                print()
                input('Aperte enter para continuar...')
            
        elif case == '8':
            print('''=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
              Akauan Cifras
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
         | Tramsposição Ajuda |
1.Cifrar: 
    Você vai dizer qual o texto plano 
(String) que será cifrado, e após isso 
dirá qual a chave (int ou String) que será usada 
para cifrar o texto.

2.Descifrar: 
    Você irá informar o texto cifrado 
(String) que deseja descifar e logo em 
seguida dirá qual a chave (int ou String) que foi 
usada para fazer essa cifra.
                  ''')
            input('Aperte enter para continuar...')
            pass

        elif case == '9':
            break

if __name__ == '__main__':
    menuGeral()
