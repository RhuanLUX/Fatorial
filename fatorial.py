# Função para calcular o fatorial de um número - em python

def fatorial(n):
    # Se n for zero, o fatorial é 1
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Solicita ao usuário um número e calcula o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
# f dentro do print é para deixar tudo como string
