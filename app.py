def mark_attendance(name):
    with open("attendance.txt", "a") as file:
        file.write(name + " Present\n")
    print(f"{name} marked present")

def view_attendance():
    try:
        with open("attendance.txt", "r") as file:
            print("\nAttendance Records:\n")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records found.")

def menu():
    while True:
        print("\n--- Attendance Management System ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            mark_attendance(name)
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()