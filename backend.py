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

@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


@app.route('/api')
def api():
    return jsonify(databaza)

@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    student = databaza["students"][student_id - 1]
    return jsonify(student)





















# 3. POST požiadavka (odosielanie dát na server)
@app.route('/data', methods=['POST'])
def spracuj_data():
    vstup = request.get_json() # Získame JSON dáta od klienta
    
    if not vstup:
        return jsonify({"error": "Neposlal si žiadne dáta"}), 400
    
    return jsonify({
        "status": "úspech",
        "prijate_data": vstup
    }), 201

if __name__ == '__main__':
    app.run(debug=True) 