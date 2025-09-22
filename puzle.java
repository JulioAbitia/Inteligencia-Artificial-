package src.Old;

public class puzle {
    public static void main(String[] args) {
        Arbol arbol = new Arbol(new Nodo("1234567 8", null));

        // Ejecutamos directamente IDDFS
        System.out.println("===== Búsqueda en Profundidad Iterativa (IDDFS) =====");
        Nodo resultado = arbol.busquedaProfundidadIterativa("12345678 ", 20);
        arbol.mostrarCamino(resultado);
    }    
}
