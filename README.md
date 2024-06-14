# **Trabajo Práctico: Análisis de Datos de la línea 144**

## Introducción

La linea 144 brinda atención, contención y asesoramiento a personas en situación de violencia de género. Esta línea fue creada en 2013 para cumplir con la ley Nº 26.485 (más información en: <https://www.argentina.gob.ar/capital-humano/generos/linea-144>).

Se dispone de archivos de datos sobre las llamadas recibidas por este número. Cada registro representa una llamada e incluye información como la fecha, la provincia, el género de la persona que llama, su edad, su nacionalidad, entre otros datos. Los mismos pueden consultarse y descargarse en el sitio <https://www.datos.gob.ar/dataset/generos-base-datos-linea-144>. En el mismo sitio pueden consultarse los campos con sus tipos de datos y descripción.

En este Proyecto Final se trabajaran con los datos correspondientes a los años 2020 al 2022 (no incluiremos los datos del año 2023 por no estar completos).

## Objetivo del Proyecto final

El objetivo primordial de este Proyecto Final es que el alumno demuestre un empleo adecuado de los elementos y construcciones del lenguaje de programación. Para ello se trabajará con los datos disponibles resolviendo ciertas consignas que se le presentaran en 3 etapas.

A lo largo de tres semanas, trabajarán en la lectura, manipulación y análisis de estos datos, así como en la creación de clases y métodos para comparar y visualizar los resultados.

## Consignas Semana 1

1. Descargar los archivos `datosVG2020.csv`, `datosVG2021.csv` y `datosVG2022.csv` ejectundo el código que se le propone a continuación

```python
# No modificar este código que le permitirá bajar los archivos que necesita para trabajar

import requests
datosVG2020 = "https://datos-abiertos.mingeneros.gob.ar/datos/linea144-2020.csv"
datosVG2021 = "https://datos-abiertos.mingeneros.gob.ar/datos/linea144-2021.csv"
datosVG2022 = "https://datos-abiertos.mingeneros.gob.ar/datos/linea144-enero-diciembre-2022.csv"

def descargarCSV(url, archivo_salida):
    print("Descargando archivo...")
    consulta = requests.get(url)
    contenido = consulta.content

    print("Guardando archivo...")
    # Abrir conexion en modo escritura
    with open(archivo_salida, "w", encoding="utf-8-sig") as archivo:
        # Escribir el contenido de la consulta
        archivo.write(contenido.decode("utf-8-sig"))

    print("¡Archivo descargado con éxito!")

descargarCSV(datosVG2020, "datosVG2020.csv")
descargarCSV(datosVG2021, "datosVG2021.csv")
descargarCSV(datosVG2022, "datosVG2022.csv")
```

2. Escribir una función `fusionarArchivosCSV` que tomando una lista de nombres de archivos (con el formato publicado de la linea 144), genere un nuevo archivo con el mismo formato con los datos de los archivos anteriores exceptuando aquellos registros con `fecha` y/o `prov_residencia_persona_en_situacion_violencia` nulos.

3. Invocar a la función `fusionarArchivosCSV` con un lista con los nombres `datosVG2020.csv`, `datosVG2021.csv` y `datosVG2022.csv` y generar un nuevo archivo llamado `datos_filtrados.csv`

4. Escribir una función _obtenerAnios_ que reciba el nombre de un archivo (con el formato publicado de la linea 144) y devuelva la lista de años que aparecen en el archivo.

5. Escribir una función _crearEstadisticasAnualDesdeArchivo_ que reciba el nombre de un archivo (con el formato publicado de la linea 144) y devuelva:
   - un diccionario donde las claves sean las provincias argentinas desde donde se realizaron llamadas ese año a la linea 144 y los valores son la cantidad de llamadas que recibió cada provincia en dicho año, y
   - el promedio de edades de las personas que llamaron a esa línea durante todo el año (como valor entero)

## Consignas Semana 2

6. Definir una clase EstadisticasAnual con los siguientes atributos:

   - `anio`: año asociado a la clase,
   - `cant_llamadas_por_provincia`: diccionario donde las claves son las provincias argentinas desde donde se realizaron llamadas el año `anio` a la linea 144 y los valores son la cantidad de llamadas que recibió cada provincia en dicho año
   - `promedio_edades`: que es el promedio de edades de las personas que llamaron a esa linea durante el año anio (como valor entero)

   y los siguientes métodos:

   - `__init__`
   - `get_anio`
   - `get_cant_llamadas_por_provincia`
   - `get_promedio_edad_llamantes`
   - `__str__`

```python
"""
La clase EstadisticasAnual se utilizará para mantener información sobre
estadísticas de Situaciones de Violencia en Argentina en un año en particular
"""

class EstadisticasAnual:
  def __init__(self, anio: int, cant_llamadas_por_provincia:dict[str,int], promedio_edad_llamantes: int):
    pass

  def getAnio(self) -> int:
    pass

  def getCantLlamadasPorProvincia(self) -> dict[str,int]:
    pass

  def getPromedioEdadLlamantes(self) -> int:
    pass

  def __str__(self)->str:
    pass
```

7. Escribir una función crearObjetosEstadisticasAnual que tome el nombre de un archivo y devuelva una lista de objetos de la clase `EstadisticasAnual`, donde cada objeto contiene información de cada año del cual se disponen datos en el archivo. Debe invocar a las funciones `obtenerAnios` y `crearEstadisticasAnualDesdeArchivo`.

8. Invocar a la función anterior con el nombre de archivo `datos_filtrados.csv`.

## Consignas Semana 3

9. Agregar el método `graficarLLamadasPorProvincia` a la clase `EstadisticasAnual` que muestre en un gráfico de barras la cantidad de llamadas que se hicieron en el año en cuestión desde cada provincia.

10. Realizar las gráficas para los años que se disponen de datos invocando a este método a partir de los objetos creados en el punto 8.

11. Definir una nueva clase `EstadisticasViolencia` con el atributo:

    - `estadisticasAnuales`lista de objetos de la clase `EstadisticasAnual`

    y los siguientes métodos:

    - `__init__`
    - `compararPromediosEdadesPorAnio`
    - `minimaEdadPromedio`
    - `compararGráficamenteDosAnios`
    - `__str__`

```python
"""
La clase EstadisticasViolencia se utilizará para mantener información sobre
estadísticas de Situaciones de Violencia en Argentina, para todos los años
que se disponga de datos
"""
class EstadisticasViolencia:
  def __init__(self, estadisticasAnuales: list[EstadisticasAnual]):
    pass

  def compararPromediosEdadesPorAnio(self):
    pass

  def minimaEdadPromedioyAnio(self):
    pass

  def compararGraficamenteDosAnios(self,anio1, anio2):
    pass

  def __str__(self):
    pass
```

12. Crear un objeto instanciando la clase `EstadisticasViolencia` que contenga los datos de todos los años disponibles.

13. Invocar a cada uno de los métodos de la clase con el objeto creado en el punto anterior. Compare gráficamente dos años de su elección.

## Agradecimientos

Agradecemos a todas las personas que han contribuido a este proyecto. [¡Ve nuestros contribuidores!](https://github.com/juan-saad/final-prog-1/contributors)
