def show_analytics(students, total_processed, rejection_reasons):
    accepted = len(students)
    rejected = total_processed - accepted
    accuracy = (accepted / total_processed * 100) if total_processed else 0

    phone_counts = {"9": 0, "8": 0, "7": 0, "6": 0}
    domain_counts = {}

    for student in students:
        first_digit = student["phone"][0]
        phone_counts[first_digit] += 1
        domain = "@" + student["email"].split("@")[1]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    print("\\n=======================================================")
    print("       STUDENT REGISTRATION - BUSINESS INTELLIGENCE")
    print("=======================================================")
    print(f"Total Contacts Processed : {total_processed}")
    print(f"Valid Registrations      : {accepted}")
    print(f"Rejected Records         : {rejected}")
    print(f"Data Quality Accuracy    : {accuracy:.1f}%")

    print("\\n--- Telecom Network Breakdown ---")
    for digit in ["9", "8", "7", "6"]:
        print(f"{digit}-Series : {phone_counts[digit]} students")

    print("\\n--- Email Domain Breakdown ---")
    for domain, count in sorted(domain_counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{domain:<22}: {count} students")

    print("\\n--- Rejection Reasons ---")
    for reason, count in rejection_reasons.items():
        print(f"{reason:<25}: {count}")
    print("=======================================================\\n")
