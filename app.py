from flask import Flask, jsonify, request
from flask_cors import CORS
from activities.social_hability import activity_social_hability
from activities.logical_probleam import activity_logical_problem

app = Flask(__name__)
CORS(app)




@app.route('/hability-social', methods=['POST'])
def hability_social():
    data = request.get_json()
    try:
        answer = activity_social_hability(data)
    except Exception as e:
        print(f"Error: {e}")
        answer = "Hubo un error al procesar tu solicitud"

    return jsonify({"answer": answer})

@app.route('/logical-problem', methods=['POST'])
def logical_problem():
    data = request.get_json()

    try:
        answer = activity_logical_problem(data)
    except Exception as e:
        print(f"Error: {e}")
        answer =  "Hubo un error al procesar tu solicitud"
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

    
