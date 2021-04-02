import pytest
import sys
sys.path.append("src/")


import os
if os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is not None:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'src/sa-firestore.json'


from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            # init db
            pass
        yield client


def test_home_page_status_code(client):
    rv = client.get('/')
    assert 200 == rv.status_code