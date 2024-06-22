import pytest
from app import create_app, db
from app.models import User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()


def test_register(test_client):
    response = test_client.post('/register', data=dict(
        username='testuser',
        password='testpass',
        confirm_password='testpass'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Account created successfully!' in response.data


def test_login(test_client):
    test_client.post('/register', data=dict(
        username='testuser',
        password='testpass',
        confirm_password='testpass'
    ), follow_redirects=True)
    response = test_client.post('/login', data=dict(
        username='testuser',
        password='testpass'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged in successfully' in response.data
