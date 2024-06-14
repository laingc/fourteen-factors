from flask import Flask, render_template, request, jsonify, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# In-memory database
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
        socketio.emit('update', {'items': items})
        return jsonify({'item': item})
    return jsonify({'error': 'Item cannot be empty'}), 400

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

@app.route('/api/items', methods=['POST'])
def api_add_item():
    data = request.json
    item = data.get('item')
    if item:
        items.append(item)
        socketio.emit('update', {'items': items})
        return jsonify({'item': item})
    return jsonify({'error': 'Item cannot be empty'}), 400

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        removed_item = items.pop(item_id)
        socketio.emit('update', {'items': items})
        return jsonify({'removed_item': removed_item})
    return jsonify({'error': 'Invalid item ID'}), 400

@app.route('/api/socket')
def get_socket_url():
    socket_url = url_for('index', _external=True).replace('http', 'ws')
    return jsonify({'socket_url': socket_url})

if __name__ == '__main__':
    socketio.run(app, debug=True)
