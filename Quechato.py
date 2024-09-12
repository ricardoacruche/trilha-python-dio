def soma_tupla (tupla):
    return sum(tupla)
    
if __name__ == "__main__":
    entrada = "2 5 6 7 9"
    elementos = tuple(map(int, entrada.split()))
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
    
    entrada = "9 8 7 6 5"
    elementos = tuple(map(int, entrada.split()))
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
    
    entrada = "50 50 50 50"
    elementos = tuple(map(int, entrada.split()))
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")