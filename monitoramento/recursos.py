import psutil
import json

def verificar_recursos():
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_memoria = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent

    return {
        "cpu": uso_cpu,
        "memoria": uso_memoria,
        "disco": uso_disco
    }

if __name__ == "__main__":
    recursos = verificar_recursos()
    print(json.dumps(recursos, indent=4))

