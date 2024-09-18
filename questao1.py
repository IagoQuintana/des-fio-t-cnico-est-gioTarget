"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de 
Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

def sequencia_fibonacci(numero):
       
    sequencia = [0, 1]
    while True:
            proximo_valor = sequencia[-1] + sequencia[-2]
            if proximo_valor > numero:
                    break
            sequencia.append(proximo_valor)
        
    return sequencia


def pertence_sequencia(numero):
       sequencia = sequencia_fibonacci(numero)
       if numero in sequencia:
              return f"O número {numero} pertence à sequência de Fibonacci.\n"
       else:
              return f"O número {numero} não pertence à sequência de Fibonacci.\n"
       


    
numero = int(input("Informe o número a ser verificado:\n"))
resultado = pertence_sequencia(numero)
print(resultado)
