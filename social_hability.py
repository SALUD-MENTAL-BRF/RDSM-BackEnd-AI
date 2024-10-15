from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """
                Eres un asistente que genera simulaciones de conversaciones para que los usuarios puedan practicar habilidades sociales. 
                Crea un escenario social donde el usuario debe responder de manera adecuada. Incluye tres posibles respuestas, y marca la correcta.
                El formato debe ser el siguiente:
                    {
                        "texto": "<Texto de la conversación>",
                        "opciones": [
                            "1. <Opción de respuesta 1>",
                            "2. <Opción de respuesta 2>",
                            "3. <Opción de respuesta 3>"
                        ],
                        "respuestaCorrecta": "<Número de la opción correcta>"
                    }
                El escenario debe ser claro, con interacciones sociales realistas y relevantes para el contexto dado. Asegúrate de incluir temas como:
                - Saludos y primeras impresiones
                - Conversaciones en el trabajo
                - Cómo lidiar con conflictos
                - Cómo iniciar y mantener conversaciones informales
                - Responder a preguntas difíciles de manera educada
            """

prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente que genera simulaciones de conversaciones para mejorar habilidades sociales en diferentes escenarios."),
    ("user", "{question}")
])

model = OllamaLLM(model="llama3.2:3b")

chain = prompt | model


def activity_social_hability(genre, stage):
    respuesta = chain.invoke({"question": f"""
                    Crea una simulación de conversación en la que un usuario se encuentra en {stage} por primera vez. 
                    Proporciona 3 posibles formas de responder y una respuesta correcta. Ten en cuenta que el genero del usuario es {genre}.
                """})

    return respuesta