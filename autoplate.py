import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio
import json
import sqlite3
from telegram import Bot
from datetime import datetime

# Função para ler configurações do arquivo JSON
def ler_configuracoes():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

# Função assíncrona para enviar mensagem pelo Telegram
async def enviar_mensagem_telegram(mensagem, chat_id, token):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=mensagem)

# Função para enviar email
def enviar_email(matricula, configuracao_email):
    remetente = configuracao_email['remetente']
    senha = configuracao_email['senha']
    destinatarios = configuracao_email['destinatarios']

    # Criando a mensagem
    assunto = "Matrícula detectada"
    corpo = f"A matrícula do veículo detectado é: {matricula}"

    try:
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain'))

        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        texto = msg.as_string()

        # Enviar a mensagem para todos os destinatários na lista
        for destinatario in destinatarios:
            msg['To'] = destinatario  # Atribui o destinatário antes de enviar
            servidor.sendmail(remetente, destinatario, texto)
        
        servidor.quit()
        print("Email enviado com sucesso")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Função para registrar no banco de dados
def registrar_matricula_bd(matricula, metodo_envio):
    try:
        # Conectar ao banco de dados SQLite (o arquivo será criado se não existir)
        conn = sqlite3.connect('matriculas.db')
        cursor = conn.cursor()

        # Criar a tabela se ela não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL,
                metodo_envio TEXT NOT NULL,
                data_envio TEXT NOT NULL
            )
        ''')

        # Inserir o registro no banco de dados
        data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO registros (matricula, metodo_envio, data_envio)
            VALUES (?, ?, ?)
        ''', (matricula, metodo_envio, data_envio))

        # Commit e fechar conexão
        conn.commit()
        conn.close()
        print("Registro inserido no banco de dados com sucesso.")
    except Exception as e:
        print(f"Erro ao registrar no banco de dados: {e}")

# Função para decidir qual método de envio usar
def enviar_matricula(matricula):
    # Carregar as configurações do arquivo JSON
    config = ler_configuracoes()

    metodo_envio = config["metodo_envio"]  # Agora metodo_envio pode ser uma lista
    token = config["token"]
    chat_ids = config["chat_ids"]

    # Verificar se o método de envio é "telegram"
    if "telegram" in metodo_envio and chat_ids:
        mensagem = f"A matrícula do veículo detectado é: {matricula}"
        
        # Usar asyncio para aguardar a função assíncrona de envio do Telegram
        loop = asyncio.get_event_loop()
        # Enviar a mensagem para todos os chat_ids no array
        for chat_id in chat_ids:
            loop.run_until_complete(enviar_mensagem_telegram(mensagem, chat_id, token))

        # Registrar no banco de dados
        registrar_matricula_bd(matricula, "telegram")

    # Verificar se o método de envio é "email"
    if "email" in metodo_envio:
        configuracao_email = config["email"]
        enviar_email(matricula, configuracao_email)

        # Registrar no banco de dados
        registrar_matricula_bd(matricula, "email")

# Exemplo de uso
if __name__ == "__main__":
    matricula_detectada = "ABC1234"
    # Enviar a matrícula com base no método definido no arquivo config.json
    enviar_matricula(matricula_detectada)
