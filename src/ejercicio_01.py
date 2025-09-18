import pandas as pd

def ejercicio_01():
   
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165],
                       index=["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"])

    
    valor_indice_3 = ventas[3]

   
    promedio = ventas.mean()

   
    ventas_ordenadas = ventas.sort_values()

    
    print("Ventas diarias:")
    print(ventas)
    print("\nValor en el índice 3:", valor_indice_3)
    print("Promedio de ventas:", promedio)
    print("\nVentas ordenadas:")
    print(ventas_ordenadas)


if __name__ == "__main__":
    ejercicio_01()
