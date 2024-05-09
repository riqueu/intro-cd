"""Módulo Criptográfico"""

DICIONARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?:;.,-_"

def encriptar(mensagem_clara, mensagem_cifrada, chave, metodo):
    if metodo == "cesar":
        for cada_linha in mensagem_clara:
            mensagem_cifrada.append(cifra_de_cesar(cada_linha, "encriptar", chave))
        return mensagem_cifrada

# DEVER DE CASA (decriptar cifra de cesar):
def decriptar(mensagem_cifrada, mensagem_decifrada, chave, metodo):
    pass

def cifra_de_cesar(mensagem, modo, chave):
    resultado = ""
    for cada_caractere in mensagem:
        if cada_caractere in DICIONARIO:
            indice_caractere = DICIONARIO.find(cada_caractere)
            if modo == "encriptar":
                indice_corrigido = indice_caractere + chave
            elif modo == "decriptar":
                indice_corrigido = indice_caractere - chave
            
            # DEVER DE CASA (destoscar a solução tosca):
            # SOLUÇÃO TOSCA:
            if indice_corrigido >= len(DICIONARIO):
                indice_corrigido = indice_corrigido - len(DICIONARIO)
            elif indice_corrigido < 0:
                indice_corrigido = indice_corrigido + len(DICIONARIO)
            
            resultado = resultado + DICIONARIO[indice_corrigido]
        else:
            resultado += cada_caractere
    return resultado