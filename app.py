from flask import Flask, request

app = Flask(__name__)

attendance = []

def mark_attendance(name):
    attendance.append(name + " Present")

def view_attendance():
    return attendance

@app.route("/")
def home():
    return """
    <h1>Attendance System</h1>
    <p>Use /mark?name=YourName</p>
    <p>Use /view to see records</p>
    """

@app.route("/mark")
def mark():
    name = request.args.get("name")
    mark_attendance(name)
    return f"{name} marked present"

@app.route("/view")
def view():
    return "<br>".join(view_attendance()) if attendance else "No records"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)