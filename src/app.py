from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

load_dotenv()

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': os.getenv('GCP_PROJECT_ID'),
})

db = firestore.client()
col = db.collection('news')

app = Flask(__name__)

@app.route('/')
def index():
    docs_ref = col.order_by(u'ts', direction=firestore.Query.DESCENDING).limit(5).stream()
    docs = [doc_snap.to_dict() for doc_snap in docs_ref]
    return render_template('home.html', docs=docs)

# if __name__ == '__main__':
#     app.config['TESTING'] = True
