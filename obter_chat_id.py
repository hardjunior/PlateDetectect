import json
import requests

# Função para ler as configurações do arquivo JSON
def ler_configuracoes():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

# Função para obter as atualizações e obter os chat_ids
def obter_chat_ids():
    # Carregar configurações do arquivo
    config = ler_configuracoes()
    TOKEN = config.get('token')  # Obtemos o token a partir da configuração
    if not TOKEN:
        print("Token não encontrado nas configurações.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {'offset': -1}
    response = requests.get(url, params=params)
    updates = response.json()

    chat_ids = []
    if 'result' in updates:
        for update in updates['result']:
            if 'message' in update:
                chat_id = update['message']['chat']['id']
                if chat_id not in chat_ids:
                    chat_ids.append(chat_id)

    # Verifique se foram encontrados chat_ids
    if chat_ids:
        config['chat_ids'] = chat_ids
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        print(f"Chat IDs obtidos e salvos com sucesso: {chat_ids}")
    else:
        print("Nenhum chat_id encontrado. Certifique-se de que o bot recebeu mensagens.")

if __name__ == "__main__":
    obter_chat_ids()
