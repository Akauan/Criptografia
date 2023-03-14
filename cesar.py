def versao():
    return 1.0

def cesar(plaintext_or_encriptex_text, int_key, encript_1_or_decript_0):
    #Modo de cifrar
    _cript = 1
    
    #Modo de descifrar
    _decript = 0
    
    #Palavra de entrada, texto plano ou encriptado
    _palavra = plaintext_or_encriptex_text
    
    #Chave usada para cifrar ou descifrar
    _chave = int_key
    
    #Define o tipo da função
    _tipo = encript_1_or_decript_0
    
    #String com todos os caracteres
    _tudo = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ0123456789.,;;~^[]{}!?@#$%¨&*()-_=+/\|'
    
    #Palavra que será retornada
    nova_palavra = ''
    
    #Verifica se a chave é inteiro
    if _chave.isdigit():
        _chave = int(_chave)
    else:
        return 'Chave inválida, tente novamente com uma chave do tipo int.'
    
    #Entra na palavra de entrada
    for c in _palavra:
        
        #Acha o index da letra atual
        _index = _tudo.find(c)
        
        #Se o não achar, ele só adiciona na nova palavra
        if _index == -1:
            nova_palavra += c
            
        #Se achar ele trata
        else:
            
            #Se o tipo for cifrar, ele faz a cifra conforme a chave
            if _tipo == _cript:
                 _novo_index = _index + _chave
                 _novo_index = _novo_index % len(_tudo)
                 nova_palavra += _tudo[_novo_index:_novo_index+1]
            
            #Se o tipo for decifrar, ele descifra conforme a chave 
            elif _tipo == _decript:
                _novo_index = _index - _chave
                _novo_index = _novo_index % len(_tudo)
                nova_palavra += _tudo[_novo_index:_novo_index+1]
        
      
    return nova_palavra
