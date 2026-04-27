def mark_attendance(name):
    with open("attendance.txt", "a") as file:
        file.write(name + " Present\n")
    print(f"{name} marked present")

def view_attendance():
    with open("attendance.txt", "r") as file:
        print(file.read())

# Demo
mark_attendance("Samridhi")
view_attendance()
