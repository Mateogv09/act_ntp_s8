import pandas as pd

def ejercicio_03():
   
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])

    print("💰 Serie de precios:")
    print(precios)
    print("\n🎟️ Serie de descuentos:")
    print(descuentos)

    
    resta = precios - descuentos
    precios_con_iva = precios * 1.16

    print("\n📌 Resta (precios - descuentos):")
    print(resta)

    print("\n📌 Precios con IVA (16%):")
    print(precios_con_iva)

    print("\n📌 Demostración de operaciones elemento por elemento:")
    for i in range(len(precios)):
        print(f"Precio {precios[i]} - Descuento {descuentos[i]} = {resta[i]}")

if __name__ == "__main__":
    ejercicio_03()
