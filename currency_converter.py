import requests

API_KEY = 'fca_live_zqXXFUPKACSnTYpWKoZTOByuveO3fp0C0X8DQxvq'
BASE_URL= f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","CAD","EUR","AUD","CNY","INR"]

def currency_convertor(base) :
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency= {base}&currencies = {CURRENCIES}"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"] 
    
    except Exception as e:
        print("Invalid Currency")
        return None


while True :
    ask = input("Enter the currency whose exchange rate want to see (q for quit ) :").upper()
    base = ask 
    if base =="Q":
       break

    data = currency_convertor(base)

    if not data :
       continue    
    
    del data[base]
    for ticker,value in data.items():
        print(f"{ticker}:{value}")

    