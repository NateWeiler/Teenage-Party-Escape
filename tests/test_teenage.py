import teenage

def test_import():
    assert teenage

def test_config():
    assert not teenage.create_app().testing
    assert teenage.create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
