from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'id': 1,
    }
