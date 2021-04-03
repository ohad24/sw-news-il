from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import firestore

load_dotenv()

firebase_admin.initialize_app()

db = firestore.client()
# transaction = db.transaction()
db_news_site = db.collection('news-site')
db_data = db_news_site.document('data')
db_ref_data = db_news_site.document('data-ref')

app = Flask(__name__)


def get_main_page_data():
    db_data_news_col = db_data.collection('news')
    docs_ref = db_data_news_col.order_by(
        u'ts', direction=firestore.Query.DESCENDING).limit(5).stream()
    latest_news = [doc_snap.to_dict() for doc_snap in docs_ref]

    tags_data = db_ref_data.collection('tags').get()
    tags = {}
    for tag_data in tags_data:
        d = tag_data.to_dict()
        tags[d.get('name')] = d
    return latest_news, tags


@app.route('/')
def index():
    latest_news, tags = get_main_page_data()
    return render_template('home.html', latest_news=latest_news, tags=tags)
