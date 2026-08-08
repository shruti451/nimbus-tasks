
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="password",
    database="nimbusdb"
)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        quest = request.form["quest"]

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO tasks (quest, completed) VALUES (%s, %s)",
            (quest, False)
        )

        db.commit()
        cursor.close()

        return redirect("/")

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()
    cursor.close()

    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (id,)
    )

    db.commit()

    return redirect("/")

@app.route("/complete/<int:id>")
def complete(id):
    cursor = db.cursor()

    cursor.execute(
        "UPDATE tasks SET completed = NOT completed WHERE id = %s",
        (id,)
    )

    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)