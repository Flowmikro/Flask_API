from app import client


def test_get():
    res = client.get('/data')

    assert res.status_code == 200
    assert len(res.get_json()) == 2
    assert res.get_json()[0]['id'] == 1


def test_post():
    data = {
        'id': 3,
        'title': 'Test 3',
        'description': 'Description 3'
    }

    res = client.post('/data', json=data)

    assert res.status_code == 200
    assert len(res.get_json()) == 3
    assert res.get_json()[-1]['title'] == data['title']
