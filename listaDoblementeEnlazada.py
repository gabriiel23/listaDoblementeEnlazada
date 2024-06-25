# Actividad usando la lista doblemente enlazada

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = Nodo()  # Nodo fantasma al principio
        self.tail = Nodo()  # Nodo fantasma al final
        self.head.siguiente = self.tail
        self.tail.anterior = self.head
        self.cursor = self.head  # El cursor comienza en el nodo fantasma al principio

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.anterior = self.cursor
        nuevo_nodo.siguiente = self.cursor.siguiente
        self.cursor.siguiente.anterior = nuevo_nodo
        self.cursor.siguiente = nuevo_nodo
        self.cursor = nuevo_nodo

    def eliminar(self):
        if self.cursor != self.head:
            self.cursor.anterior.siguiente = self.cursor.siguiente
            self.cursor.siguiente.anterior = self.cursor.anterior
            self.cursor = self.cursor.anterior

    def mover_cursor_izquierda(self):
        if self.cursor != self.head:
            self.cursor = self.cursor.anterior

    def mover_cursor_derecha(self):
        if self.cursor.siguiente != self.tail:
            self.cursor = self.cursor.siguiente

    def obtener_texto(self):
        actual = self.head.siguiente
        texto = []
        while actual != self.tail:
            texto.append(actual.valor)
            actual = actual.siguiente
        return ''.join(texto)

class EditorTexto:
    def __init__(self):
        self.lista = ListaDoblementeEnlazada()

    def insertar(self, caracter):
        self.lista.insertar(caracter)

    def eliminar(self):
        self.lista.eliminar()

    def mover_cursor_izquierda(self):
        self.lista.mover_cursor_izquierda()

    def mover_cursor_derecha(self):
        self.lista.mover_cursor_derecha()

    def mostrar_texto(self):
        print(self.lista.obtener_texto())

# Ejecución interactiva
def main():
    editor = EditorTexto()
    print("----------------------------")
    print("   Editor de texto simple   ")
    print("----------------------------")
    print("")
    print("Comandos disponibles:")
    print("")
    print("1. Para insertar un caracter en la posición del cursor escriba: insertar <caracter que desea ingresar>")
    print("2. Para eliminar el caracter en la posición del cursor escriba: eliminar")
    print("3. Para mover el cursor a la izquierda escriba: izquierda")
    print("4. Para mover el cursor a la derecha escriba: derecha")
    print("5. Para mostrar el texto actual escriba: mostrar")
    print("6. Para terminar el programa escriba: salir")
    print("")

    while True:
        comando = input("Comando: ").strip().split()
        if not comando:
            continue

        accion = comando[0].lower()

        if accion == "insertar" and len(comando) == 2:
            caracter = comando[1]
            editor.insertar(caracter)
        elif accion == "eliminar":
            editor.eliminar()
        elif accion == "izquierda":
            editor.mover_cursor_izquierda()
        elif accion == "derecha":
            editor.mover_cursor_derecha()
        elif accion == "mostrar":
            editor.mostrar_texto()
        elif accion == "salir":
            print("Gracias por usar este programa...")
            print("")
            break
        else:
            print("Comando no reconocido. Intente de nuevo.")

if __name__ == "__main__":
    main()
