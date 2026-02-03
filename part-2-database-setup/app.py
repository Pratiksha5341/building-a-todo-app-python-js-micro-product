from flask import Flask, render_template
from models import db, User, Todo, init_db

app = Flask(__name__)

# ============================
# DATABASE CONFIG
# ============================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)


# ============================
# ROUTES
# ============================

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test-db')
def test_db():
    """
    Creates 3 users and multiple todos.
    Demonstrates query operations.
    """

    # ----------------------------
    # ACTIVITY 4: ADD TEST DATA
    # ----------------------------
    users_data = [
        ('alice', 'alice@mail.com', '1111111111'),
        ('bob', 'bob@mail.com', '2222222222'),
        ('charlie', 'charlie@mail.com', '3333333333')
    ]

    for username, email, phone in users_data:
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(
                username=username,
                email=email,
                phone=phone,
                password_hash='temp'
            )
            db.session.add(user)
            db.session.commit()

            todo1 = Todo(task_content=f"{username}'s first task", user_id=user.id)
            todo2 = Todo(task_content=f"{username}'s second task", user_id=user.id)
            db.session.add_all([todo1, todo2])
            db.session.commit()

    # ----------------------------
    # ACTIVITY 2: QUERY PRACTICE
    # ----------------------------
    all_users = User.query.all()
    first_user = User.query.first()
    user_count = User.query.count()

    all_todos = Todo.query.all()

    return render_template(
        'test_db.html',
        users=all_users,
        todos=all_todos,
        first_user=first_user,
        user_count=user_count
    )


# ============================
# RUN SERVER
# ============================
if __name__ == '__main__':
    print("\n" + "="*50)
    print("  Part 2: Database Setup")
    print("  Home: http://127.0.0.1:5000")
    print("  Test DB: http://127.0.0.1:5000/test-db")
    print("="*50 + "\n")
    app.run(debug=True)
