from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_read():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API de Loja de Roupas funcionando!"}

def test_register_roupa():
    json = {
        "nome": "Camiseta Básica",
        "tamanho": "M",
        "marca": "MarcaX",
        "novo": True,
        "preco": 49.90
    }
    response = client.post("/roupas/", json=json)

    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Camiseta Básica"
    assert data["tamanho"] == "M"
    assert data["marca"] == "MarcaX"

def test_all_roupa():
    response = client.get("/roupas/")

    assert response.status_code == 200
    assert type(response.json()) == list

def test_get_roupa_error():
    response = client.get("/roupas/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Roupa não encontrada!"

def test_patch_roupa():

    json = {
        "novo": False
    }

    response = client.patch("/roupas/1", json=json)

    assert response.status_code == 200

def test_delete_roupa():
    json = {
        "nome": "Calça Jeans",
        "tamanho": "42",
        "marca": "JeansCo",
        "novo": True,
        "preco": 120.00
    }

    response1 = client.post("/roupas/", json=json)

    assert response1.status_code == 200

    id = response1.json()["id"]

    response2 = client.delete(f"/roupas/{id}")

    assert response2.status_code == 200

    assert response2.json()["message"] == "Roupa deletada com sucesso!"
