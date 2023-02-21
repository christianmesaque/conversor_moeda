import requests
import json

def conversor(valor, de, para):
    api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")

    if api.status_code == 200:
        response = api.json()
        return float(response[0]['bid']) * valor
    else:
        return None 


print('===== CONVERSOR DE MOEDAS ====')
print('Principais moedas: BRL, USD, EUR')

valor = float(input("Valor: "))
de = input("Converter de (código moeda): ")
para = input("Para (código moeda): ")

cotacao = conversor(valor, de, para)


if cotacao is not None:
    print(f"{valor} {de} é quivalente a {cotacao} {para}")
else:
    print("ERRO: moeda inválida.")
        