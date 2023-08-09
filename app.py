from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

data = [
            {
                'id': 1,
                'title': 'Title 1',
                'description': 'Description 1'
            },
            {
                'id': 2,
                'title': 'Title 2',
                'description': 'Description 2'
            }
       ]


@app.route('/data', methods=['GET'])
def get_list():
    return jsonify(data)


@app.route('/data', methods=['POST'])
def post_list():
    new_one = request.json
    data.append(new_one)
    return jsonify(data)


@app.route('/data/<int:data_id>', methods=['PUT'])
def put_list(data_id):
    item = next((x for x in data if x['id'] == data_id), None)
    params = request.json  # параметры, который переданы для изменения
    if not item:
        return {'message': 'data с таким id не найден'}, 400
    item.update(params)
    return item


@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    idx, _ = next((x for x in enumerate(data) if x[1]['id'] == data_id), (None, None))
    data.pop(idx)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)