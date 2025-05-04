def get_user_input() -> list:
    """Collect exam and exercise inputs from the user."""
    results_input = int(input("How many results would you like to enter? "))
    data = []
    i = 0
    while i < results_input:
        user_input1 = input(f"({i + 1}) Enter the exam points: ")
        user_input2 = input(f"({i + 1}) Enter the exercises completed: ")
        try:
            exam_str, exercises_str = user_input1, user_input2
            exam_points = int(exam_str)
            exercises_completed = int(exercises_str)
            if 0 <= exam_points <= 30 and 0 <= exercises_completed <= 100:
                data.append((exam_points, exercises_completed))
                i += 1 
            else:
                print("Invalid input. Exam (0-30), Exercises (0-100).")
        except ValueError:
            print("Invalid input. Please enter two integers.")   
    return data

def convert_exercise_points(exercises_completed : int) -> int:
    return exercises_completed // 10

def calculate_total_points(exam: int, exercises: int) -> int: 
    return exam + convert_exercise_points(exercises)

def determine_grade(total_points: int) -> int: 
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
    total_points_list = []
    grades = []

    for exam_points, exercises_completed in data:
        total_points = calculate_total_points(exam_points, exercises_completed)
        grade = determine_grade(total_points)
        total_points_list.append(total_points)
        grades.append(grade)

    average = sum(total_points_list) / len(total_points_list)
    pass_count = len([g for g in grades if g > 0])
    pass_percentage = (pass_count / len(grades)) * 100

    print("\nStatistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for g in reversed(range(6)):
        stars = grades.count(g)
        print(f"  {g}: {'*' * stars}")

def main():
    data = get_user_input()
    if data:
        calculate_statistics(data)
    else:
        print("No data entered.")


if __name__ == "__main__":
    main()
