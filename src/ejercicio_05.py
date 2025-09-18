import pandas as pd

def ejercicio_05():
    data = [
        {'empleado': 'Juan', 'salario': 3000, 'departamento': 'IT'},
        {'empleado': 'Ana', 'salario': 3500, 'departamento': 'HR'},
        {'empleado': 'Luis', 'salario': 2800, 'departamento': 'Ventas'}
    ]
    df = pd.DataFrame(data)
    print(df)
    print(df.iloc[0])
    print(df.iloc[1])

if __name__ == "__main__":
    ejercicio_05()
