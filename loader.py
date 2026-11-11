import csv
from validator import validate_contact

INPUT_FILE = "contacts.csv"
OUTPUT_FILE = "students_clean.csv"
FIELDS = ["name", "phone", "email"]

def load_contacts():
    students = []
    seen_phones = set()
    seen_emails = set()
    rejection_reasons = {}
    total = 0

    with open(INPUT_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += 1
            name = row.get("name", "")
            phone = row.get("phone", "").strip()
            email = row.get("email", "").strip().lower()

            valid, reason = validate_contact(name, phone, email)
            if not valid:
                rejection_reasons[reason] = rejection_reasons.get(reason, 0) + 1
                print(f"Rejected row {total}: {reason}")
                continue

            if phone in seen_phones:
                reason = "Duplicate phone"
            elif email in seen_emails:
                reason = "Duplicate email"
            else:
                reason = ""

            if reason:
                rejection_reasons[reason] = rejection_reasons.get(reason, 0) + 1
                print(f"Rejected row {total}: {reason}")
                continue

            student = {"name": name.strip(), "phone": phone, "email": email}
            students.append(student)
            seen_phones.add(phone)
            seen_emails.add(email)

    save_students(students)
    accepted = len(students)
    print("\\n========== INGESTION SUMMARY ==========")
    print(f"Total rows read       : {total}")
    print(f"Valid rows accepted   : {accepted}")
    print(f"Rejected rows         : {total - accepted}")
    print("Rejection reasons:")
    for reason, count in rejection_reasons.items():
        print(f"  {reason}: {count}")
    print("=======================================\\n")
    return students, total, rejection_reasons

def save_students(students):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    load_contacts()
