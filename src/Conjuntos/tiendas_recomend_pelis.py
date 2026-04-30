# Sets: tiendas y recomendaciones de películas

# 1. Catálogos de cada tienda como sets
tienda_centro = {"Acción", "Comedia", "Drama", "Terror", "Sci-Fi"}
tienda_norte  = {"Comedia", "Drama", "Animación", "Documental"}
tienda_sur    = {"Terror", "Sci-Fi", "Thriller", "Acción"}

# 2. Unión e intersección de las tres tiendas
catalogo_completo  = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes  = tienda_centro.intersection(tienda_norte, tienda_sur)

# 3. Exclusivos de cada tienda (géneros que solo esa tienda tiene)
exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
exclusivos_norte  = tienda_norte.difference(tienda_centro, tienda_sur)
exclusivos_sur    = tienda_sur.difference(tienda_centro, tienda_norte)

# isdisjoint() → True si no comparten ningún elemento
norte_sur_disjoint = tienda_norte.isdisjoint(tienda_sur)
centro_sur_disjoint = tienda_centro.isdisjoint(tienda_sur)

print("═══ ANÁLISIS DE TIENDAS ═══")
print(f"Catálogo completo   : {sorted(catalogo_completo)}")
print(f"Géneros en las 3    : {productos_comunes or '∅ (ninguno)'}")
print(f"Solo en Centro      : {exclusivos_centro}")
print(f"Solo en Norte       : {exclusivos_norte}")
print(f"Solo en Sur         : {exclusivos_sur}")
print(f"Norte y Sur sin solapamiento: {norte_sur_disjoint}")
print(f"Centro y Sur sin solapamiento: {centro_sur_disjoint}")

# ──────────────────────────────────────────────

# 4. Sets de géneros favoritos de cada usuario
usuario1 = {"Acción", "Sci-Fi", "Thriller"}
usuario2 = {"Sci-Fi", "Drama", "Animación"}
usuario3 = {"Comedia", "Drama", "Documental"}

# 5. Operadores matemáticos de sets
comunes_1_2    = usuario1 & usuario2          # intersección
universo       = usuario1 | usuario2 | usuario3  # unión
exclusivos_u1  = usuario1 - usuario2          # diferencia
solo_uno_u1_u2 = usuario1 ^ usuario2          # diferencia simétrica

# 6. Verificar subconjunto con <=
u1_subconjunto_universo = usuario1 <= universo
u2_subconjunto_u1       = usuario2 <= usuario1   # esperamos False

print("\n═══ RECOMENDACIONES DE PELÍCULAS ═══")
print(f"Gustos en común U1∩U2      : {comunes_1_2}")
print(f"Universo de géneros U1∪U2∪U3: {sorted(universo)}")
print(f"Le gusta a U1 pero no a U2  : {exclusivos_u1}")
print(f"Solo le gusta a uno (U1△U2) : {solo_uno_u1_u2}")
print(f"U1 ⊆ universo               : {u1_subconjunto_universo}")
print(f"U2 ⊆ U1                     : {u2_subconjunto_u1}")

# Recomendación: géneros que gustan a U2 o U3 pero U1 aún no conoce
recomendados_a_u1 = (usuario2 | usuario3) - usuario1
print(f"\nRecomendados para U1        : {recomendados_a_u1}")