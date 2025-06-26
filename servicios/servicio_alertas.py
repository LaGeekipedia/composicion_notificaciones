class ServicioAlertas:
    def __init__(self, notificador):
        self.__notificador = notificador

    def enviar_alerta(self, mensaje):
        return self.__notificador.enviar(mensaje)
