from sesion32.notificaciones.notificador import Notificador


class Email(Notificador):
    def __init__(self, correo_destino):
        self.__correo_destino = correo_destino

    def enviar(self, mensaje):
        return "Enviando correo a:", self.__correo_destino, "\nContenido del mensaje: ", mensaje
