import csv
import os


def fusionarArchivosCSV(lista_archivos_entrada: list[str], archivo_salida: str) -> None:
    """
    fusionarArchivosCSV recibe una lista con los nombres de los archivos a fusionar archivo (con el formato
    publicado de la linea 144) y genera un nuevo archivo en memoria con todos los contenidos de los archivos
    recien mencionados. No devuelve nada.
    """

    # Si el archivo ya existe, no se debe crear nada
    if os.path.exists(archivo_salida):
        return

    # Abrir el archivo de salida en modo de escritura
    with open(archivo_salida, "w", encoding="utf-8") as archivo_fusionado:
        # Bucle para procesar cada archivo de la lista de entrada
        for i, archivo in enumerate(lista_archivos_entrada):
            with open(archivo, "r", encoding="utf-8") as f:
                # Leer todas las líneas del archivo
                lineas = f.readlines()
                # Escribir las líneas en el archivo de salida
                if i == 0:
                    # Escribir todas las líneas, incluyendo la cabecera para el primer archivo
                    archivo_fusionado.writelines(lineas)
                else:
                    # Omitir la primera línea (cabecera) para los archivos subsiguientes
                    archivo_fusionado.writelines(lineas[1:])


def obtenerAnios(nombre_archivo: str) -> list[int]:
    """
    obtenerAnios es una funcion que recibe recibe el nombre de un archivo (con el formato
    publicado de la linea 144) y devuelve la lista de años que aparecen en el archivo
    """

    # Si el archivo no existe devuelve una lista vacia
    if not os.path.exists(nombre_archivo):
        return []

    with open(nombre_archivo, "r", encoding="utf-8-sig") as archivo:
        lector = csv.reader(archivo)
        anios = set()

        # Omitir el encabezado
        next(lector, None)

        for fila in lector:
            if fila:
                anios.add(int(fila[0][:4]))

        return list(anios)


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

    with open(nombre_archivo, encoding="utf-8") as archivo:
        anios = obtenerAnios(nombre_archivo)
        
        if len(anios) == 0 or anio not in anios:
            return None
        
        contar_provincias = {}
        lineas = archivo.readlines()
        
        for i, linea in enumerate(lineas):
            if linea != "\n" and i > 0:
                lista_lineas = linea.split(",")
                provincia = lista_lineas[1]

                provincia_existente = contar_provincias.get(provincia)

                if provincia_existente:
                    contar_provincias[provincia] += 1
                else:
                    contar_provincias[provincia] = 1

        print(contar_provincias)


lista_de_archivos = [
    "./datos/datosVG2020.csv",
    "./datos/datosVG2021.csv",
    "./datos/datosVG2022.csv",
]

crearEstadisticasAnualDesdeArchivo("./datos/datos_filtrados.csv", 2022)
