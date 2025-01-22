from flask import Flask, render_template, request, jsonify
from chatbot import bot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': "Please provide a message."}), 400
    bot_response = bot.get_response(user_message)
    return jsonify({'response': str(bot_response)})

if __name__ == "__main__":
    app.run(debug=True)