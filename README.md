# Student Registration & Contact Intelligence System

## Project overview
A beginner-friendly Python project that reads student contacts from a CSV file, validates names, phone numbers and email addresses, rejects duplicate phone numbers/emails, provides a menu to manage students, and prints a business-intelligence summary.

## Requirements
- Python 3
- No third-party packages are required.

## Project files
- `contacts.csv` — original sample input.
- `validator.py` — checks name, phone and email.
- `loader.py` — reads the input CSV, rejects invalid/duplicate rows and creates `students_clean.csv`.
- `analytics.py` — calculates acceptance, phone-prefix and email-domain summaries.
- `main.py` — interactive menu for viewing, searching, adding, updating and deleting.
- `proof/` — sample test evidence.

## How to run
1. Extract the project folder.
2. Open a terminal in the `student_registration` folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Choose menu options 1–7. Option 7 saves the current records and exits.

To run only the initial CSV loader, use `python loader.py`.

## Validation rules
- Name must not be blank.
- Phone must contain exactly 10 digits and begin with 6, 7, 8 or 9.
- Email must contain exactly one `@`, no spaces, a non-empty part before `@`, and a domain containing a period that is not at the beginning or end.
- Phone numbers and email addresses must be unique.

## Learning outcomes
This project practices variables, strings, lists, dictionaries, functions, sets, loops, conditionals, CSV file handling and modular programming.\n