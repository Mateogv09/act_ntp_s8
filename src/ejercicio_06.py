import pandas as pd

def ejercicio_06():
    data = [
        ['Cien años de soledad', 'Gabriel García Márquez', 1967],
        ['Don Quijote', 'Miguel de Cervantes', 1605],
        ['La ciudad y los perros', 'Mario Vargas Llosa', 1963]
    ]
    df = pd.DataFrame(data, columns=['Titulo', 'Autor', 'Año'])
    print(df)
    print("Dimensiones:", df.shape)

if __name__ == "__main__":
    ejercicio_06()
