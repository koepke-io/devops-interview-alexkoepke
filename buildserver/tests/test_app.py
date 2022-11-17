import re


def test_index(client):
    response = client.get("/")

    assert response.text == "Hello from EnergyHub!"
