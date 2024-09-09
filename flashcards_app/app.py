from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# DB Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Flashcard Model
class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem_title = db.Column(db.String(100), nullable=False)
    problem_url = db.Column(db.String(200), nullable=False)
    current_level = db.Column(db.Integer, default=0)
    difficulty = db.Column(db.String(10), nullable=False)

# Initialize DB
with app.app_context():
    db.create_all()

# Route to display flashcards
@app.route('/')
def index():
    flashcards = Flashcard.query.all()
    return render_template('index.html', flashcards=flashcards)

# Route to add a new flashcard
@app.route('/add', methods=['POST'])
def add_flashcard():
    problem_title = request.form['problem_title']
    problem_url = request.form['problem_url']
    difficulty = request.form['difficulty']  

    if not difficulty:
        return "Difficulty is required", 400

    new_flashcard = Flashcard(
        problem_title=problem_title,
        problem_url=problem_url,
        current_level=0,  
        difficulty=difficulty  
    )

    db.session.add(new_flashcard)
    db.session.commit()

    return redirect(url_for('index'))


# Route to update flashcard level
@app.route('/move/<int:flashcard_id>/<direction>')
def move_flashcard(flashcard_id, direction):
    flashcard = Flashcard.query.get(flashcard_id)
    if direction == 'up' and flashcard.current_level < 5:
        flashcard.current_level += 1
    elif direction == 'down' and flashcard.current_level > 0:
        flashcard.current_level -= 1
    db.session.commit()
    return redirect(url_for('index'))

# Route to delete a flashcard
@app.route('/delete/<int:flashcard_id>')
def delete_flashcard(flashcard_id):
    flashcard = Flashcard.query.get(flashcard_id)
    db.session.delete(flashcard)
    db.session.commit()
    return redirect(url_for('index'))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
