from langchain_core.prompts import ChatPromptTemplate
from config.connectAI import model


prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente que genera problemas con resoluciones logicas."),
    ("user", "{question}")
])

chain = prompt | model


def activity_logical_problem(data):
    respuesta = chain.invoke({
        "question": f"""
        Crea un problema {data["complexity"]}. 
        Genera **tres respuestas posibles**: una debe ser correcta y las otras dos incorrectas. 
        Es **crucial** que incluyas todas las respuestas y que sigas estrictamente esta estructura:

        - Problema: "Descripción clara del problema."
        - Respuestas:
          1) "Primera respuesta incorrecta."
          2) "Respuesta correcta."
          3) "Segunda respuesta incorrecta."
        - Correcta: INDICA EL NÚMERO DE LA RESPUESTA CORRECTA (1, 2 o 3).
        - Explicación: "Explica por qué esta es la opción correcta en una o dos frases."

        **Ejemplo de formato correcto:**
        Problema: "En un rompecabezas, tienes tres llaves, pero solo una abre la puerta. ¿Cuál usas?"
        Respuestas:
        1) "La llave plateada."
        2) "La llave dorada."
        3) "La llave de bronce."
        Correcta: 2
        Explicación: "La opción 2 es correcta porque es la única llave que abre la puerta según la descripción del problema."


        **Asegúrate de que el formato sea muy claro y que no haya variaciones en la estructura.** 
        """
    })
    

    return respuesta.content if hasattr(respuesta, 'content') else str(respuesta)