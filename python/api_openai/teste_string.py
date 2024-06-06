from unidecode import unidecode

palavra = "CaRlOs%(@#*@ OOOO 0039202 ÇÇÇ ^^^~a ão ÃO ÁÁAÁ[S[S]])"
palavra = unidecode("".join(filter(str.isalpha, palavra)).upper())
print(palavra)