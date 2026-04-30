# Analizador de ventas con list, dict y set comprehension

# Dataset: lista de dicts con 6 productos
ventas = [
    {"producto": "Laptop",     "unidades": 12, "precio": 899.99, "categoria": "Tecnología"},
    {"producto": "Auriculares", "unidades": 45, "precio":  59.99, "categoria": "Tecnología"},
    {"producto": "Escritorio",  "unidades":  8, "precio": 349.00, "categoria": "Mobiliario"},
    {"producto": "Bolígrafo",   "unidades":200, "precio":   1.50, "categoria": "Papelería"},
    {"producto": "Monitor",     "unidades": 20, "precio": 299.00, "categoria": "Tecnología"},
    {"producto": "Silla",       "unidades": 15, "precio": 189.00, "categoria": "Mobiliario"},
]

# ── LIST COMPREHENSIONS ──────────────────────────────────────

# 1. Valor total por producto (unidades × precio)
valor_total = [round(v["unidades"] * v["precio"], 2) for v in ventas]

# 2. Nombres de productos con valor_total > 1000
productos_destacados = [
    v["producto"]
    for v, total in zip(ventas, valor_total)
    if total > 1_000
]

# ── DICT COMPREHENSIONS ──────────────────────────────────────

# 3. producto_info: nombre → {valor, unidades}
producto_info = {
    v["producto"]: {"valor": total, "unidades": v["unidades"]}
    for v, total in zip(ventas, valor_total)
}

# 4. ranking_premium: precio > 50, ordenado por valor desc
ranking_premium = dict(
    sorted(
        {
            v["producto"]: total
            for v, total in zip(ventas, valor_total)
            if v["precio"] > 50
        }.items(),
        key=lambda x: x[1],
        reverse=True,
    )
)

# ── SET COMPREHENSIONS ───────────────────────────────────────

# 5. Categorías únicas presentes en el dataset
categorias_unicas = {v["categoria"] for v in ventas}

# 6. Nombres de productos baratos (precio ≤ 50)
productos_baratos = {v["producto"] for v in ventas if v["precio"] <= 50}

# ── COMBINACIÓN FINAL ────────────────────────────────────────

# 7. Resumen formateado: solo productos destacados con su info
resumen_formateado = {
    nombre: f"${info['valor']:,.2f} ({info['unidades']} uds)"
    for nombre, info in producto_info.items()
    if nombre in productos_destacados
}

gran_total = sum(valor_total)

# ── IMPRESIÓN ────────────────────────────────────────────────
print("── Valores por producto ──")
for v, total in zip(ventas, valor_total):
    print(f"  {v['producto']:<14} ${total:>8,.2f}")

print(f"\n── Destacados (> $1 000) ──\n  {productos_destacados}")

print("\n── Ranking premium (precio > $50) ──")
for i, (nombre, total) in enumerate(ranking_premium.items(), 1):
    print(f"  {i}. {nombre:<14} ${total:>8,.2f}")

print(f"\n── Categorías únicas ──\n  {categorias_unicas}")
print(f"── Productos baratos (≤ $50) ──\n  {productos_baratos}")

print("\n── Resumen destacados ──")
for nombre, detalle in resumen_formateado.items():
    print(f"  {nombre:<14} {detalle}")

print(f"\n  GRAN TOTAL: ${gran_total:,.2f}")