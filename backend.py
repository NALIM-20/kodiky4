from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Vitaj v mojom Flask backende!"})


databaza = {
    "students": [
        {
            "id": 1,
            "name": "Adrian",
            "surname": "Cervenka",
            "nickname": "chilli pepper"
        },{
             "id": 2,
            "name": "Milan",
            "surname": "Kokina",
            "nickname": "tanecník"
        },{
             "id": 3,
            "name": "Martin",
            "surname": "Jelínek",
            "nickname": "král jelimán"
        },{
             "id": 4,
            "name": "Daniel",
            "surname": "Barta",
            "nickname": "skeleton"
        }
    ]
}

# 1. Hlavná stránka
@app.route('/')
def home():
    return jsonify({"message": "Vitaj v mojom Flask backende!"})

# 2. Zobrazenie všetkých študentov (/api)
@app.route('/api')
def get_all_students():
    return jsonify(databaza)

# 3. Vyhľadávanie podľa ID (/api/student/1)
@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    
    # Ak sa nenájde, vráti chybu
    return jsonify({"error": "Student not found"}), 404

# 4. Pridávanie nových dát (POST)
@app.route('/data', methods=['POST'])
def spracuj_data():
    vstup = request.get_json()
    if not vstup:
        return jsonify({"error": "Neposlal si žiadne dáta"}), 400
    
    return jsonify({
        "status": "úspech",
        "prijate_data": vstup
    }), 201

if __name__ == '__main__':
    app.run(debug=True)



