# Import typing support for type annotations (optional, but good for clarity)
from typing import List, Tuple

def get_user_input() -> list:
    """Collect exam and exercise inputs from the user."""

    # Ask how many results the user wants to enter
    results_input = int(input("How many results would you like to enter? "))
    data = []
    i = 0

    # Collect inputs for the number of results specified
    while i < results_input:
        user_input1 = input(f"({i + 1}) Enter the exam points: ")
        user_input2 = input(f"({i + 1}) Enter the exercises completed: ")
        try:
            # Convert user input strings to integers
            exam_str, exercises_str = user_input1, user_input2
            exam_points = int(exam_str)
            exercises_completed = int(exercises_str)

            # Check if values are within valid ranges
            if 0 <= exam_points <= 30 and 0 <= exercises_completed <= 100:
                data.append((exam_points, exercises_completed))
                i += 1  # Move to the next input
            else:
                print("Invalid input. Exam (0-30), Exercises (0-100).")
        except ValueError:
            print("Invalid input. Please enter two integers.")
    
    # Return list of (exam, exercises) tuples
    return data


def convert_exercise_points(exercises_completed : int) -> int:
    # Convert exercises to exercise points: 1 point per 10 exercises
    return exercises_completed // 10


def calculate_total_points(exam: int, exercises: int) -> int:
    # Total points = exam points + converted exercise points
    return exam + convert_exercise_points(exercises)


def determine_grade(total_points: int) -> int:
    # Determine grade based on total points
    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5


def calculate_statistics(data: list[tuple[int, int]]) -> None:
    # Handle case where no data was entered
    if len(data) == 0:
        print("No data to analyze.")
        return

    total_points_list = []  # To store each student's total points
    grades = []             # To store each student's grade

    # Loop through all (exam, exercises) pairs and compute results
    for exam_points, exercises_completed in data:
        total_points = calculate_total_points(exam_points, exercises_completed)
        grade = determine_grade(total_points)
        total_points_list.append(total_points)
        grades.append(grade)

    # Calculate class average and pass percentage
    average = sum(total_points_list) / len(total_points_list)
    pass_count = len([g for g in grades if g > 0])
    pass_percentage = (pass_count / len(grades)) * 100

    # Display overall statistics
    print("\nStatistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    
    # Show grade distribution using stars
    print("Grade distribution:")
    for g in reversed(range(6)):  # From grade 5 to 0
        stars = grades.count(g)
        print(f"  {g}: {'*' * stars}")

    # Show each student's result with detailed breakdown
    print("\nIndividual results:")
    for i, (exam_points, exercises_completed) in enumerate(data, start=1):
        total_points = calculate_total_points(exam_points, exercises_completed)
        grade = determine_grade(total_points)
        print(f"  Student {i}: Exam {exam_points} + Exercises {convert_exercise_points(exercises_completed)} = Total {total_points} → Grade {grade}")


def main():
    # Start the program: collect input and process it
    data = get_user_input()
    if data:
        calculate_statistics(data)
    else:
        print("No data entered.")


# Only run the main function if this file is executed directly
if __name__ == "__main__":
    main()
