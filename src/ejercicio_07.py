import pandas as pd
import csv
import os

def ejercicio_07():
    filename = "cursos.csv"
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["curso", "instructor", "duracion"])
            writer.writerow(["Python", "Carlos", "3 meses"])
            writer.writerow(["SQL", "Ana", "2 meses"])
            writer.writerow(["Excel", "Luis", "1 mes"])
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            print(df)
        else:
            print("El archivo no existe.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    ejercicio_07()
