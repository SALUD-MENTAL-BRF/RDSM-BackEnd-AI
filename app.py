from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(data)

    try:
        completion = client.chat.completions.create(
            model="NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF",
            messages=[
                {"role": "system", "content": "Eres un asistente que responde preguntas sobre la salud mental, no respondas nada que no tenga que ver con la salud mental."},
                {"role": "user", "content": data["msg"]}
            ],
            temperature=0.7,
            max_tokens=500
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        answer = "Hubo un error al procesar tu solicitud."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

