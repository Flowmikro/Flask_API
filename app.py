from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

data = [
            {
                'title': 'Title 1',
                'description': 'Description 1'
            },
            {
                'title': 'Title 2',
                'description': 'Description 2'
            }
       ]


@app.route('/', methods=['GET'])
def get_list():
    return jsonify(data)


@app.route('/', methods=['POST'])
def update_list():
    new_one = request.json
    data.append(new_one)
    return jsonify(data)






if __name__ == '__main__':
    app.run(debug=True)