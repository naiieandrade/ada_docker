from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_ada:password_ada@db/db_ada'
db = SQLAlchemy(app)

class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(255), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        novo_dado = Dados(user_input=user_input)
        db.session.add(novo_dado)
        db.session.commit()
        return f'Você enviou: {user_input} e os dados foram adicionados ao banco!'
    return render_template('index.html')

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()
    app.run(debug=True, host='0.0.0.0')