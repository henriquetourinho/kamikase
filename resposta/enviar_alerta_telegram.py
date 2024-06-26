from telegram import Bot

def enviar_alerta_telegram(mensagem, bot_token, chat_id):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=mensagem)

if __name__ == "__main__":
    bot_token_telegram = "SEU_TOKEN_DE_BOT"
    chat_id_telegram = "SEU_CHAT_ID"
    enviar_alerta_telegram("Teste de alerta para o Telegram", bot_token_telegram, chat_id_telegram)

