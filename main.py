from loader import load_contacts, save_students
from validator import validate_contact
from analytics import show_analytics

students, total_processed, rejection_reasons = load_contacts()

def print_students():
    if not students:
        print("No student records found.")
        return
    print("\\nID  NAME                 PHONE       EMAIL")
    print("-" * 72)
    for i, s in enumerate(students, start=1):
        print(f"{i:<3} {s['name']:<20} {s['phone']:<11} {s['email']}")

def find_student(query):
    query = query.strip().lower()
    for i, s in enumerate(students):
        if query in (s["phone"].lower(), s["email"].lower()) or query == s["name"].lower():
            return i
    return None

def unique_contact(phone, email, ignore_index=None):
    for i, s in enumerate(students):
        if i != ignore_index and (s["phone"] == phone or s["email"].lower() == email.lower()):
            return False
    return True

def register_student():
    name = input("Enter student name: ")
    phone = input("Enter 10-digit phone: ")
    email = input("Enter email: ")
    valid, reason = validate_contact(name, phone, email)
    if not valid:
        print("Registration rejected:", reason)
    elif not unique_contact(phone.strip(), email.strip()):
        print("Registration rejected: duplicate phone or email.")
    else:
        students.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip().lower()})
        save_students(students)
        print("Student registered successfully.")

def update_student():
    query = input("Enter student ID, phone, email or exact name: ").strip()
    index = None
    if query.isdigit() and 1 <= int(query) <= len(students):
        index = int(query) - 1
    else:
        index = find_student(query)
    if index is None:
        print("Student not found.")
        return
    old = students[index]
    print("Press Enter to keep an existing value.")
    name = input(f"Name [{old['name']}]: ").strip() or old["name"]
    phone = input(f"Phone [{old['phone']}]: ").strip() or old["phone"]
    email = input(f"Email [{old['email']}]: ").strip() or old["email"]
    valid, reason = validate_contact(name, phone, email)
    if not valid:
        print("Update rejected:", reason)
    elif not unique_contact(phone, email, index):
        print("Update rejected: duplicate phone or email.")
    else:
        students[index] = {"name": name, "phone": phone, "email": email.lower()}
        save_students(students)
        print("Student updated successfully.")

def delete_student():
    query = input("Enter student ID or phone number: ").strip()
    index = None
    if query.isdigit() and 1 <= int(query) <= len(students):
        index = int(query) - 1
    else:
        for i, s in enumerate(students):
            if s["phone"] == query:
                index = i
                break
    if index is None:
        print("Student not found.")
    else:
        removed = students.pop(index)
        save_students(students)
        print("Deleted:", removed["name"])

def search_student():
    query = input("Enter name, phone or email: ")
    index = find_student(query)
    if index is None:
        print("Student not found.")
    else:
        print_students() if False else print(students[index])

def menu():
    while True:
        print("\\n===== STUDENT REGISTRATION SYSTEM =====")
        print("1. View All Students")
        print("2. Search Record")
        print("3. Register Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Analytics Report")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print_students()
        elif choice == "2":
            search_student()
        elif choice == "3":
            register_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_analytics(students, total_processed, rejection_reasons)
        elif choice == "7":
            save_students(students)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1 to 7.")

if __name__ == "__main__":
    menu()
