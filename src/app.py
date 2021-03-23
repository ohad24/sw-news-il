from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# if __name__ == '__main__':
#     app.config['TESTING'] = True
