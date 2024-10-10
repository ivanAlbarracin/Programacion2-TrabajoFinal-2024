Aquí tienes un borrador del archivo README para el proyecto:

---

# Proyecto Final de Programación 2

## Objetivo
Desarrollo de una plataforma de turismo nacional utilizando Django, aplicando conceptos aprendidos durante la materia como: 
- Árboles binarios
- Grafos
- Complejidad de algoritmos
- Estructuras de datos
- Programación orientada a objetos

## Objetivos específicos
- Implementación del algoritmo de Dijkstra para encontrar la ruta más corta entre dos ciudades.
- Carga de datos de las ciudades con información turística relevante.
- Utilización de árboles binarios de búsqueda (BST) para ordenar la lista de ciudades antes de pasar los datos al frontend.

## Instrucciones de instalación

1. Clonar el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplicar las migraciones:
    ```bash
    python manage.py migrate
    ```

5. Crear usuario y contraseña para el admin: 
    ```bash
    python manage.py createsuperuser
    ```

6. Iniciar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Acceder al administrador de Django en `http://localhost:8000/admin` para cargar las ciudades.

## Estructura del Proyecto

El proyecto sigue la estructura estándar de Django:

```
/gps_simulation/
    /routes/
        models.py   # Modelos del proyecto
        views.py    # Lógica de las vistas
        urls.py     # Rutas del proyecto
        templates/  # Templates HTML
    /static/
        css/        # Archivos de estilo
    settings.py     # Configuraciones del proyecto
```

## Funcionalidades Implementadas

- **Carga de ciudades**: Utilizando el administrador de Django, se puede ingresar información sobre las ciudades.
- **Carga de runtas**: Se permite cargar rutas entre ciudades, que representan las distancias entre ellas.
  
## Funcionalidades a Implementar

Los estudiantes deberán completar:
1. **Agregar información sobre las ciudades**: Moddificar el modelo de ciudades apra cargar información relevante para el turismo de la provincia
2. **Árboles Binarios de Búsqueda**: Implementar la lógica para ordenar las ciudades mediante un árbol binario de búsqueda antes de mostrar los datos al frontend.
3. **Algoritmo de Dijkstra**: Implementar desde cero el algoritmo para encontrar la ruta más corta entre dos ciudades. La entrada serán las ciudades cargadas previamente, y la salida, la ruta óptima y la distancia.

### Notas Importantes

- **Carga de datos**: Se realiza desde el administrador de Django, y los datos de las rutas deben cargarse después de registrar las ciudades.
- **Frontend**: Los docentes proporcionarán el diseño del frontend, los estudiantes deben centrarse en la lógica del backend.

## Testing

El proyecto utiliza las herramientas de testing de Django. Para ejecutar los tests:

```bash
python manage.py test
```

Asegúrate de que todas las pruebas pasen antes de realizar una entrega.

## Sugerencias para la Implementación

- Para **las rutas** (distancias entre ciudades), se recomienda usar diccionarios donde las claves sean las ciudades y los valores sean listas con las ciudades vecinas y la distancia entre ellas.
- Los estudiantes pueden usar listas de adyacencia o matrices de adyacencia según prefieran.
- Se sugiere seguir buenas prácticas de programación con comentarios claros en el código y manejo adecuado de excepciones.

## Criterios de Evaluación

1. Claridad y comentarios en el código.
2. Manejo de errores y excepciones.
3. Trabajo en equipo.
4. Implementación de tests unitarios.
5. Presentación oral del proyecto.
6. Preguntas teóricas sobre lo implementado.
7. **Punto extra**: Agregar funcionalidades adicionales más allá de lo requerido.


## Anexo

implementados ahora:
/ # Página de home
/shortest-route 
/admin