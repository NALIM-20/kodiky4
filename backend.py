from flask import Flask, jsonify
from flask_cors import CORS  # Umožňuje prepojenie s tvojím JavaScriptom

app = Flask(__name__)
CORS(app)  # Povolíme prístup z iných adries (kvôli bonusu)

# 1. Databáza študentov (10 záznamov s obrázkami z internetu)
databaza = {
    "students": [
        {"id": 1, "name": "Adrian", "surname": "Cervenka", "nickname": "chilli pepper", "image": "https://picsum.photos/id/1011/300/200"},
        {"id": 2, "name": "Milan", "surname": "Kokina", "nickname": "tanecník", "image": "https://picsum.photos/id/1012/300/200"},
        {"id": 3, "name": "Martin", "surname": "Jelínek", "nickname": "král jelimán", "image": "https://picsum.photos/id/1013/300/200"},
        {"id": 4, "name": "Daniel", "surname": "Barta", "nickname": "skeleton", "image": "https://picsum.photos/id/1014/300/200"},
        {"id": 5, "name": "Elena", "surname": "Kováčová", "nickname": "perla", "image": "https://picsum.photos/id/1015/300/200"},
        {"id": 6, "name": "Peter", "surname": "Sekerka", "nickname": "drevorubač", "image": "https://picsum.photos/id/1016/300/200"},
        {"id": 7, "name": "Jana", "surname": "Malá", "nickname": "včielka", "image": "https://picsum.photos/id/1018/300/200"},
        {"id": 8, "name": "Marek", "surname": "Sloboda", "nickname": "vták", "image": "https://picsum.photos/id/1019/300/200"},
        {"id": 9, "name": "Simona", "surname": "Vysoká", "nickname": "žirafa", "image": "https://picsum.photos/id/1020/300/200"},
        {"id": 10, "name": "Lukáš", "surname": "Novák", "nickname": "blesk", "image": "https://picsum.photos/id/1021/300/200"}
    ]
}

# 2. Route pre domovskú stránku (/)
@app.route('/')
def home():
    return jsonify({"message": "Vitaj v mojom prvom Flask backende!"})

# 3. Route pre všetkých študentov (/api)
@app.route('/api')
def get_all_students():
    # Vracia celé pole študentov
    return jsonify(databaza["students"])

# 4. Route pre jedného študenta podľa ID (/api/student/X)
@app.route('/api/student/<int:student_id>')
def get_student_by_id(student_id):
    # Prechádzame zoznam a hľadáme zhodné ID
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    
    # Ak sa ID nenájde, vráti chybu a kód 404
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)