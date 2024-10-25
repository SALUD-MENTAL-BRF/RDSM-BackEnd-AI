from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente que genera simulaciones de conversaciones para mejorar habilidades sociales en diferentes escenarios."),
    ("user", "{question}")
])

model = OllamaLLM(model="llama3.2:3b-instruct-q8_0")

chain = prompt | model


def activity_social_hability(genre, stage):
    respuesta = chain.invoke({
        "question": f"""
        Crea un escenario social simple acorde a mi edad de 18 años, en el cual estoy en {stage} y soy de género {genre}. 
        Genera **tres respuestas posibles**: una debe ser correcta y las otras dos incorrectas. 
        Es **crucial** que incluyas todas las respuestas y que sigas estrictamente esta estructura:

        - Escenario: "Descripción clara del escenario."
        - Respuestas:
          1) "Primera respuesta incorrecta."
          2) "Respuesta correcta."
          3) "Segunda respuesta incorrecta."
        - Correcta: INDICA EL NÚMERO DE LA RESPUESTA CORRECTA (1, 2 o 3).

        **Ejemplo de formato correcto:**
        Escenario: "Estás en una reunión de trabajo y tu jefe te pide que presentes un informe."
        Respuestas:
        1) "Te disculpas y dices que no tienes el informe listo."
        2) "Presentas el informe tal como te lo han pedido."
        3) "Dices que otra persona se encargará de la presentación."
        Correcta: 2

        **Asegúrate de que el formato sea muy claro y que no haya variaciones en la estructura.** 
        """
    })

    return respuesta
