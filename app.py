from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bot_response(message):
    message = message.lower()
    if message == "hello":
        return "Hello "
    elif message == "who are you":
        return "I am a Python website bot"
    elif message == "cyber security":
        return "Cyber security is protecting systems from attacks"
    else:
        return "I don't understand"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["msg"]
    return jsonify({"response": bot_response(user_message)})

if __name__ == "__main__":
    app.run(debug=True)
