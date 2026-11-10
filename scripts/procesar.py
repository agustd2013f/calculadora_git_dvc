import csv
from collections import defaultdict
from pathlib import Path

estadisticas = defaultdict(list)

with open("datos/operaciones.csv", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)

    for fila in reader:
        operacion = fila["operacion"]
        resultado = float(fila["resultado"])
        estadisticas[operacion].append(resultado)

Path("resultados").mkdir(exist_ok=True)

with open("resultados/resumen.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["operacion", "cantidad", "promedio"])

    for operacion, valores in sorted(estadisticas.items()):
        cantidad = len(valores)
        promedio = sum(valores) / cantidad
        writer.writerow([operacion, cantidad, promedio])

print("Resumen generado correctamente")