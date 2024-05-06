from telegram.ext import Updater, MessageHandler, Filters
import time

# Función para manejar los mensajes
def message_handler(update, context):
    message = update.message
    chat_id = message.chat_id
    text = message.text
    chat_type = message.chat.type
    date = message.date

    # Aquí puedes definir tu patrón de mensaje específico
    # Por ejemplo, si quieres buscar mensajes que contienen la palabra "hola"
    if "hola" in text.lower():
        alert_message = f"Mensaje encontrado en {chat_type} '{chat_id}' a las {date}: {text}"
        print(alert_message)
        # Aquí puedes agregar tu propia lógica de alerta, por ejemplo, enviar una notificación

def main():
    # Token de tu bot de Telegram
    updater = Updater("TOKEN")

    # Manejador para los mensajes
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    # Iniciar el bot
    updater.start_polling()

    # Verificar los mensajes cada 15 minutos
    while True:
        time.sleep(900)  # 900 segundos = 15 minutos
        # Aquí puedes agregar lógica para verificar nuevos mensajes

if __name__ == "__main__":
    main()
