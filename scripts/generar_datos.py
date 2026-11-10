import argparse
import csv
import random
from pathlib import Path
from calculadora import sumar, restar, multiplicar, dividir

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, required=True)
parser.add_argument("--seed", type=int, default=42)
args = parser.parse_args()

random.seed(args.seed)
Path("datos").mkdir(exist_ok=True)

operaciones = {
    "suma": sumar,
    "resta": restar,
    "multiplicacion": multiplicar,
    "division": dividir
}

with open("datos/operaciones.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["id", "operacion", "a", "b", "resultado"])

    for i in range(args.n):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        nombre = random.choice(list(operaciones))
        resultado = operaciones[nombre](a, b)
        writer.writerow([i + 1, nombre, a, b, resultado])

print(f"Dataset generado: {args.n} registros")