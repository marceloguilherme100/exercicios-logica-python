def inverter_string(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

# Teste
string = input("Digite uma string: ")
print(f"String invertida: {inverter_string(string)}")
