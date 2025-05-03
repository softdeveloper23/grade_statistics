def results() -> list:
    points_exercises = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        points_exercises.append(user_input.split())
    return points_exercises

def calculate_grade(points_exercises : list):
    points = 0
    length = len(points_exercises)
    grade_sum = 0
    for entry in points_exercises:
        exam_points = int(entry[0])
        exercises_completed = int(entry[1])
        points = convert_exercise_points(exercises_completed)
        grade = calculate_course_grade(exam_points, points)
        grade_sum += grade 
        points_average = calculate_average(grade_sum, length)
    print("Statistics:")
    print(f"Points average: {points_average}")
    calculate_grade_distribution(points_exercises, length)

def convert_exercise_points(points : int) -> int:
    exercise_points = points // 10
    return exercise_points

def calculate_course_grade(exam_points : int, points : int) -> int:
    grade = exam_points + points
    return grade

def calculate_average(grade_sum : int, length : int) -> float:
    points_average = grade_sum / length
    return points_average

def calculate_pass_percentage(grade : int, length: int) -> float:
    return 0

def calculate_grade_distribution(points_exercises: list, length):
    grade_0 = grade_1 = grade_2 = grade_3 = grade_4 = grade_5 = 0

    for entry in points_exercises:
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
    points_exercises = results()
    calculate_grade(points_exercises)
    


main()
