import requests
import json

def enviar_alerta_slack(mensagem, webhook_url):
    payload = {"text": mensagem}
    headers = {"Content-Type": "application/json"}

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("Alerta enviado para o Slack com sucesso.")
    else:
        print("Erro ao enviar alerta para o Slack:", response.text)

if __name__ == "__main__":
    webhook_url_slack = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    enviar_alerta_slack("Teste de alerta para o Slack", webhook_url_slack)

