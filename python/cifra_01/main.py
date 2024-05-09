"""Módulo Principal: PROJETO 2"""

import criptografia
import arquivos

mensagem_clara = []
mensagem_cifrada = []

nome_arquivo_entrada = "mensagem_clara.txt"
nome_arquivo_saida = "mensagem_cifrada.txt"
chave = 3
metodo = "cesar"

arquivos.ler_arquivo(nome_arquivo_entrada, mensagem_clara)
criptografia.encriptar(mensagem_clara, mensagem_cifrada, chave, metodo)
arquivos.escrever_arquivo(nome_arquivo_saida, mensagem_cifrada)