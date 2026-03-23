from flask import Flask, jsonify, request

app = Flask(__name__)

# Tvoja databáza
databaza = [
    {"id": 1, "name": "Adrian", "surname": "Cervenka", "nickname": "chilli pepper", "image": "https://picsum.photos/id/10/200"},
    {"id": 2, "name": "Milan", "surname": "Kokina", "nickname": "tanecník", "image": "https://picsum.photos/id/20/200"},
    {"id": 3, "name": "Martin", "surname": "Jelínek", "nickname": "král jelimán", "image": "https://picsum.photos/id/30/200"},
    {"id": 4, "name": "Daniel", "surname": "Barta", "nickname": "skeleton", "image": "https://picsum.photos/id/40/200"},
    {"id": 5, "name": "Jana", "surname": "Veselá", "nickname": "slniečko", "image": "https://picsum.photos/id/50/200"},
    {"id": 6, "name": "Peter", "surname": "Horský", "nickname": "vlk", "image": "https://picsum.photos/id/60/200"},
    {"id": 7, "name": "Lucia", "surname": "Biela", "nickname": "snežienka", "image": "https://picsum.photos/id/70/200"},
    {"id": 8, "name": "Marek", "surname": "Tichý", "nickname": "duch", "image": "https://picsum.photos/id/80/200"},
    {"id": 9, "name": "Simona", "surname": "Rýchla", "nickname": "raketa", "image": "https://picsum.photos/id/90/200"},
    {"id": 10, "name": "Jakub", "surname": "Kováč", "nickname": "kladivo", "image": "https://picsum.photos/id/100/200"}
]



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
