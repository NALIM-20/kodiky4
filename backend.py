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

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Vitaj v mojom Flask backende!"})

# 1. Zobrazenie celej databázy
@app.route('/api', methods=['GET'])
def api():
    return jsonify(databaza)

# 2. Vyhľadávanie študenta podľa ID pomocou FOR cyklu
@app.route('/api/student/<int:student_id>', methods=['GET'])
def find_student(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    
    # Ak po prejdení celého cyklu nenájde zhodu
    return jsonify({"error": f"Student s ID {student_id} nebol najdený"}), 404

# 3. POST požiadavka - Pridanie nového študenta do zoznamu
@app.route('/api/student', methods=['POST'])
def pridaj_studenta():
    novy_student = request.get_json()
    
    if not novy_student:
        return jsonify({"error": "Neposlal si žiadne dáta"}), 400

    # Pridáme študenta do nášho zoznamu
    databaza["students"].append(novy_student)
    
    return jsonify({
        "message": "Študent úspešne pridaný!",
        "prijate_data": novy_student
    }), 201

if __name__ == '__main__':
    app.run(debug=True)




