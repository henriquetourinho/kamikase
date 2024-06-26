# Kamikaze

## Descrição

Kamikaze é um sistema de monitoramento de servidor que detecta problemas críticos e toma ações automáticas para corrigir ou mitigar esses problemas.

## Estrutura do Projeto

- `monitoramento/`: Scripts para monitoramento de recursos e serviços.
- `resposta/`: Scripts para ações de resposta como reiniciar serviços e enviar alertas.
- `config/`: Arquivo de configuração.
- `main.py`: Script principal que coordena as verificações e respostas.

## Como Usar

1. Configure o arquivo `config/config.json` com suas informações de email, Slack e Telegram.
2. Execute o script principal:
    ```sh
    python3 main.py
    ```

