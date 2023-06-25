import requests
import json

#Requesting API
response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

#Loading the response into a Python object
data = json.loads(response.text)

#Converting Text to Float
currencyFloat = float(data['USDBRL']['bid'])

#USD to BRL conversion function
def convertToUSD(currency):
    value = currency * currencyFloat
    rounded_num = round(value, 2)
    return rounded_num

#BRL to USD conversion function
def convertToBRL(currency):
    value = currency / currencyFloat
    rounded_num = round(value, 2)
    return rounded_num

#Introduction to the system
while True:
    print('\nHello, welcome to the daily exchange rate.\n')
    initialChoice = int(input('Select an option:\n1. Check USD value (BRL).\n2. Convert USD to BRL.\n3. Convert BRL to USD.\nYour choice: '))
    if initialChoice == 1:
        print(f"\n{data['USDBRL']['code']}: R${data['USDBRL']['bid']}")
        print('----------')
    elif initialChoice == 2:
        convertedValue = float(input('\nEnter the value to convert: '))
        print(f'USD: ${convertedValue}\nBRL: R${convertToUSD(convertedValue)}')
        print('----------')
    elif initialChoice == 3:
        convertedValue = float(input('\nEnter the value to convert: '))
        print(f'BRL: R${convertedValue}\nUSD: ${convertToBRL(convertedValue)}')
        print('----------')
    else:
        break
    
        
        
    
    
