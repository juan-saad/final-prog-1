import csv
import matplotlib.pyplot as plt

def fusionarArchivosCSV(lista_archivos_entrada: list[str], archivo_salida: str) -> None:
    """
    fusionarArchivosCSV recibe una lista con los nombres de los archivos a fusionar archivo (con el formato
    publicado de la linea 144) y genera un nuevo archivo en memoria con todos los contenidos de los archivos
    recien mencionados. No devuelve nada.
    """
    with open(archivo_salida, "w") as salida:
        for i, archivo in enumerate(lista_archivos_entrada):
            with open(archivo) as entrada:
                # si el indice es 0, copie todo el archivo, sino que me saltee la primer linea
                if i == 0:
                    salida.writelines(entrada.readlines())
                else:
                    salida.writelines(entrada.readlines()[1:])


def obtenerAnios(nombre_archivo: str) -> list[int]:
    """
    obtenerAnios es una funcion que recibe recibe el nombre de un archivo (con el formato
    publicado de la linea 144) y devuelve la lista de años que aparecen en el archivo
    """

    with open(nombre_archivo) as archivo:
        lineas = archivo.readlines()
        lista_anios = []

        for i, linea in enumerate(lineas):
            # obtengo el anio del archivo
            anio = linea.split(",")[0].split("-")[0]

            if linea != "\n" and i > 0 and anio not in lista_anios:
                lista_anios.append(anio)

        # transformo en entero los anios de la lista agregada
        lista_anios = map(lambda x: int(x), lista_anios)

        return list(lista_anios)


def crearEstadisticasAnualDesdeArchivo(
    nombre_archivo: str, anio: int
) -> tuple[dict[str, int], int] | None:
    """
    crearEstadisticasAnualDesdeArchivo recibe el nombre de un archivo (con el formato publicado de la linea 144)
    y un año y devuelve:
      - None si no hay datos de dicho año en el archivo
      - un diccionario contar_provincias: dict[str,int]
          donde las claves son las provincias argentinas desde donde se realizaron llamadas ese año
          a la linea 144 y los valores son la cantidad de llamadas que recibió cada provincia en dicho año,
        y promedio_edades: int
          que es el promedio de edades de las personas que llamaron a esa línea durante todo el año
    """
    anios = obtenerAnios(nombre_archivo)

    if len(anios) == 0 or anio not in anios:
        return None

    contar_provincias = {}
    promedios_edades = 0
    lista_edades = []

    with open(nombre_archivo, encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        # Omitir el encabezado
        next(lector, None)

        for fila in lector:
            if fila and int(fila[0][:4]) == anio:
                provincia = fila[1] if fila[1] != '' else 'Sin especificar'
                edad = fila[3]
                provincia_existente = contar_provincias.get(provincia)

                if provincia_existente:
                    contar_provincias[provincia] += 1
                else:
                    contar_provincias[provincia] = 1

                if edad:
                    lista_edades.append(int(edad))

        promedios_edades = sum(lista_edades) / len(lista_edades)
        return contar_provincias, promedios_edades


"""
La clase EstadisticasAnual se utilizará para mantener información sobre
estadísticas de Situaciones de Violencia en Argentina en un año en particular
"""


class EstadisticasAnual:
    def __init__(
        self,
        anio: int,
        cant_llamadas_por_provincia: dict[str, int],
        promedio_edad_llamantes: int,
    ):
        self._anio = anio
        self._cant_llamadas_por_provincia = cant_llamadas_por_provincia
        self._promedio_edad_llamantes = promedio_edad_llamantes

    def get_anio(self) -> int:
        return self._anio

    def get_cant_llamadas_por_provincia(self) -> dict[str, int]:
        return self._cant_llamadas_por_provincia

    def get_promedio_edad_llamantes(self) -> int:
        return self._promedio_edad_llamantes

    def graficarLLamadasPorProvincia(self):
        lista_x = list(self._cant_llamadas_por_provincia.keys())
        lista_y = list(self._cant_llamadas_por_provincia.values())
        plt.figure(figsize = (15,8))
        plt.title('Estadisticas anuales',fontsize=25)
        plt.bar(lista_x, lista_y)
        plt.xlabel('Provincias', fontsize=15)
        plt.ylabel('Cantidad de llamadas', fontsize=15)
        plt.xticks(rotation=90)
        plt.show()

    def __str__(self) -> str:
        return (
            f"Año: {self._anio}\n"
            f"\nCantidad de llamadas por provincia: {self._cant_llamadas_por_provincia}\n"
            f"\nPromedio de edad de los llamantes: {self._promedio_edad_llamantes}\n\n"
        )


def crearObjetosEstadisticasAnual(nombre_archivo: str) -> list[EstadisticasAnual]:
    anios = obtenerAnios(nombre_archivo)
    lista_estadistica_anual = []

    for anio in anios:
        resultado = crearEstadisticasAnualDesdeArchivo(nombre_archivo, anio)
        estadistica_anual = EstadisticasAnual(anio, resultado[0], resultado[1])
        lista_estadistica_anual.append(estadistica_anual)
        estadistica_anual.graficarLLamadasPorProvincia()

    return lista_estadistica_anual




"""
La clase EstadisticasViolencia se utilizará para mantener información sobre
estadísticas de Situaciones de Violencia en Argentina, para todos los años
que se disponga de datos
"""
class EstadisticasViolencia:
  def __init__(self, estadisticas_anuales: list[EstadisticasAnual]):
    self._estadisticas_anuales = estadisticas_anuales

  def comparar_promedios_edades_por_anio(self):
    self._estadisticas_anuales 

  def minima_edad_promedioyAnio(self):
    pass

  def comparar_graficamente_dos_anios(self,anio1, anio2):
    pass

  def __str__(self):
    pass


# -------------------- Proceso principal ---------------------
lista = [
    "./datos/datosVG2020.csv",
    "./datos/datosVG2021.csv",
    "./datos/datosVG2022.csv",
]
# fusionarArchivosCSV(lista, "./datos/datos_filtrados.csv")
# obtenerAnios("./datos/datos_filtrados.csv")
# crearEstadisticasAnualDesdeArchivo("./datos/datos_filtrados.csv", 2022)
crearObjetosEstadisticasAnual("./datos/datos_filtrados.csv")
