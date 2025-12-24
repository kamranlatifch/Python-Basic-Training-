# file name: grade_programme.py


def calculate_average_grade():

    total = 0
    count = 0

    while True:
        try:
            grade = float(input("Please enter a grade (enter 0 to finish): "))
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
            continue

        if grade == 0:
            break

        total += grade
        count += 1

    if count == 0:
        print("No grades were entered.")
    else:
        average = total / count
        print(f"Average: {average}")


calculate_average_grade()
