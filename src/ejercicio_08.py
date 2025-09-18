import pandas as pd
import json
import os

def ejercicio_08():
    filename = "vehiculos.json"
    data = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Fiesta", "año": 2018},
        {"marca": "Honda", "modelo": "Civic", "año": 2021}
    ]
    with open(filename, "w") as file:
        json.dump(data, file)
    if os.path.exists(filename):
        df = pd.read_json(filename)
        print(df)
        print(df.dtypes)
    else:
        print("El archivo no existe.")

if __name__ == "__main__":
    ejercicio_08()
