#Enunciado:  Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/', timeout=10)

except (urllib.error.URLError, TimeoutError):
    print('ERRO! O site Pudim não está acessível no momento.')

else:
    print('O site Pudim foi acessado corretamente!')
    site.close()