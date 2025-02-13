# Projeto de Reconhecimento de Matrículas

## Descrição

Este projeto é uma aplicação que utiliza técnicas de reconhecimento de matrícula para detectar a placa de veículos a partir de imagens, seja por câmeras ou de forma manual. Após detectar a matrícula, o sistema pode enviar essa informação por **Telegram** ou **Email** de acordo com a configuração definida no arquivo `config.json`.

### Funcionalidades:
- **Reconhecimento de Matrículas**: A aplicação utiliza uma câmera ou uma imagem fornecida para detectar a matrícula de veículos.
- **Envio de Notificações**: A matrícula detectada pode ser enviada automaticamente por **Telegram** ou **Email**.
- **Armazenamento em Banco de Dados**: A matrícula detectada pode ser salva em um banco de dados para posterior análise ou consulta.
- **Configuração Dinâmica**: O método de envio (Telegram ou Email) é configurável através de um arquivo `config.json`.

## Requisitos

Antes de executar o projeto, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```
## Dependências:

- `requests` – Para fazer requisições HTTP, especialmente para enviar mensagens via Telegram.
- `smtplib` – Para enviar e-mails via SMTP.
- `asyncio` – Para trabalhar com funções assíncronas, como o envio de mensagens no Telegram.
- `email.mime` – Para criar e-mails com cabeçalhos e corpo adequados.
- `sqlite3` – Para armazenar dados no banco de dados local (se aplicável).
- `opencv-python` – Para capturar imagens da câmera e processá-las (caso necessário).

## Arquivos principais:
- `config.json`: Contém todas as configurações do sistema, como o método de envio e informações do Telegram e Email.
- `main.py`: O script principal que controla o fluxo do programa, processando as matrículas detectadas e enviando notificações.
- `enviar_email.py`: Script responsável por enviar a matrícula detectada por e-mail.
- `enviar_telegram.py`: Script responsável por enviar a matrícula detectada via Telegram.

## Como Usar
#### 1. Configuração Inicial:

Antes de rodar o projeto, configure o arquivo `config.json` com as informações de envio de Telegram e Email.

#### Exemplo do arquivo `config.json`:
````bash
{
  "token": "SEU_TOKEN_AQUI",
  "metodo_envio": ["email", "telegram"],
  "chat_ids": ["123456789", "987654321"],
  "email": {
    "remetente": "seuemail@gmail.com",
    "senha": "sua_senha",
    "destinatarios": ["destinatario1@gmail.com", "destinatario2@gmail.com"]
  }
}
````

- `token`: O token do seu bot Telegram, obtido através do BotFather.
- `metodo_envio`: Um array que define quais métodos de envio serão usados. Os valores podem ser `"email"` e `"telegram"`.
- `chat_ids`: Array contendo os IDs dos chats de destino no Telegram.
- `email`: Configurações de envio de e-mail, incluindo remetente, senha e destinatários.
#### 2. Executando o Projeto:

Após configurar o `config.json`, execute o script principal para testar a detecção da matrícula e o envio das notificações:
````bash
python main.py
````
#### 3. Visualização dos Dados:

O projeto também pode salvar as matrículas detectadas em um banco de dados (SQLite, por exemplo). Para acessar ou visualizar os dados salvos, use qualquer cliente de SQLite ou ferramentas como DB Browser for SQLite.

## Funcionalidades Detalhadas
### 1. Reconhecimento de Matrículas:
O sistema utiliza um modelo de OCR (Reconhecimento Óptico de Caracteres) para processar imagens e identificar a matrícula de veículos. A aplicação captura a imagem da câmera ou lê uma imagem fornecida e extrai a matrícula.

### 2. Envio de Mensagens (Telegram e Email):
- **Telegram**: A mensagem com a matrícula é enviada para os IDs de chat fornecidos no arquivo `config.json`.
- **Email**: A matrícula é enviada para os e-mails fornecidos no `config.json`, usando o servidor SMTP (exemplo: Gmail).

## Exemplos de Execução
- Para enviar a matrícula detectada **por Telegram**: O bot enviará uma mensagem para os `chat_ids` configurados no arquivo `config.json`.

- Para enviar a matrícula por Email: O sistema enviará um e-mail para os destinatários configurados no `config.json`.

- Se o arquivo `config.json` incluir ambos os métodos, a matrícula será enviada tanto por **Telegram quanto por e-mail**.

## Personalizações
- **Alterar método de envio**: No arquivo `config.json`, altere o array `metodo_envio` para escolher o método que deseja usar. Você pode selecionar apenas um ou ambos (`"email"`, `"telegram"`).

- **Alterar configurações do Telegram**: O `token` e os `chat_ids` devem ser atualizados no `config.json` com os dados do seu bot Telegram e os IDs de chat para os quais você deseja enviar a mensagem.

- **Alterar configurações do E-mail**: Atualize as credenciais de e-mail e os destinatários no arquivo `config.json`.

## Contribuições
Se você deseja contribuir para o projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para a sua alteração (`git checkout -b feature/nova-funcionalidade`).
3. Faça as modificações necessárias.
4. Faça o commit das suas mudanças (`git commit -am 'Adicionando nova funcionalidade'`).
5. Envie para o repositório (`git push origin feature/nova-funcionalidade`).
6. Crie um pull request explicando as mudanças realizadas.
Licença
7. Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

