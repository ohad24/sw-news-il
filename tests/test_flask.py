import os
import pytest
import sys
import json
sys.path.append("src/")

if os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'src/sa-firestore.json'


from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            # init db
            pass
        app.config['WTF_CSRF_ENABLED'] = False
        yield client


def test_home_page_status_code(client):
    rv = client.get('/')
    assert 200 == rv.status_code


def test_subscription(client):
    rv = client.post('/_subscribe',
                     data=json.dumps({"email": "test@test.com",
                                      "tag_names": ['test1', 'test2']}),
                     content_type='application/json')
    # print(rv.data.decode('utf-8'))
    assert 200 == rv.status_code
