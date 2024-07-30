from openai import OpenAI


client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="TheBloke/Llama-2-7B-GGUF",
  messages=[
    {"role": "system", "content": "Eres un asistente que responde preguntas sobre la salud mental."},
    {"role": "user", "content": "Que es el neurodesarrollo?"}
  ],
  temperature=0.7,
  max_tokens=500
)

print(completion.choices[0].message)

