from flask import Flask, jsonify, request
from flask_cors import CORS
from activities.social_hability import activity_social_hability

app = Flask(__name__)
CORS(app)




@app.route('/hability-social', methods=['POST'])
def hability_social():
    data = request.get_json()
    try:
        answer = activity_social_hability(data["age"],data["genre"], data["stage"], data["complexity"], data["personality"])
    except Exception as e:
        print(f"Error: {e}")
        answer = "Hubo un error al procesar tu solicitud"

    return jsonify({"answer": answer})

# @app.route('/logical-problem', methods='POST')
# def logical_problem():

if __name__ == "__main__":
    app.run(debug=True)

    
