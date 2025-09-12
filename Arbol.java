package src.Old;
public class Arbol {
    private Nodo raiz;

      public Arbol() {
          this.raiz = null;
      }

      public boolean vacio() {
          return raiz == null;
      }

      public void insertar(String nombre) {
          raiz = insertarRec(raiz, nombre);
      }

      // Insertar
      private Nodo insertarRec(Nodo actual, String nombre) {
          if (actual == null) {
              return new Nodo(nombre);
          }

          if (nombre.compareTo(actual.nombre) < 0) {
              actual.izquierda = insertarRec(actual.izquierda, nombre);
          } else if (nombre.compareTo(actual.nombre) > 0) {
              actual.derecha = insertarRec(actual.derecha, nombre);
          }

          return actual;
      }

      // Buscar
      public Nodo buscarNodo(String nombre) {
          return buscarRec(raiz, nombre);
      }
      private Nodo buscarRec(Nodo actual, String nombre) {
          if (actual == null || actual.nombre.equals(nombre)) {
              return actual;
          }

          if (nombre.compareTo(actual.nombre) < 0) {
              return buscarRec(actual.izquierda, nombre);
          } else {
              return buscarRec(actual.derecha, nombre);
          }
      }

      // Imprimir
      public void inorden() {
          System.out.println("Raíz: " + (raiz != null ? raiz.nombre : "Arbol vacío"));
          inordenRec(raiz);
          System.out.println();
      }

      private void inordenRec(Nodo actual) {
          if (actual != null) {
              inordenRec(actual.izquierda);
              System.out.print(actual.nombre + " ");
              inordenRec(actual.derecha);
          }
      }

      
}
