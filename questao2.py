"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

"""

def confere_letras(texto):
    
    soma = 0

    if "a" in texto :
            for letra in texto:
                   if letra =="a":
                          soma += 1

            print (f"A letra 'a' está presente na string e aparece {soma} vezes!\n")
    else:
            print (f"A letra 'a' não está presente na string\n")
    
    soma = 0
           
                      
string = input("Informe a String que será verificada:\n")
string = string.lower()

confere_letras(string)