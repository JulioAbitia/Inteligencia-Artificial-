import heapq

def dijkstra(grafo, inicio):
    # Distancias iniciales: infinito para todos menos el inicio
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Cola de prioridad (min-heap)
    cola = [(0, inicio)]  # (distancia, nodo)

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si ya encontramos una distancia mejor antes, se ignora
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Revisar vecinos
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Si encontramos un camino más corto
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))

    return distancias

# Grafo de ejemplo (diccionario de diccionarios)
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'E': 3},
    'D': {'B': 10, 'E': 4},
    'E': {'C': 3, 'D': 4}
}

# Ejecutar algoritmo desde el nodo A
resultado = dijkstra(grafo, 'A')
print("Distancias más cortas desde A:")
print(resultado)
