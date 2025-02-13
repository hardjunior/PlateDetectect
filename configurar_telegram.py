import json

# Função para configurar o arquivo JSON com o token e outros parâmetros
def configurar_bot():
    token = input("Digite o token do seu bot Telegram: ")
    metodo_envio = input("Escolha o método de envio (telegram/email): ").lower()

    # Estrutura inicial do JSON
    configuracoes = {
        "token": token,
        "metodo_envio": metodo_envio,
        "chat_ids": []
    }

    # Salvar as configurações no arquivo JSON
    with open('config.json', 'w') as f:
        json.dump(configuracoes, f, indent=4)

    print("Configuração salva com sucesso!")

if __name__ == "__main__":
    configurar_bot()
