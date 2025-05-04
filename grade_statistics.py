def get_user_input() -> list:
    """Collect exam and exercise inputs from the user."""
    data = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        try:
            exam_str, exercises_str = user_input.split()
            exam_points = int(exam_str)
            exercises_completed = int(exercises_str)
            if 0 <= exam_points <= 30 and 0 <= exercises_completed <= 100:
                data.append((exam_points, exercises_completed))
            else:
                print("Invalid input. Exam (0-30), Exercises (0-100).")
        except ValueError:
            print("Invalid input. Please enter two integers.")    
    return data

def calculate_grade(data : list):
    points = 0
    length = len(data)
    grade_sum = 0
    for entry in data:
        exam_points = int(entry[0])
        exercises_completed = int(entry[1])
        grade_sum += grade 
        points_average = calculate_average(grade_sum, length)
    print("Statistics:")
    print(f"Points average: {points_average}")
    calculate_grade_distribution(data, length)

def convert_exercise_points(exercises_completed : int) -> int:
    return exercises_completed // 10

def calculate_total_points(exam: int, exercises: int) -> int: # Added this new function. Need to delete other irrelevant code and functions.
    return exam + convert_exercise_points(exercises)

def calculate_statistics(data: list):
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

def determine_grade(total_points: int) -> int: # Added this new function. Need to delete other irrelevant code and functions.
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

def calculate_course_grade(exam_points : int, points : int) -> int:
    grade = exam_points + points
    return grade

def calculate_average(grade_sum : int, length : int) -> float:
    points_average = grade_sum / length
    return points_average

def calculate_pass_percentage(grade : int, length: int) -> float:
    return 0

def calculate_grade_distribution(data: list, length):
    grade_0 = grade_1 = grade_2 = grade_3 = grade_4 = grade_5 = 0

    for entry in data:
        exam_points = int(entry[0])
        exercises_completed = int(entry[1])
        points = convert_exercise_points(exercises_completed)
        if exam_points < 10:
            grade = 0
        else:
            grade = calculate_course_grade(exam_points, points)

        if grade <= 14:
            grade_0 += 1
        elif grade <= 17:
            grade_1 += 1 
        elif grade <= 20:
            grade_2 += 1 
        elif grade <= 23:
            grade_3 += 1 
        elif grade <= 27:
            grade_4 += 1 
        else:  # grade <= 30
            grade_5 += 1 

    pass_percentage = (1 - (grade_0 / length)) * 100

    print(f"Pass percentage: {pass_percentage:.1f}")

    print("Grade distribution:")
    print(f"  5: {'*' * grade_5}")
    print(f"  4: {'*' * grade_4}")
    print(f"  3: {'*' * grade_3}")
    print(f"  2: {'*' * grade_2}")
    print(f"  1: {'*' * grade_1}")
    print(f"  0: {'*' * grade_0}")



def main():
    data = get_user_input()
    calculate_grade(data)
    


main()
