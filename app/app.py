
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []
next_id = 1

@app.route("/",  methods=["GET", "POST"])

def home():
     global next_id
     if request.method == "POST":

        quest = request.form["quest"]

        task = {
    "id": next_id,
    "quest": quest,
    "completed": False
      }

        tasks.append(task)

        next_id += 1

     return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break

    return redirect("/")

@app.route("/complete/<int:id>")
def complete(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = not task["completed"]
            break

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)