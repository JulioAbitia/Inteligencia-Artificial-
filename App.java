package src.Old;

public class App {
    public static void main(String[] args) {
        String estadoInicial = "1234567 8";
        String estadoFinal   = "12345678 ";

        Arbol arbol = new Arbol(new Nodo(estadoInicial, null));

        // ===== BFS =====
        System.out.println("===== BFS (Anchura) =====");
        Nodo resultadoBFS = arbol.realizarBusquedaEnAnchura(estadoFinal);
        arbol.mostrarCamino(resultadoBFS);

        // ===== DFS =====
        System.out.println("===== DFS (Profundidad) =====");
        Nodo resultadoDFS = arbol.busquedaProfundidad(estadoFinal);
        arbol.mostrarCamino(resultadoDFS);

        // ===== UCS =====
        System.out.println("===== UCS (Costo Uniforme) =====");
        Nodo resultadoUCS = arbol.busquedaCostoUniforme(estadoFinal);
        arbol.mostrarCamino(resultadoUCS);

        // ===== IDDFS =====
        System.out.println("===== Búsqueda en Profundidad Iterativa (IDDFS) =====");
        Nodo resultadoIDDFS = arbol.busquedaProfundidadIterativa(estadoFinal, 20);
        arbol.mostrarCamino(resultadoIDDFS);
    }
}
