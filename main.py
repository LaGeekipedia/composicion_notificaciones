from notificaciones.email import Email
from notificaciones.sms import SMS
from notificaciones.push import Push
from servicios.servicio_alertas import ServicioAlertas

def main():
    notificador_email = Email("fulanito@ejemplo.com")
    notificador_sms = SMS("555-123-4567")
    notificador_push = Push("dispositivo_987")

    mensaje = "¡Este es un mensaje de alerta!"

    alertas = [
        ServicioAlertas(notificador_email),
        ServicioAlertas(notificador_sms),
        ServicioAlertas(notificador_push)
    ]

    for alerta in alertas:
        print(alerta.enviar_alerta(mensaje))
        print("-" * 40)


if __name__ == "__main__":
    main()
