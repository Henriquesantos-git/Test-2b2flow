import os
import requests
import logging
from dotenv import load_dotenv
from supabase import create_client

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Carrega variáveis do .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


def buscar_contatos():
    """Busca todos os contatos do Supabase."""
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        response = supabase.table("contatos").select("*").execute()
        logging.info(f"{len(response.data)} contato(s) encontrado(s) no banco.")
        return response.data
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        return []


def enviar_mensagem(telefone, nome):
    """Envia mensagem via Z-API para um contato."""
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN
    }
    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            logging.info(f"Mensagem enviada para {nome} ({telefone}) ✅")
        else:
            logging.warning(f"Falha ao enviar para {nome} ({telefone}): {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem para {nome}: {e}")


def main():
    logging.info("Iniciando envio de mensagens...")
    contatos = buscar_contatos()

    if not contatos:
        logging.warning("Nenhum contato encontrado. Encerrando.")
        return

    for contato in contatos:
        enviar_mensagem(contato["telefone"], contato["nome"])

    logging.info("Processo finalizado.")


if __name__ == "__main__":
    main()