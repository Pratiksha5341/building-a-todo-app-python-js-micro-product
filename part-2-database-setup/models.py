from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ============================
# USER MODEL
# ============================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))  # ✅ Activity 1
    password_hash = db.Column(db.String(128), nullable=False)

    todos = db.relationship('Todo', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


# ============================
# TODO MODEL
# ============================
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Todo {self.task_content}>"


# ============================
# INIT DATABASE
# ============================
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
