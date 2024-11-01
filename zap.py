import openai
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Carregue sua chave de API da OpenAI de uma variável de ambiente
openai.api_key = "SUA-CHAVE-API"

def get_chatgpt_response(prompt):
    # Ajuste a mensagem de forma amigável e interativa
    prompt = f"Responda de forma amigável, respeitosa e termine com uma pergunta sobre a mensagem: {prompt}"
    try:
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        # A resposta agora é acessada através do dict response, verifique sua estrutura correta
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Erro na chamada de API: {e}")
        return "Desculpe, não consegui processar sua solicitação no momento."

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get('Body', '').strip()
    gpt_response = get_chatgpt_response(incoming_msg)
    response = MessagingResponse()
    response.message(gpt_response)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
