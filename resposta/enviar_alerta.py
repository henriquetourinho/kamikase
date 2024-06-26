import smtplib
from email.mime.text import MIMEText
import json

def enviar_alerta(mensagem):
    with open('config/config.json') as config_file:
        config = json.load(config_file)

    msg = MIMEText(mensagem)
    msg['Subject'] = 'Alerta do Sistema Kamikaze'
    msg['From'] = config['email_from']
    msg['To'] = config['email_to']

    with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
        server.login(config['email_from'], config['email_password'])
        server.sendmail(config['email_from'], [config['email_to']], msg.as_string())

if __name__ == "__main__":
    enviar_alerta("Teste de alerta do Kamikaze.")

