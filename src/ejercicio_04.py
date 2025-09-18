import pandas as pd

def ejercicio_04():
    data = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet'],
        'Precio': [1200, 800, 400],
        'Categoria': ['Electrónica', 'Electrónica', 'Electrónica']
    }
    df = pd.DataFrame(data)
    print(df)
    print(df['Precio'])
    print(df.info())

if __name__ == "__main__":
    ejercicio_04()
