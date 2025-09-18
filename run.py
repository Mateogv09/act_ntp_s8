import sys
import os

def run_exercise(num):
    # Ruta absoluta a la carpeta actual del proyecto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "src", f"ejercicio_{num:02d}.py")

    print(f"🔎 Buscando archivo en: {filename}")

    if os.path.exists(filename):
        print(f"▶ Ejecutando {filename}\n")
        os.system(f'python "{filename}"')
    else:
        print(f"❌ El archivo {filename} no existe.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python run.py <numero_ejercicio>")
        print("Ejemplo: python run.py 1")
    else:
        try:
            num = int(sys.argv[1])
            run_exercise(num)
        except ValueError:
            print("Debes ingresar un número válido.")
