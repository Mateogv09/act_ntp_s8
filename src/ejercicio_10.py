import pandas as pd
import requests

def ejercicio_10():
    url = "https://playground.mockoon.com/users"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                df = pd.json_normalize(data)  # 👈 aplana los campos anidados
                print(df.head())
                print(df.info())
            else:
                print("La API devolvió un tipo inesperado:", type(data))
        else:
            print("Error en la petición. Código:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

if __name__ == "__main__":
    ejercicio_10()
