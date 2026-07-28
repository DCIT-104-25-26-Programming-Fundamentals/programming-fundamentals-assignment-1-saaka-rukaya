# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_average(scores):
    total_score = 0

    for score in scores:
        total_score = total_score + score

    average_score = total_score / len(scores)
    return round(average_score, 2)


def student_id_exists(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return True

    return False


def add_student(students):
    student_name = input("Student name: ").strip()

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    if student_id_exists(students, student_id):
        print("Error: A student with this ID already exists.")
        return

    try:
        number_of_scores = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    if number_of_scores <= 0:
        print("Error: Number of scores must be greater than zero.")
        return

    scores = []

    for score_number in range(1, number_of_scores + 1):
        try:
            student_score = float(
                input("Enter score " + str(score_number) + ": ")
            )

            if student_score < 0 or student_score > 100:
                print("Error: Scores must be between 0 and 100.")
                return

            scores.append(student_score)

        except ValueError:
            print("Error: Please enter a valid score.")
            return

    student_record = {
        "name": student_name,
        "id": student_id,
        "scores": scores
    }

    students.append(student_record)

    print('Student "' + student_name + '" added successfully.')


def display_all_students(students):
    if len(students) == 0:
        print("No student records have been added yet.")
        return

    print("\n" + "-" * 70)
    print(f"{'Name':<20}{'ID':<15}{'Scores':<25}{'Average':<10}")
    print("-" * 70)

    for student in students:
        scores_text = ""

        for score_number in range(len(student["scores"])):
            scores_text = scores_text + str(student["scores"][score_number])

            if score_number < len(student["scores"]) - 1:
                scores_text = scores_text + ", "

        average_score = calculate_average(student["scores"])

        print(
            f"{student['name']:<20}"
            f"{student['id']:<15}"
            f"{scores_text:<25}"
            f"{average_score:<10.2f}"
        )

    print("-" * 70)


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def display_student_average(students):
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    student = find_student(students, student_id)

    if student is None:
        print("Error: Student ID not found.")
    else:
        average_score = calculate_average(student["scores"])

        print(
            student["name"] + "'s average score:",
            format(average_score, ".2f")
        )


def display_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        display_menu()
        menu_choice = input("Enter your choice (1-4): ")

        if menu_choice == "1":
            add_student(students)

        elif menu_choice == "2":
            display_all_students(students)

        elif menu_choice == "3":
            display_student_average(students)

        elif menu_choice == "4":
            print("Goodbye!")
            break

        else:
            print("Error: Please enter a number from 1 to 4.")


main()