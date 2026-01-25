from modelos.archivo_log import ArchivoLog


def registrar_evento(nombre_archivo, mensaje):
    # Creamos una instancia del modelo
    log = ArchivoLog(nombre_archivo)
    log.escribir(mensaje)
    print(f"[SERVICIO]: Evento '{mensaje}' registrado.")
    # Al salir de este método, el objeto 'log' se queda sin referencias
    # y es probable que el recolector de basura llame a __del__ pronto.


class GestorLog:
    def __init__(self):
        print("[SERVICIO]: Iniciando Gestor de Logs...")

