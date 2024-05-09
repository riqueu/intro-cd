"""Módulo Leitura Arquivos"""

def ler_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'r') as arquivo:
        for cada_linha in arquivo:
            texto.append(cada_linha)

def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as arquivo:
        for cada_linha in texto:
            arquivo.write(cada_linha)