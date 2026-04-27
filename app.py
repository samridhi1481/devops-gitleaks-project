from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def mark_attendance(name):
    with open("attendance.txt", "a") as file:
        file.write(name + " Present\n")

def get_attendance():
    try:
        with open("attendance.txt", "r") as file:
            return file.readlines()
    except:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            mark_attendance(name)
        return redirect("/")
    
    records = get_attendance()
    return render_template("index.html", records=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)