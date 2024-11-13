from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=os.getenv("API_GEMINIAI_KEY"))



prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente que genera simulaciones de conversaciones para mejorar habilidades sociales en diferentes escenarios."),
    ("user", "{question}")
])

chain = prompt | model


def activity_social_hability(age, genre, stage, complexity, personality):
    respuesta = chain.invoke({
        "question": f"""
        Crea un escenario social {complexity} acorde a mi edad de {age} años, en el cual estoy en {stage}, soy de género {genre} y personalidad es {personality}. 
        Genera **tres respuestas posibles**: una debe ser correcta y las otras dos incorrectas. 
        Es **crucial** que incluyas todas las respuestas y que sigas estrictamente esta estructura:

        - Escenario: "Descripción clara del escenario."
        - Respuestas:
          1) "Primera respuesta incorrecta."
          2) "Respuesta correcta."
          3) "Segunda respuesta incorrecta."
        - Correcta: INDICA EL NÚMERO DE LA RESPUESTA CORRECTA (1, 2 o 3).
        - Explicación: "Explica por qué esta es la opción correcta en una o dos frases."

        **Ejemplo de formato correcto:**
        Escenario: "Estás en una reunión de trabajo y tu jefe te pide que presentes un informe."
        Respuestas:
        1) "Te disculpas y dices que no tienes el informe listo."
        2) "Presentas el informe tal como te lo han pedido."
        3) "Dices que otra persona se encargará de la presentación."
        Correcta: 2
        Explicación: "La opción 2 es correcta porque muestra responsabilidad y respeto hacia tu jefe al estar preparado."

        **Asegúrate de que el formato sea muy claro y que no haya variaciones en la estructura.** 
        """
    })
    

    return respuesta.content if hasattr(respuesta, 'content') else str(respuesta)

