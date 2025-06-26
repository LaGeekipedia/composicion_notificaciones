from sesion32.notificaciones.notificador import Notificador


class Push(Notificador):
    def __init__(self, dispositivo_id):
        self.__dispositivo_id = dispositivo_id

    def enviar(self, mensaje):
        return "Enviando notificación Push al dispositivo:", self.__dispositivo_id, "\nContenido del mensaje: ", mensaje
