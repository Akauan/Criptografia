#Cifra de transposição

#        =======        =====     =====        =======        =======   =======        =======        =======      =====   #
#       ==== ====       =====    =====        ==== ====        =====     =====        ==== ====       ========     =====   #
#      ====   ====      =====   =====        ====   ====       =====     =====       ====   ====      =========    =====   #
#     ====     ====     ====== =====        ====     ====     =====       =====     ====     ====     ==========   =====   #
#    ===============    ===========        ===============    =====       =====    ===============    ===== =====  =====   #
#   =================   ====== =====      =================   =====       =====   =================   =====  ===== =====   #
#   =====       =====   =====  =====      =====       =====   =====       =====   =====       =====   =====   ==========   #
#   =====       =====   =====   =====     =====       =====   =====       =====   =====       =====   =====    =========   #
#   ====         ====   =====    =====    ====         ====    ===============    ====         ====   =====     ========   #
#   ====         ====   =====     =====   ====         ====     =============     ====         ====   =====      =======   #

def versao():
    return 1.0

def cript(string_plaintext,string_key):
    _frase = string_plaintext.replace(' ','')
    _chave = string_key
    _listaChave = sorted(list(_chave))
    _cifrado = ''
    _separado = []

    _contador = 0

    #Verifica se a frase é do tamanho certo
    while len(_frase) % len(_chave) != 0:
            
        #Transforma do tamanho certo
        _frase += ' '
            
        
    
    #Quebra a frase em listas
    for l in range(int(len(_frase)/len(_chave))):
        #Lista temporaria
        _temp = []

        #Coloca os valores na lista temporaria
        for c in range(len(_chave)):
            _temp.append(_frase[_contador])

            #Aumenta 1 no contador
            _contador += 1

        #Adiciona a lista temporaria na lista separada
        _separado.append(_temp)

    #Cifra
    for l in range(len(_chave)):
        for c in _separado:
            _cifrado += c[_chave.index(_listaChave[l])]

    
    return(_cifrado)

def decript(string_encripted_plaintext,string_key):
    _frase = string_encripted_plaintext
    _chave = string_key
    _listaChave = sorted(list(_chave))
    _separado = []
    _organizado = []
    _contador = 0
    _decifrado = ''

    #Verifica se a frase é do tamanho certo
    while len(_frase) % len(_chave) != 0:
            
        #Transforma do tamanho certo
        _frase += ' '
            
      

    #Quebra a frase em listas
    for c in range(len(_chave)):
        #Lista temporaria
        _temp = []

        #Coloca os valores na lista temporaria
        for l in range(int(len(_frase)/len(_chave))):
            _temp.append(_frase[_contador])

            #Aumenta 1 no contador
            _contador += 1

        #Adiciona a lista temporaria na lista separada
        _separado.append(_temp)

    #For para organizar a lista
    for o in _chave:
        
        #Lista temporária
        _temp = []

        #Organiza a lista
        _organizado.append(_separado[_listaChave.index(o)])

    #For para decifrar a frase organizada, colocando todas as letras em sequencia.
    for l in range(int(len(_frase)/len(_chave))):
        
        for c in _organizado:
            
            _decifrado += c[l]

    return _decifrado

     
if __name__ == '__main__':

    key = '987654321'
    cfrase = 'eu sou foda'
    dfrase = 'atp dia ousifmseuaevotmaslorurbrekoo'
    

    print(decript(dfrase,key))
