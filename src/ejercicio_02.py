import pandas as pd

def ejercicio_02():
   
    serie = pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])

    print("📌 Serie de Calificaciones:")
    print(serie)
    print("\n✅ Acceder al valor de Ciencias:", serie['Ciencias'])

    
    print("\nℹ️ Información de la Serie:")
    print("Índices:", serie.index.tolist())
    print("Valores:", serie.values.tolist())
    print("Cantidad de elementos:", serie.size)

   
    print("\n📊 Estadísticas:")
    print("Suma:", serie.sum())
    print("Promedio:", serie.mean())

if __name__ == "__main__":
    ejercicio_02()
