from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# In-memory storage for notes
notes = []

@app.route("/")
def home():
    return render_template("home.html", notes=notes)

@app.route("/new_note")
def new_note():
    return render_template("new_note.html")

@app.route("/create_note", methods=["POST"])
def create_note():
    title = request.form["title"]
    content = request.form["content"]
    notes.append({"title": title, "content": content})
    return redirect("/")

@app.route("/edit_note/<int:index>")
def edit_note(index):
    note = notes[index]
    return render_template("edit_note.html", index=index, note=note)

@app.route("/update_note/<int:index>", methods=["POST"])
def update_note(index):
    title = request.form["title"]
    content = request.form["content"]
    notes[index] = {"title": title, "content": content}
    return redirect("/")

@app.route("/delete_note/<int:index>")
def delete_note(index):
    del notes[index]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
