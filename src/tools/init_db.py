# from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred = credentials.Certificate('src/sa-firestore.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
db_news_site = db.collection('news-site')
db_data_ref = db_news_site.document('data-ref')
db_data_ref_tags = db_data_ref.collection('tags')

tags = [{"name": "Database", "hex_color": "#de1010", "style-cls": "database"},
        {"name": "Frontend", "hex_color": "#deae10", "style-cls": "frontend"},
        {"name": "Backend", "hex_color": "#66de10", "style-cls": "backend"},
        {"name": "Tech", "hex_color": "#10dede", "style-cls": "tech"},
        {"name": "Team Development", "hex_color": "#4c34eb", "style-cls": "team-dev"}]

for tag_data in tags:
    db_data_ref_tags.document(tag_data.get('name')).set(tag_data)
