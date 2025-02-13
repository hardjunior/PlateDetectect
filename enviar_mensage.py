import json
import asyncio
from telegram import Bot

# Função para ler configurações do JSON
def ler_configuracoes():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

# Função assíncrona para enviar a mensagem no Telegram
async def enviar_mensagem_telegram(mensagem, chat_id, token):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=mensagem)

# Função para enviar mensagem de teste
def enviar_mensagem_teste():
    config = ler_configuracoes()

    if 'chat_ids' in config and len(config['chat_ids']) > 0:
        chat_id = config['chat_ids'][0]  # Enviar para o primeiro chat_id
        token = config['token']
        mensagem = "Esta é uma mensagem de teste do seu bot!"

        # Usar asyncio para aguardar a função assíncrona
        loop = asyncio.get_event_loop()
        loop.run_until_complete(enviar_mensagem_telegram(mensagem, chat_id, token))
        
        print("Mensagem enviada com sucesso!")
    else:
        print("Nenhum chat_id encontrado.")

if __name__ == "__main__":
    enviar_mensagem_teste()
