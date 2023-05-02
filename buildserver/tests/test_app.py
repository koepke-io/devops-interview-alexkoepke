import json
import re
import os


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello from EnergyHub!"


def test_index(client):
    response = client.get("/status")
    data = json.loads(response.data)

    # print the precess ids
    # print(f"/status pid: {data['pid']}")
    # print(f"server pid: {os.getpid()}")

    assert response.status_code == 200
    assert "pid" in data
    assert "status" in data
    # ensure the pid returned is the same as the process id of the server
    assert os.getpid() == data["pid"]
    assert data["status"] == "ok"
