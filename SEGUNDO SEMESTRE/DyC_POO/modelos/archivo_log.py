
class ArchivoLog:
    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR: Inicializa el estado del objeto.
        - Abre el archivo en modo 'append' (añadir).
        - Si el archivo no existe, lo crea.
        - Se ejecuta automáticamente al instanciar la clase.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, "a")
        print(f"[CONSTRUCTOR]: Conexión establecida con '{self.nombre_archivo}'.")

    def escribir(self, mensaje):
        self.archivo.write(mensaje + "\n")

    def __del__(self):
        """
        DESTRUCTOR: Realiza la limpieza de recursos.
        - Cierra el flujo del archivo para evitar fugas de memoria o archivos bloqueados.
        - Se ejecuta cuando el objeto ya no tiene referencias o el programa finaliza.
        """
        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()
            print(f"[DESTRUCTOR]: El archivo '{self.nombre_archivo}' ha sido cerrado correctamente.")