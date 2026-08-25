# Student Grade Manager

students = {}


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    math = float(input("Enter Math mark: "))
    science = float(input("Enter Science mark: "))
    english = float(input("Enter English mark: "))

    total = math + science + english
    average = total / 3
    grade = calculate_grade(average)

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    print(f"\nStudent '{name}' added successfully!")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def display_students():
    if not students:
        print("\nNo students available.")
        return

    print("\n========== STUDENT DETAILS ==========")

    for name, data in students.items():
        print(f"\nName    : {name}")
        print(f"Math    : {data['Math']}")
        print(f"Science : {data['Science']}")
        print(f"English : {data['English']}")
        print(f"Total   : {data['Total']}")
        print(f"Average : {data['Average']:.2f}")
        print(f"Grade   : {data['Grade']}")


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        data = students[name]

        print("\nStudent Found!")
        print(f"Name    : {name}")
        print(f"Math    : {data['Math']}")
        print(f"Science : {data['Science']}")
        print(f"English : {data['English']}")
        print(f"Total   : {data['Total']}")
        print(f"Average : {data['Average']:.2f}")
        print(f"Grade   : {data['Grade']}")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n========== STUDENT GRADE MANAGER ==========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


main()