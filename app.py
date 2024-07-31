from openai import OpenAI
from flask import Flask, jsonify, request


client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")



app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():

  data = request.get_json()


  completion = client.chat.completions.create(
    model="NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF",
    messages=[
      {"role": "system", "content": "Eres un asistente que responde preguntas sobre la salud mental."},
      {"role": "user", "content": data["msg"]}
    ],
    temperature=0.7,
    max_tokens=500
  )

  return jsonify({"answer":completion.choices[0].message.content})


if __name__ == "__main__":
  app.run(debug=True)




