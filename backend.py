from flask import Flask, jsonify, request

app = Flask(__name__)

# Tvoja databáza
databaza = {
    "students": [
        {"id": 1, "name": "Adrian", "surname": "Cervenka", "nickname": "chilli pepper"},
        {"id": 2, "name": "Milan", "surname": "Kokina", "nickname": "tanecník"},
        {"id": 3, "name": "Martin", "surname": "Jelínek", "nickname": "král jelimán"},
        {"id": 4, "name": "Daniel", "surname": "Barta", "nickname": "skeleton"}
    ]
}

# Hlavná stránka - názov funkcie: home
@app.route('/')
def home():
    return jsonify({"message": "Vitaj v mojom Flask backende!"})

# Zobrazenie všetkých - názov funkcie: get_api
@app.route('/api')
def get_api():
    return jsonify(databaza)

# Vyhľadávanie podľa ID - názov funkcie: get_student_by_id
@app.route('/api/student/<int:student_id>')
def get_student_by_id(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Študent sa nenašiel"}), 404

# POST endpoint na dáta - názov funkcie: post_data
@app.route('/data', methods=['POST'])
def post_data():
    vstup = request.get_json()
    if not vstup:
        return jsonify({"error": "Žiadne dáta"}), 400
    return jsonify({"status": "prijaté", "data": vstup}), 201

if __name__ == '__main__':
    # Spustenie servera
    app.run(debug=True)
    