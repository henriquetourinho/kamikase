import monitoramento.recursos as recursos
import subprocess
import json
import resposta.enviar_alerta as alerta_email
import resposta.enviar_alerta_slack as alerta_slack
import resposta.enviar_alerta_telegram as alerta_telegram

def carregar_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)

def main():
    config = carregar_config()
    status_recursos = recursos.verificar_recursos()

    if status_recursos['cpu'] > 80:
        subprocess.run(['./resposta/reiniciar_servicos.sh'])

        mensagem_alerta = "Uso de CPU acima de 80%. Serviços reiniciados."
        
        # Enviar alerta por email
        alerta_email.enviar_alerta(mensagem_alerta)
        
        # Enviar alerta para o Slack
        alerta_slack.enviar_alerta_slack(mensagem_alerta, config['slack_webhook_url'])

        # Enviar alerta para o Telegram
        alerta_telegram.enviar_alerta_telegram(mensagem_alerta, config['telegram_bot_token'], config['telegram_chat_id'])

if __name__ == "__main__":
    main()

