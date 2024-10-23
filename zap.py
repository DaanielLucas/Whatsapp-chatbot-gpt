import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Chave API da OpenAI
openai.api_key = 'Sua chave API'

def get_chatgpt_response(message):
    # Define o contexto para respostas mais curtas e amigáveis
    prompt = f"Responda de forma amigavel, respeitosa e terminando com alguma dúvida a mais?  a esta mensagem: {message}"
    
    #Envia a mensagem para o ChatGPT e obtém a resposta
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # Modelo do ChatGPT
        messages=[{"role": "user", "content": prompt}] # Mensagem do usuário com o contexto
    )

    # Retorna a resposta gerada
    return response['choices'][0]['message']['content']


@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # Obtendo a mensagem recebida via WhatsApp
    incoming_msg = request.form.get('Body', '').strip()

    # Obtendo a resposta do ChatGPT
    gpt_response = get_chatgpt_response(incoming_msg)


    # Criando a resposta via Twilio
    response = MessagingResponse()
    response.message(gpt_response)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)