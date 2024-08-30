from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI with your API key
 import os
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/')
def home():
    return "hello I am Jarvis the voice ai asitant from iron man, how can I be of asistance?!"

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    user_input = data.get('command')
    response = chatgpt_response(user_input)
    return jsonify({"response": response})

def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Or "gpt-4" if available
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

