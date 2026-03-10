# =========================================
# APUNTES TEÓRICOS DE ESTRUCTURAS LINEALES
# =========================================

# 1️ Listas simplemente enlazadas (Singly Linked List)
# ---------------------------------------------------
# Definición:
#   Colección de nodos donde cada nodo contiene un dato y un puntero al siguiente nodo.
# Características:
#   - Dinámica: su tamaño puede crecer o decrecer según necesidad.
#   - Recorrido lineal desde el primer nodo hasta el último.
#   - Inserción y eliminación eficiente al inicio; lenta en medio o final.
# Ventajas:
#   - No necesita tamaño fijo como un array.
#   - Eficiente para operaciones al inicio.
# Desventajas:
#   - Acceso a elementos intermedios es lineal O(n).
#   - Solo se puede recorrer en un sentido.

# 2️ Listas doblemente enlazadas (Doubly Linked List)
# ---------------------------------------------------
# Definición:
#   Cada nodo contiene un dato y dos punteros: uno al nodo siguiente y otro al anterior.
# Características:
#   - Permite recorrido en ambos sentidos (adelante y atrás).
#   - Inserción y eliminación eficiente si se tiene referencia al nodo.
# Ventajas:
#   - Más flexible que la lista simple.
#   - Permite retroceder en la lista fácilmente.
# Desventajas:
#   - Consume más memoria (dos punteros por nodo).
#   - Más compleja de implementar.

# 3️ Listas circulares
# ---------------------
# Definición:
#   El último nodo apunta al primero, formando un ciclo.
# Tipos:
#   - Simplemente circular: puntero solo al siguiente nodo.
#   - Doblemente circular: punteros al siguiente y al anterior.
# Ventajas:
#   - Útil en buffers circulares y sistemas cíclicos.
#   - No existe un "final" absoluto.
# Desventajas:
#   - Mayor complejidad de implementación.
#   - Riesgo de bucles infinitos si no se controla el recorrido.

# 4️ Pilas (Stacks)
# ------------------
# Definición:
#   Estructura LIFO (Last In, First Out): el último en entrar es el primero en salir.
# Operaciones:
#   - push(dato): insertar al tope.
#   - pop(): eliminar del tope.
#   - peek()/top(): ver el tope sin eliminarlo.
# Ventajas:
#   - Operaciones muy rápidas O(1).
#   - Útil en llamadas recursivas, undo/redo, evaluación de expresiones.
# Desventajas:
#   - Acceso limitado al elemento del tope únicamente.

# 5️ Colas (Queues)
# ------------------
# Definición:
#   Estructura FIFO (First In, First Out): el primero en entrar es el primero en salir.
# Operaciones:
#   - enqueue(dato): agregar al final.
#   - dequeue(): eliminar del inicio.
# Ventajas:
#   - Mantiene el orden de llegada.
#   - Muy útil para atención por turnos, impresión, mensajería.
# Desventajas:
#   - Acceso a elementos intermedios lento O(n).

# 6️ Colas con prioridad
# ----------------------
# Definición:
#   Cada elemento tiene una prioridad; el que tiene mayor prioridad se atiende primero.
# Características:
#   - Puede implementarse con listas enlazadas o heaps.
#   - Si dos elementos tienen la misma prioridad, se puede atender FIFO.
# Ventajas:
#   - Ideal para emergencias, planificación de CPU, atención médica.
#   - Permite atención eficiente según importancia.
# Desventajas:
#   - Inserción puede ser más costosa que en una cola simple O(n).
#   - Requiere comparar prioridades al insertar.

# 🔹 Comparación general
# ----------------------
# | Estructura       | Orden  | Acceso   | Inserción/Elim. | Uso típico                  |
# |-----------------|--------|----------|-----------------|-----------------------------|
# | Lista simple     | Secuencial | Lineal | O(1) inicio, O(n) medio/final | Listas dinámicas          |
# | Lista doble      | Secuencial | Bidireccional | O(1) inicio, O(n) medio/final | Recorridos bidireccionales |
# | Lista circular   | Circular   | Lineal/circular | O(1) inicio, O(n) medio/final | Buffers, juegos           |
# | Pila             | LIFO       | Tope     | O(1)            | Undo/redo, recursión       |
# | Cola             | FIFO       | Inicio/fin | O(1)          | Atención por orden de llegada|
# | Cola prioridad   | Por prioridad | Inicio | O(n) lista, O(log n) heap | Emergencias, CPU scheduling|