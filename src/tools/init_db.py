# from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# load_dotenv()

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': os.getenv('GCP_PROJECT_ID'),
})

db = firestore.client()
db_news_site = db.collection('news-site')
db_data_ref = db_news_site.document('data-ref')
db_data_ref_tags = db_data_ref.collection('tags')

tags = [{"name": "Database", "hex_color": "#de1010"},
{"name": "Frontend", "hex_color": "#deae10"},
{"name": "Backend", "hex_color": "#66de10"},
{"name": "Tech", "hex_color": "#10dede"}]

for tag_data in tags:
    db_data_ref_tags.document(tag_data.get('name')).set(tag_data)

