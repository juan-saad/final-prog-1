import csv


def fusionarArchivosCSV(lista_archivos_entrada: list[str], archivo_salida: str) -> None:
    """
    fusionarArchivosCSV recibe una lista con los nombres de los archivos a fusionar archivo (con el formato
    publicado de la linea 144) y genera un nuevo archivo en memoria con todos los contenidos de los archivos
    recien mencionados. No devuelve nada.
    """
    with open(archivo_salida, 'w') as salida:
        for i,archivo in enumerate(lista_archivos_entrada):
            with open(archivo) as entrada:
                #si el indice es 0, copie todo el archivo, sino que me saltee la primer linea
                if(i == 0):  
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
        for i,linea in enumerate(lineas):
            #obtengo el anio del archivo
            anio = linea.split(",")[0].split('-')[0]
            if(linea != '\n' and i > 0 and anio not in lista_anios):
                lista_anios.append(anio)
        #transformo en entero los anios de la lista agregada
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

    with open(nombre_archivo) as archivo:
        anios = obtenerAnios(nombre_archivo)
        if (len(anios) == 0 or anio not in anios):
            return None        
        contar_provincias = {} 
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas):
            if(linea != '\n' and i > 0):
                lista_lineas = linea.split(",")
                provincia = lista_lineas[1]
                
                provincia_existente = contar_provincias.get(provincia)
                
                if provincia_existente:
                    contar_provincias[provincia] += 1
                else:
                    contar_provincias[provincia] = 1
                    
        print(contar_provincias)

lista = ["./datos/datosVG2020.csv","./datos/datosVG2021.csv","./datos/datosVG2022.csv"]
fusionarArchivosCSV(lista,"./datos/datos_filtrados.csv")
obtenerAnios("./datos/datos_filtrados.csv")
crearEstadisticasAnualDesdeArchivo("./datos/datos_filtrados.csv", 2022)