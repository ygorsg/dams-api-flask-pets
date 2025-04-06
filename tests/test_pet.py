import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from app import app

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste."""
    with app.test_client() as client:
        yield client

def test_get_all_pets(client):
    """Teste para listar todos os pets."""
    response = client.get('/api/pet/')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    if response.json:
        assert 'id' in response.json[0]
        assert 'nome' in response.json[0]
        assert 'tipo' in response.json[0]
        assert 'idade' in response.json[0]

def test_create_pet(client):
    """Teste para criar um novo pet."""
    new_pet = {"nome": "Filomena", "tipo": "Cobra", "idade": 3}
    response = client.post('/api/pet/', json=new_pet)
    assert response.status_code == 201
    assert response.json['nome'] == "Filomena"
    assert response.json['tipo'] == "Cobra"
    assert response.json['idade'] == 3

def test_get_pet_by_id(client):
    """Teste para buscar um pet por ID."""
    pet_id = 1
    response = client.get(f'/api/pet/{pet_id}')
    assert response.status_code == 200
    assert response.json['id'] == pet_id

def test_update_pet(client):
    """Teste para atualizar um pet existente."""
    pet_id = 1 
    updated_data = {"nome": "Rex Atualizado", "tipo": "Cachorro", "idade": 4}
    response = client.put(f'/api/pet/{pet_id}', json=updated_data)
    assert response.status_code == 200
    assert response.json['nome'] == "Rex Atualizado"
    assert response.json['idade'] == 4

def test_delete_pet(client):
    """Teste para deletar um pet."""
    pet_id = 1 
    response = client.delete(f'/api/pet/{pet_id}')
    assert response.status_code == 204  # No Content
