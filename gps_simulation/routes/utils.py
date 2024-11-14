import heapq
from .models import City, Route

def dijkstra(start_city):
    distances = {start_city:0}
    previous_cities = {start_city:None}
    cola_prioridad = [(0, start_city)]
    
    while cola_prioridad:
        distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distances[ciudad_actual]:
            continue

        for vecino, peso in ciudad_actual.obtener_vecinos():
            distancia = distancia_actual + peso

            if distancia < distances.get(vecino, float('inf')):
                distances[vecino] = distancia
                previous_cities[vecino] = ciudad_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distances, previous_cities

def get_shortest_path(start_city, end_city):
    distances, previous_cities = dijkstra(start_city)
    path = []
    city = end_city

    while previous_cities[city]:
        path.insert(0, city)
        city = previous_cities[city]
    path.insert(0, city)

    return path, distances[end_city]

class ArbolBinarioBusqueda:

    def __init__(self): # Constructor de la clase
        self.raiz = None # atributo raiz inicializado como None
        self.tamano = 0 # atributo tamano inicializado en 0

    def agregar(self,clave,valor): #Metodo agregar toma dos parametros
        if self.raiz: #si la raiz del objeto contiene algo
            self._agregar(clave,valor,self.raiz) #usa el método _agregar con los mismos parametros mas la raiz del objeto
        else: # si la raiz del objeto no contiene nada
            self.raiz = NodoArbol(clave,valor) # se crea un nodo con los mismos dos parametros y se guarda en la raiz del objeto
        self.tamano = self.tamano + 1 # al atributo tamaño del objeto se le suma 1

    def _agregar(self,clave,valor,nodoActual): #Metodo _agregar toma tres parametros
        if clave < nodoActual.clave: # si la clave pasada por parametro es menor que la clave del nodo actual
            if nodoActual.tieneHijoIzquierdo(): # si el nodo actual tiene hijo izquierdo
                self._agregar(clave,valor,nodoActual.hijoIzquierdo) # Va a seguir ejecutandose _agregar recursivamente
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual) # Se crea el nuevo nodo y se guarda en el hijo izquierdo de nodoActual
        else: # si la clave pasada por parametro es mayor o igual que la clave del nodo actual
            if nodoActual.tieneHijoDerecho(): # si el actual tiene hijo derecho
                self._agregar(clave,valor,nodoActual.hijoDerecho) # Se va a ejecutar recursivamente el metodo _agregar
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) # Se crea el nuevo nodo y se guarda en el hijo derecho de nodoActual

    def __setitem__(self,c,v): # Este metodo se usa para que un objeto de una clase actue como un contenedor de tipo diccionario o lista, toma una clave y un valor y lo asigna o actualiza.
        self.agregar(c,v) # Se invoca al método agregar

    def obtener(self,clave): # Este método busca un nodo en el arbol segun su clave, si lo encuentra; devuelve su carga útil
        if self.raiz: # si el objeto contiene raiz
            res = self._obtener(clave,self.raiz) #se guarda en la variable res lo retornado por la funcion _obtener, se le pasa el atributo clave y el self.raiz
            if res: # si hay algo
                return res.cargaUtil # Si se encuentra el nodo, se devuelve su carga útil (valor)
            else: # Sino
                return None # Si no se encuentra el nodo, se devuelve None
        else: # Si no contiene raiz
            return None # Si el árbol está vacío, se devuelve None

    def _obtener(self,clave,nodoActual): # Este método recursivo busca el nodo con la clave especificada
        if not nodoActual: # Si no hay nada
            return None # Si el nodo es None, significa que hemos llegado a un punto que está vacío
        elif nodoActual.clave == clave: # Si el nodo actual tiene la clave buscada
            return nodoActual # se retorna el nodo
        elif clave < nodoActual.clave: # Si la clave es menor
            return self._obtener(clave,nodoActual.hijoIzquierdo) # buscar en el subárbol izquierdo
        else: # Si la clave es mayor
            return self._obtener(clave,nodoActual.hijoDerecho) # buscar en el subárbol derecho

    def obtener_claves(self): # Este método devuelve una lista con todas las claves del árbol, en orden ascendente
        claves = [] # Crea una lista vacía para almacenar las claves
        self._obtener_claves(self.raiz, claves) # Llama al método recursivo para llenar la lista
        return claves # Retorna la lista de claves

    def _obtener_claves(self, nodoActual, claves): # Este método realiza un recorrido en inorden (izquierda, raíz, derecha) para llenar la lista "claves" con las claves del árbol en orden ascendente
        if nodoActual: # Si el nodo actual no es None
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self): # Este método retorna una lista de los valores del árbol, usando las claves obtenidas con el método obtener_claves
        return [self.obtener(clave) for clave in self.obtener_claves()] # Devuelve una lista de valores, usando las claves en orden

    def __getitem__(self,clave): # Este metodo se usa para que un objeto de una clase actue como un contenedor de tipo diccionario o lista, toma una clave y devuelve el valor
        res = self.obtener(clave) # Crea una variable y le da el valor de "self.obtener(clave)"
        if res: # Si se encuentra la clave
            return res # se retorna el valor
        else: # Si no encuentra la clave
            raise KeyError('Error, la clave no está en el árbol') # se lanza una excepción

    def __contains__(self,clave): # Este método permite verificar si una clave está en el árbol, como un método "in" en un diccionario
        if self._obtener(clave,self.raiz):  # Si el nodo con la clave se encuentra en el árbol
            return True # Retorna True
        else: # si no
            return False # rRetorna False

    def longitud(self): # Este método devuelve el número de nodos en el árbol (el tamaño del árbol)
        return self.tamano # Retorna el número de nodos en el árbol

    def __len__(self): # Este método permite usar la función len() en una instancia de ArbolBinarioBusqueda para obtener su tamaño
        return self.tamano # Permite usar len() en el árbol y retorna el tamaño

    def __iter__(self): # Este método devuelve un iterador para recorrer los nodos del árbol (el recorrido específico no está implementado en este fragmento)
        return self.raiz.__iter__() # Devuelve un iterador para recorrer los nodos del árbol

    def eliminar(self,clave): # Este método elimina un nodo con la clave dada
        if self.tamano > 1: # si tamaño es mayor a 1
            nodoAEliminar = self._obtener(clave,self.raiz) # Busca el nodo con la clave
            if nodoAEliminar: # Se contiene algo
                self.remover(nodoAEliminar) # Si lo encuentra, lo elimina
                self.tamano = self.tamano-1 # y le resta 1 al atributo tamaño
            else: # Si no lo encuentra
                raise KeyError('Error, la clave no está en el árbol') # Se lanza un error
        elif self.tamano == 1 and self.raiz.clave == clave: # Si el arbol tgiene un solo nodo
            self.raiz = None # Lo elimina
            self.tamano = self.tamano - 1 # y le resta 1 al atributo tamaño
        else: # Si no encuentra nada
            raise KeyError('Error, la clave no está en el árbol') # Le lanza un error

    def __delitem__(self,clave): # Este metodo permite usar el operador "del" en el árbol, lo que invoca el método eliminar.
        self.eliminar(clave) # Permite usar el operador "del" para eliminar un nodo del árbol

    def remover(self,nodoActual): # Este método se encarga de eliminar un nodo del árbol, dependiendo del tipo de nodo (hoja, nodo con dos hijos o nodo con un solo hijo), realiza diferentes operaciones
        if nodoActual.esHoja(): # Si el nodo es hoja (sin hijos)
            if nodoActual == nodoActual.padre.hijoIzquierdo: # Si el nodo actual es igual al hijo izquierdo del padre del nodo actual
                nodoActual.padre.hijoIzquierdo = None # Se elimina de su padre
            else: # Si es hijo derecho
                nodoActual.padre.hijoDerecho = None # Se elimina del padre
        elif nodoActual.tieneAmbosHijos(): # Si tiene ambos hijos
            suc = nodoActual.encontrarSucesor() # Se encuentra el sucesor en el subárbol derecho
            suc.empalmar() # El sucesor reemplaza al nodo actual
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else: # si este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo(): # Si tiene hijo izquierdo
                if nodoActual.esHijoIzquierdo(): #Si el nodo actual es el hijo izquierdo de su padre, el hijo izquierdo del nodo actual (nodoActual.hijoIzquierdo) debe ser conectado al padre del nodo actual
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # Se asigna el padre del nodo actual al hijo izquierdo, para que el hijo izquierdo ahora apunte correctamente hacia el padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo # el padre del nodo actual debe actualizar su referencia al hijo izquierdo, apuntando ahora al hijo izquierdo del nodo actual (ya que el nodo está siendo eliminado)
                elif nodoActual.esHijoDerecho(): # Si el nodo actual es el hijo derecho de su padre, entonces se ejecuta el bloque correspondiente
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # se asigna el padre del nodo actual al hijo izquierdo, para que apunte correctamente hacia el padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo # Se actualiza el enlace del padre para que su hijo derecho apunte al hijo izquierdo del nodo actual
                else: # Si el nodo no es ni hijo izquierdo ni hijo derecho de su padre
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho) # Se llama a reemplazarDatoDeNodo() para reemplazar la clave, la carga útil y los hijos del nodo actual con los del hijo izquierdo
            else: # Si tiene hijo derecho
                if nodoActual.esHijoIzquierdo(): #Si el nodo actual es el hijo izquierdo de su padre, el hijo izquierdo del nodo actual (nodoActual.hijoIzquierdo) debe ser conectado al padre del nodo actual
                    nodoActual.hijoDerecho.padre = nodoActual.padre # Se asigna el padre del nodo actual al hijo izquierdo, para que el hijo izquierdo ahora apunte correctamente hacia el padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho # el padre del nodo actual debe actualizar su referencia al hijo izquierdo, apuntando ahora al hijo derecho del nodo actual (ya que el nodo está siendo eliminado)
                elif nodoActual.esHijoDerecho(): # Si el nodo actual es el hijo derecho de su padre, entonces se ejecuta el bloque correspondiente
                    nodoActual.hijoDerecho.padre = nodoActual.padre # se asigna el padre del nodo actual al hijo derecho, para que apunte correctamente hacia el padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho # Se actualiza el enlace del padre para que su hijo derecho apunte al hijo derecho del nodo actual
                else: # Si el nodo no es ni hijo izquierdo ni hijo derecho de su padre
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho) # Se llama a reemplazarDatoDeNodo() para reemplazar la clave, la carga útil y los hijos del nodo actual con los del hijo derecho

    def inorden(self): # Define el método inorden
        self._inorden(self.raiz) # llama al método privado _inorden, pasando la raíz del árbol (self.raiz) como argumento. El recorrido en inorden visita los nodos de izquierda a derecha: primero recorre el subárbol izquierdo, luego visita el nodo actual y finalmente recorre el subárbol derecho.

    def _inorden(self,arbol): # Define el metodo _inorden
        if arbol != None: # Si el árbol es distinto de None sigue
            self._inorden(arbol.hijoIzquierdo) # Recorre el subárbol izquierdo
            print(arbol.clave) # Imprime la clave del nodo actual
            self._inorden(arbol.hijoDerecho) # Recorre el subárbol derecho

    def postorden(self): # Define el méttodo postorden
        self._postorden(self.raiz) # inicia el recorrido postorden desde la raíz del árbol

    def _postorden(self, arbol): # Define el método _postorden
        if arbol: # si allrbol contiene algo
            self._postorden(arbol.hijoDerecho) # Recorre primero el subárbol derecho
            self._postorden(arbol.hijoIzquierdo) # Luego recorre el subárbol izquierdo
            print(arbol.clave) # Imprime la clave del nodo actual después de recorrer los hijos

    def preorden(self): # Define el método preorden
        self._preorden(self.raiz) # inicia el recorrido preorden desde la raíz del árbol

    def _preorden(self,arbol): # Define el metodo _preorden
        if arbol: # Si el arbol contiene algo
            print(arbol.clave) # Primero imprime la clave del nodo actual
            self._preorden(arbol.hijoIzquierdo) # Recorre el subárbol izquierdo
            self._preorden(arbol.hijoDerecho) # Recorre el subárbol derecho

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None): # Constructor de la clase
        self.clave = clave # atributo clave
        self.cargaUtil = valor # atributo cargaUtil
        self.hijoIzquierdo = izquierdo # atributo hijoIzquierdo es izquierdo
        self.hijoDerecho = derecho # atributo hijoDerecho es derecho
        self.padre = padre # Atributo padre
        self.factorEquilibrio = 0 # atributo inicializado en 0

    def tieneHijoIzquierdo(self): # Metodo tieneHijoIzquierdo
        return self.hijoIzquierdo  # Devuelve True si el nodo tiene un hijo izquierdo

    def tieneHijoDerecho(self): # Método tieneHijoDerecho
        return self.hijoDerecho # Devuelve True si el nodo tiene un hijo derecho

    def esHijoIzquierdo(self): # Método tieneHijoDerecho
        return self.padre and self.padre.hijoIzquierdo == self # Devuelve True si el nodo actual es el hijo izquierdo de su padre

    def esHijoDerecho(self): # Método esHijoDerecho
        return self.padre and self.padre.hijoDerecho == self # Devuelve True si el nodo actual es el hijo derecho de su padre

    def esRaiz(self): # Méodo esRaiz
        return not self.padre # Devuelve True si el nodo es la raíz del árbol (es decir, si no tiene padre)

    def esHoja(self): # Método esHoja
        return not (self.hijoDerecho or self.hijoIzquierdo) # Devuelve True si el nodo es una hoja, es decir, si no tiene hijos

    def tieneAlgunHijo(self): # Método tieneAlgunHijo
        return self.hijoDerecho or self.hijoIzquierdo #  Devuelve True si el nodo tiene al menos un hijo (izquierdo o derecho)

    def tieneAmbosHijos(self): # Método tieneAmbosHijos
        return self.hijoDerecho and self.hijoIzquierdo # devuelve True si el nodo tiene ambos hijos (izquierdo y derecho)

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder): # Método reemplazarDatoDeNodo
        self.clave = clave # Actualiza la clave del nodo
        self.cargaUtil = valor # Actualiza la cargaUtil
        self.hijoIzquierdo = hizq # Actualiza hijoDerecho
        self.hijoDerecho = hder # Actualiza hijoDerecho
        if self.tieneHijoIzquierdo(): # Si tiene hijo izquierdo
            self.hijoIzquierdo.padre = self # Actualiza el padra
        if self.tieneHijoDerecho(): # si tiene hijo derecho
            self.hijoDerecho.padre = self #acyualiza el padre

    def encontrarSucesor(self): # Define el método encontarSucesor
        suc = None # Crea la variable suc y la inicializa en None
        if self.tieneHijoDerecho(): # si tiene hijo derecho
            suc = self.hijoDerecho.encontrarMin() # Encuentra el mínimo en el subárbol derecho
        else: # Si el nodo no tiene un hijo derecho, el sucesor se debe buscar hacia arriba en el árbol.
            if self.padre: # Comprueba si el nodo tiene un padre. Si tiene un padre, se puede intentar encontrar el sucesor subiendo por el árbol
                if self.esHijoIzquierdo(): # i el nodo actual es el hijo izquierdo de su padre, entonces el sucesor será el propio padre. Esto se debe a que en un árbol binario de búsqueda, el sucesor de un nodo que es hijo izquierdo de su padre es precisamente el padre del nodo
                    suc = self.padre
                else: # Si el nodo no es el hijo izquierdo (es decir, es el hijo derecho de su padre), entonces el sucesor no es el padre directamente, sino que se necesita buscar más arriba.
                    self.padre.hijoDerecho = None # se elimina temporalmente la referencia al hijo derecho del nodo actual en el padre
                    suc = self.padre.encontrarSucesor() # Recursivamente busca el sucesor
                    self.padre.hijoDerecho = self # se restablece la referencia al hijo derecho del nodo actual en su padre
        return suc # Retorna suc

    def empalmar(self): # Define método empalmar
        if self.esHoja(): # Comprueba si el nodo actual es una hoja
            if self.esHijoIzquierdo(): # Si es el hijo izquierdo de su padre
                self.padre.hijoIzquierdo = None # El padre del nodo actual ya no tendrá un hijo izquierdo, por lo que se asigna None
            else: # Si el nodo no es el hijo izquierdo
                self.padre.hijoDerecho = None # el padre del nodo actual no tendrá un hijo derecho, así que se establece None
        elif self.tieneAlgunHijo(): # Si el nodo no es una hoja, pero tiene al menos un hijo
            if self.tieneHijoIzquierdo(): # Se comprueba si el nodo tiene un hijo izquierdo
                if self.esHijoIzquierdo(): # Si el nodo actual es el hijo izquierdo de su padre
                    self.padre.hijoIzquierdo = self.hijoIzquierdo # El padre del nodo actual ahora tendrá como hijo izquierdo al hijo izquierdo del nodo actual
                else: # Si el nodo actual no es el hijo izquierdo de su padre
                    self.padre.hijoDerecho = self.hijoIzquierdo # el padre del nodo actual reemplaza su referencia a hijoDerecho con el hijo izquierdo del nodo actual
                self.hijoIzquierdo.padre = self.padre # Independientemente de si el nodo es el hijo izquierdo o derecho, el hijo izquierdo (que ahora se conecta al padre) debe tener su referencia a padre actualizada para apuntar al padre del nodo actual
            else: # si tiene un hijo derecho
                if self.esHijoIzquierdo(): # Si el nodo es el hijo izquierdo de su padre, entonces el hijo derecho del nodo debe reemplazar al nodo en la referencia hijoIzquierdo de su padre
                    self.padre.hijoIzquierdo = self.hijoDerecho #  El padre del nodo actual ahora tendrá como hijo izquierdo al hijo derecho del nodo actual
                else: # Si el nodo no es el hijo izquierdo de su padre
                    self.padre.hijoDerecho = self.hijoDerecho # El padre del nodo actual ahora tendrá como hijo derecho al hijo derecho del nodo actual
                self.hijoDerecho.padre = self.padre #  Independientemente de si el nodo es el hijo izquierdo o derecho, el hijo derecho (que ahora se conecta al padre) debe tener su referencia a padre actualizada para apuntar al padre del nodo actual

    def encontrarMin(self): # Define el método
        actual = self # crea una variable y le Asigna el nodo actual self
        while actual.tieneHijoIzquierdo(): # Mientras el nodo actual tenga un hijo izquierdo, sigue
            actual = actual.hijoIzquierdo # Si el nodo actual tiene un hijo izquierdo, actualiza actual para que apunte a su hijo izquierdo
        return actual # Retorna el nodo actual

    def __iter__(self): # Define el método
        if self: # Si el nodo actual no es None
            if self.tieneHijoIzquierdo(): # Si el nodo tiene un hijo izquierdo, se procede a recorrer primero ese subárbol izquierdo
                for elem in self.hijoIzquierdo: # Si el nodo tiene un hijo izquierdo, se recorre recursivamente ese subárbol, usa __iter__ para que sea recursivo
                    yield elem # Por cada elemento que se recorre en el subárbol izquierdo, se "devuelve" ese valor
            yield self.clave # se devuelve la clave del nodo actual
            if self.tieneHijoDerecho(): # Si el nodo tiene un hijo derecho
                for elem in self.hijoDerecho: # se recurre al método __iter__ de forma recursiva en el hijo derecho
                    yield elem # Cada elemento del subarbol es devuelto a medida que se va recorriendo el arbpl