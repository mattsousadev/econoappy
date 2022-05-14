
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_operations():
    response = client.get('/operation/')
    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "data":[],
        "size": 0
    }

def test_post_operations():
    response = client.post('/operation/',
        json={
            "code": '1',
            "value": 1,
            "description": "Teste"
        })
    assert response.status_code == 201
    assert response.json() == {
        "success": True,
        "data": {
            "code": '1',
            "value": 1,
            "description": "Teste"
        },
        "message": "Registro inserido com sucesso!"
    }

def test_delete_operations():
    response = client.delete('/operation/1')
    assert response.status_code == 204
