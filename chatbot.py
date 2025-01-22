from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import nltk
from flask import Flask, request, jsonify, render_template

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the chatbot
bot = ChatBot(
    "chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="mysql+mysqlconnector://root:password@localhost/chatbot",
    logic_adapters=["chatterbot.logic.BestMatch"]
)

# Define the training data in the required format (list of tuples)
training_data = [
    #traning your data
    ("Is hostel Strict", "You have to follow rules which are instructed to you"),
    ("where is administrative block located", "near the gate ,opposite to the fish tank"),
    ("where is digital library located", "It is located inside college library"),
    ("How can I help you?", "I’m here to assist with any questions you have!"),
    ("What can I do for you today?", "Just let me know what you need, and I’ll do my best!"),
    ("How’s your day going?", "It’s been awesome, thanks for asking! How about you?"),
    ("Where are you from?", "I live in the cloud, so I’m from everywhere and nowhere at the same time!"),
    ("What’s your favorite color?", "I don’t have a favorite, but I think I’d love the color Indigo"),
    ("Do you have any hobbies?", "I enjoy chatting with people like you. That’s my favorite hobby!"),
    ("Can you help me with my homework?", "I’d be happy to help! But try you best to complete it"),
    ("Do you know about the college?", "Yes! I know lots about the college. What would you like to know?"),
    ("What programs do you offer?", "We offer a wide range of programs. Is there something specific you’re interested in? https://www.nirmalacollegeonline.ac.in/programoffered.php"),
    ("Can I apply online?", "Yes, you can apply directly through our website. It’s super easy! https://www.nirmalacollegeonline.ac.in/application.php"),
    ("What’s the campus like?", "It’s a great place! A mix of green spaces, modern buildings, and lots of friendly faces."),
    ("Do you have a library?", "Yes, we have a huge library with tons of books and study areas!")
]

# Train the chatbot using the ListTrainer
try:
    trainer = ListTrainer(bot)
    for pattern, response in training_data:
        trainer.train([pattern, response])
    print("Training completed successfully!")
except Exception as e:
    print("An error occurred:", e)

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_response = bot.get_response(user_input)
    return jsonify({"response": str(bot_response)})

if __name__ == "__main__":
    app.run(debug=True)
