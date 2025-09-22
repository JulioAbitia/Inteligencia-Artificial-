package src.Old;

import java.util.*;

public class Arbol {
    Nodo raiz;

    public Arbol(Nodo raiz){
        this.raiz = raiz;
    }

    // 🔹 Búsqueda en Anchura (BFS)
    public Nodo realizarBusquedaEnAnchura(String objetivo){
        HashSet<String> visitados = new HashSet<>();
        Queue<Nodo> cola = new LinkedList<>();
        cola.add(raiz);
        visitados.add(raiz.estado);

        while (!cola.isEmpty()) {
            Nodo actual = cola.poll();
            if (actual.estado.equals(objetivo)) {
                return actual;
            }
            for (String sucesor : Nodo.obtenerSucesores(actual.estado)) {
                if (!visitados.contains(sucesor)) {
                    Nodo hijo = new Nodo(sucesor, actual);
                    cola.add(hijo);
                    visitados.add(sucesor);
                }
            }
        }
        return null;
    }

    // 🔹 Búsqueda en Profundidad (DFS)
    public Nodo busquedaProfundidad(String objetivo){
        HashSet<String> visitados = new HashSet<>();
        Stack<Nodo> pila = new Stack<>();
        pila.push(raiz);
        visitados.add(raiz.estado);

        while (!pila.isEmpty()) {
            Nodo actual = pila.pop();
            if (actual.estado.equals(objetivo)) {
                return actual;
            }
            for (String sucesor : Nodo.obtenerSucesores(actual.estado)) {
                if (!visitados.contains(sucesor)) {
                    Nodo hijo = new Nodo(sucesor, actual);
                    pila.push(hijo);
                    visitados.add(sucesor);
                }
            }
        }
        return null;
    }

    // 🔹 Búsqueda de Costo Uniforme (UCS)
    public Nodo busquedaCostoUniforme(String objetivo){
        HashSet<String> visitados = new HashSet<>();
        PriorityQueue<Nodo> frontera = new PriorityQueue<>(Comparator.comparingInt(n -> n.costo));

        raiz.costo = 0;
        frontera.add(raiz);

        while (!frontera.isEmpty()) {
            Nodo actual = frontera.poll();

            if (actual.estado.equals(objetivo)) {
                return actual;
            }
            if (!visitados.contains(actual.estado)) {
                visitados.add(actual.estado);
                for (String sucesor : Nodo.obtenerSucesores(actual.estado)) {
                    if (!visitados.contains(sucesor)) {
                        Nodo hijo = new Nodo(sucesor, actual);
                        hijo.costo = actual.costo + 1; // cada movimiento cuesta 1
                        frontera.add(hijo);
                    }
                }
            }
        }
        return null;
    }

    // 🔹 Búsqueda en Profundidad Limitada (DLS)
    private Nodo busquedaLimitada(Nodo nodo, String objetivo, int limite, HashSet<String> visitados) {
        if (nodo.estado.equals(objetivo)) {
            return nodo;
        }
        if (limite <= 0) {
            return null;
        }

        visitados.add(nodo.estado);

        for (String sucesor : Nodo.obtenerSucesores(nodo.estado)) {
            if (!visitados.contains(sucesor)) {
                Nodo hijo = new Nodo(sucesor, nodo);
                Nodo resultado = busquedaLimitada(hijo, objetivo, limite - 1, visitados);
                if (resultado != null) {
                    return resultado;
                }
            }
        }
        return null;
    }

    // 🔹 Búsqueda en Profundidad Iterativa (IDDFS)
    public Nodo busquedaProfundidadIterativa(String objetivo, int maxProfundidad) {
        for (int limite = 0; limite <= maxProfundidad; limite++) {
            HashSet<String> visitados = new HashSet<>();
            Nodo resultado = busquedaLimitada(raiz, objetivo, limite, visitados);
            if (resultado != null) {
                return resultado;
            }
        }
        return null;
    }

    // 🔹 Mostrar el camino desde el inicial hasta la solución
    public void mostrarCamino(Nodo solucion) {
        if (solucion == null) {
            System.out.println("No hay solución.");
            return;
        }
        List<String> camino = new ArrayList<>();
        Nodo actual = solucion;
        while (actual != null) {
            camino.add(actual.estado);
            actual = actual.padre;
        }
        Collections.reverse(camino);

        System.out.println("\nMovimientos:");
        for (String estado : camino) {
            imprimirTablero(estado);
            System.out.println("________");
        }
    }

    // 🔹 Imprimir el tablero en formato 3x3
    private void imprimirTablero(String estado) {
        for (int i = 0; i < estado.length(); i++) {
            char c = estado.charAt(i);
            System.out.print((c == ' ' ? "x" : c) + " ");
            if ((i + 1) % 3 == 0) {
                System.out.println();
            }
        }
    }
}
