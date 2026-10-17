# Создать Flask-приложение
# В app.py создайте Flask-приложение и добавьте маршрут /, который возвращает сообщение:My Collection API
# Запустите приложение и откройте http://127.0.0.1:5000/.

from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {
        'id': 1, 'name': 'Титаник', 'genre': 'мелодрама', 'year': 1997, 'director': 'Джеймс Кэмерон', 'rating': 9.0
    },
    {
        'id': 2, 'name': 'Один дома', 'genre': 'комедия', 'year': 1990, 'director': 'Крис Коламбус', 'rating': 8.5
    },
    {
        'id': 3, 'name': 'Аватар', 'genre': 'фантастика', 'year': 2009, 'director': 'Джеймс Кэмерон', 'rating': 8.0
    }
]

@app.route('/')
def index():
    return 'My collection api'

@app.route('/collection')
def get_collection():
    return jsonify(items)

@app.route('/collection/<int:item_id>')
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    
    return {'error': 'Объект не найден'}, 404

@app.route('/collection', methods=['POST'])
def add_items():
    req_data = request.json

    new_item = {
        'id': len(items)+1,
        'name': req_data['name'],
        'genre': req_data['genre'],
        'year': req_data['year'],
        'director': req_data['director'],
        'rating': req_data['rating'],
    }

    items.append(new_item)

    
    return jsonify(new_item), 201

@app.route('/collection/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    req_data = request.json

    for item in items:
        if item['id'] == item_id:
            item['name'] = req_data['name']
            item['genre'] = req_data['genre']
            item['year'] = req_data['year']
            item['director'] = req_data['director']
            item['rating'] = req_data['rating']

            return jsonify(item)
    return {'error': 'Объект не найден'}, 404


if __name__ == '__main__':
    app.run(debug = True)