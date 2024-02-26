from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://my_user:my_password@db/my_database'
# db = SQLAlchemy(app)

@app.route('/')
def hello():
	#return 'Hello, Flask in Docker with Database NAIARAs!'
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)