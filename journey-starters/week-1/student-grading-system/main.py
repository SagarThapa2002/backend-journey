from student import Student

def main() -> None:
    try:
        subjects = [
            "Maths",
            "AI",
            "Networking",
            "Databases",
            "Software Engineering"
            ]
        marks = []
        print("Enter marks: ")

        for subject in subjects:
            value = float(input(f"{subject}: "))
            marks.append(value)

        student = Student(marks)

        print("\n--- Result ---")
        print(f"Percentage: {student.get_percentage():.2f}%")
        print(f"Grade: {student.get_grade()}")

    except ValueError as error:
        print(f"Error : {error}")
    

if __name__== "__main__":
    main()