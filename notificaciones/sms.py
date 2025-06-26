from sesion32.notificaciones.notificador import Notificador


# SMS significa Servicio de Mensajes Cortos(Short Message Service)
class SMS(Notificador):
    def __init__(self, numero_telefono):
        self.__numero_telefono = numero_telefono

    def enviar(self, mensaje):
        return "Enviando SMS al número:", self.__numero_telefono, "\nContenido del mensaje: ", mensaje
