from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

from datetime import datetime


app = Flask(__name__)
DB_NAME = "edufin.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            amount REAL,
            expense_date TEXT
        )
    """)
    db.commit()
    db.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        category = request.form["category"]
        amount = request.form["amount"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        db = get_db()
        db.execute(
            "INSERT INTO expenses (title, category, amount, expense_date) VALUES (?, ?, ?, ?)",
            (title, category, amount, date)
        )
        db.commit()
        db.close()
        return redirect("/expenses")

    return render_template("add.html")


@app.route("/expenses")
def expenses():
    db = get_db()
    data = db.execute("SELECT * FROM expenses").fetchall()
    db.close()
    return render_template("expenses.html", expenses=data)


@app.route("/summary")
def summary():
    db = get_db()
    data = db.execute("""
        SELECT substr(expense_date, 1, 7) AS month, SUM(amount) AS total
        FROM expenses
        GROUP BY month
    """).fetchall()
    db.close()
    return render_template("summary.html", summary=data)


@app.route("/api/expenses")
def api_expenses():
    db = get_db()
    data = db.execute("SELECT * FROM expenses").fetchall()
    db.close()
    return jsonify([dict(row) for row in data])

@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    db = get_db()
    db.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    db.commit()
    db.close()
    return redirect("/expenses")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
