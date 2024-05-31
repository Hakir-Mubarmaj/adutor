from flask import Flask, request, jsonify
from flask_cors import CORS
from Amigo import responseA, appFunction

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/voice_assistant', methods=['POST'])
def voice_assistant():
    appFunction()
    return jsonify({"status": "success"})

@app.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    if question:
        answer = responseA(question, 1)
        return jsonify({"answer": answer})
    else:
        return jsonify({"answer": "No question provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
