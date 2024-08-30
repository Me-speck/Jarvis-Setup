nano app.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load models using Hugging Face Transformers
models = {
    "gpt2": pipeline('text-generation', model='gpt2'),
    "gpt-neo": pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B'),
    "gpt-j": pipeline('text-generation', model='EleutherAI/gpt-j-6B')
}

@app.route('/')
def home():
    return "Hello, I am Jarvis, the AI voice assistant from Iron Man. How may I be of use today?"

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    user_input = data.get('command')
    model_name = data.get('model', 'gpt2')  # Default to GPT-2 if no model is specified
    response = generate_response(user_input, model_name)
    return jsonify({"response": response})

def generate_response(prompt, model_name):
    model = models.get(model_name, models["gpt2"])  # Default to GPT-2 if the model name is not found
    results = model(prompt, max_length=150, num_return_sequences=1)
    return results[0]['generated_text']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
