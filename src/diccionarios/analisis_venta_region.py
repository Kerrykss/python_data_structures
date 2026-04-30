# Análisis de ventas por región con diccionarios anidados

# 1. Dict anidado { region: { trimestre: ventas } }
ventas_por_region = {
    "Norte": {"Q1": 12_000, "Q2": 15_500, "Q3": 13_200, "Q4": 18_900},
    "Sur":   {"Q1": 9_800,  "Q2": 11_200, "Q3": 10_500, "Q4": 14_300},
    "Este":  {"Q1": 20_100, "Q2": 22_400, "Q3": 19_700, "Q4": 25_600},
    "Oeste": {"Q1": 16_300, "Q2": 17_800, "Q3": 15_900, "Q4": 21_100},
}

# 2. Total anual por región con items() y sum(values())
totales_por_region = {
    region: sum(trimestres.values())
    for region, trimestres in ventas_por_region.items()
}

# 3. Región con mayores ventas usando max() + key=lambda
mejor_region = max(totales_por_region, key=lambda r: totales_por_region[r])

# 4. Inicializar totales por trimestre
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

# 5. Acumular con iteración anidada
for trimestres in ventas_por_region.values():
    for trimestre, ventas in trimestres.items():
        totales_por_trimestre[trimestre] += ventas

# 6. Gran total y porcentajes con dict comprehension
gran_total = sum(totales_por_region.values())

porcentajes = {
    region: round(total / gran_total * 100, 1)
    for region, total in totales_por_region.items()
}

# 7. Reporte ordenado de mayor a menor con sorted() + items()
print("╔══════════════════════════════════════╗")
print("║       REPORTE ANUAL DE VENTAS        ║")
print("╠══════════════════════════════════════╣")

for region, total in sorted(totales_por_region.items(), key=lambda x: x[1], reverse=True):
    barra = "█" * int(porcentajes[region] / 2)
    print(f"  {region:<6}  ${total:>8,}  {porcentajes[region]:>5}%  {barra}")

print("╠══════════════════════════════════════╣")
print(f"  TOTAL   ${gran_total:>8,}  100.0%")
print(f"  Mejor región: {mejor_region} (${totales_por_region[mejor_region]:,})")
print("╚══════════════════════════════════════╝")

print("\n── Ventas acumuladas por trimestre ──")
for trimestre, total in totales_por_trimestre.items():
    print(f"  {trimestre}: ${total:,}")