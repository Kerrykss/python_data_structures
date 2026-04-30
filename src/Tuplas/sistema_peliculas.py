# Sistema de películas con tuplas

# 1. Catálogo: tupla de subtuplas (titulo, director, año, puntuacion)
catalogo = (
    ("El Padrino",          "Francis Ford Coppola", 1972, 9.2),
    ("Pulp Fiction",         "Quentin Tarantino",    1994, 8.9),
    ("Reservoir Dogs",       "Quentin Tarantino",    1992, 8.3),
    ("Interestelar",         "Christopher Nolan",    2014, 8.6),
    ("El origen",            "Christopher Nolan",    2010, 8.8),
)

# 2. Desempaquetar cada película en el bucle
print("=== CATÁLOGO COMPLETO ===")
for titulo, director, anio, puntuacion in catalogo:
    print(f"  {titulo} ({anio}) — {director} — ★ {puntuacion}")

# 3. Operador * para separar la primera película del resto
primera, *resto = catalogo
print(f"\nPrimera película : {primera[0]}")
print(f"Resto del catálogo: {len(resto)} películas")

# 4. Buscar películas por director
def buscar_por_director(director):
    return tuple(
        pelicula for pelicula in catalogo
        if pelicula[1].lower() == director.lower()
    )

# 5. Estadísticas: devuelve (min, max, promedio) de puntuaciones
def obtener_estadisticas(peliculas):
    puntuaciones = tuple(p[3] for p in peliculas)
    minima   = min(puntuaciones)
    maxima   = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    return (minima, maxima, round(promedio, 2))

# --- Llamadas ---

# Buscar por director
coincidencias = buscar_por_director("Quentin Tarantino")
print("\n=== PELÍCULAS DE TARANTINO ===")
for titulo, director, anio, puntuacion in coincidencias:
    print(f"  {titulo} ({anio}) — ★ {puntuacion}")

# 6. Desempaquetar retorno de obtener_estadisticas
minima, maxima, promedio = obtener_estadisticas(catalogo)
print(f"\n=== ESTADÍSTICAS ===")
print(f"  Mínima  : ★ {minima}")
print(f"  Máxima  : ★ {maxima}")
print(f"  Promedio: ★ {promedio}")