# 🚀 WhatsApp GPT Application

Este projeto integra o ChatGPT com o WhatsApp para permitir respostas automatizadas e inteligentes, utilizando a API da OpenAI.

## 📋 Sumário

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Configuração e Execução](#configuração-e-execução)
- [Licença](#licença)

## 📖 Sobre

A **WhatsApp GPT Application** foi criada para oferecer uma maneira eficiente e inteligente de responder mensagens no WhatsApp automaticamente, utilizando a poderosa inteligência artificial do ChatGPT. É um exemplo perfeito de como a IA pode ser integrada em aplicações reais para facilitar o dia a dia.

## ✨ Funcionalidades

- Respostas automáticas e inteligentes baseadas no contexto da mensagem recebida.
- Integração fácil com o WhatsApp usando a API da OpenAI.
- Criação de túnel seguro para acesso ao servidor local via **ngrok**.
- Resposta customizadas ao abrir o arquivo zap.py e editar a linha do prompt

## 🛠 Tecnologias Utilizadas

- **Python** 🐍: Para desenvolver a lógica do servidor e integração com a API.
- **Flask** 🌐: Framework web para criar endpoints e gerenciar requisições HTTP.
- **ngrok**🟣: Para criar um túnel seguro e acessar o servidor local externamente.
- **OpenAI API** 🤖: Para gerar respostas inteligentes e naturais.
- **Twilio API** 📞: Para conectar e interagir com o WhatsApp. 

## 🚀 Configuração e Execução

### Pré-requisitos

- [Python 3.12+](https://www.python.org/downloads/)
- Conta e API Key na [OpenAI](https://platform.openai.com/)
- Conta na [Twilio](https://www.twilio.com/)
- [ngrok](https://ngrok.com/)

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/whatsapp-gpt-app.git

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt

3. Configure suas credenciais no arquivo .env.

4. Execute o NGROK para criar um túnel seguro:
    ```bash
    ngrok http 5000

5. Inicie o Servidor:
    ```bash
    python app.py

6. Conecte o webhook da Twilio ao URL do ngrok gerado

## Contato 💬 
Email: daniellucas0606@gmail.com
Linkedin: www.linkedin.com/in/daniel-lucas-214065195/
